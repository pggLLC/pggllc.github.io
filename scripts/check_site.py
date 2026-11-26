from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set();self.h1=0;self.title=False;self.desc=False;self.lang=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.title=True
  if tag=='meta' and a.get('name')=='description':self.desc=True
  if tag=='html' and a.get('lang'):self.lang=True
  for k in ['href','src']:
   if k in a:self.links.append(a[k])
pages={}
for file in root.rglob('*.html'):
 q=Page();q.feed(file.read_text());pages[file]=q
errors=[];count=0
for asset in (root/'assets').glob('*.svg'):
 try:ET.parse(asset)
 except ET.ParseError as e:errors.append(f'{asset.name}: invalid SVG: {e}')
for file,q in pages.items():
 if file.name=='housing-insights.html':continue
 if not(q.h1==1 and q.title and q.desc and q.lang):errors.append(f'{file}: document semantics')
 for link in q.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(root/unquote(u.path).lstrip('/')) if u.path.startswith('/') else file.parent/unquote(u.path)
  if not u.path:target=file
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{file.name}: missing {link}')
  elif u.fragment and target in pages and u.fragment not in pages[target].ids:errors.append(f'{file.name}: missing fragment {link}')
  count+=1
print(f'Checked {len(pages)-1} new pages and {count} local references; preserved legacy analysis excluded from new-page semantics.')
if errors:print('\n'.join(errors));sys.exit(1)
print('PASS')
