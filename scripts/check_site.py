"""Check generated HTML, local links, and shared accessibility landmarks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import xml.etree.ElementTree as ET

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
assert (root / 'index.html').exists(), 'Build the site before checking it.'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.links, self.ids, self.errors = path, [], set(), []
        self.h1 = self.main = self.footer = self.current = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:
                self.errors.append('duplicate id: ' + a['id'])
            self.ids.add(a['id'])
        self.h1 += tag == 'h1'
        self.main += tag == 'main'
        self.footer += tag == 'footer'
        self.current += a.get('aria-current') == 'page'
        if tag == 'img' and 'alt' not in a:
            self.errors.append('image without alt text')
        for key in ('href', 'src'):
            if key in a:
                self.links.append(a[key])

pages = {}
for path in root.rglob('*.html'):
    page = Page(path)
    page.feed(path.read_text())
    pages[path] = page
errors = []
for path, page in pages.items():
    for message in page.errors:
        errors.append(f'{path.relative_to(root)}: {message}')
    if (page.h1, page.main, page.footer) != (1, 1, 1):
        errors.append(f'{path.name}: expected one h1, main and footer')
    if path.name != '404.html' and page.current != 1:
        errors.append(f'{path}: expected one current navigation link')
    for link in page.links:
        url = urlsplit(link)
        if url.scheme in ('mailto', 'tel') or url.netloc not in ('', 'unaigomezhernandez.github.io'):
            continue
        target = (root / unquote(url.path).lstrip('/') if url.path.startswith('/') else path.parent / unquote(url.path)).resolve() if url.path else path
        if target.is_dir():
            target /= 'index.html'
        if not target.is_file():
            errors.append(f'{path.relative_to(root)}: missing local target {link}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{path.relative_to(root)}: missing anchor {link}')
ET.parse(root / 'feed.xml')
assert len(pages) == 6, f'Expected six public pages, found {len(pages)}; check demo post exclusion.'
assert len(ET.parse(root / 'feed.xml').findall('.//item')) == 0, 'Demo posts remain in feed'
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} pages; local links and fragments, landmarks, image alternatives, navigation, feed, and demo exclusion.')
