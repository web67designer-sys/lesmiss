"""Vercel serverless endpoint: read-only live public Shopify product data."""
from http.server import BaseHTTPRequestHandler
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
import json

HANDLES = ['swan-charm', 'pink-ballet-slippers-charm', 'necklace-base', 'custom-style-bundle-1']
FIELDS = ('handle', 'title', 'price', 'price_varies', 'compare_at_price', 'available', 'featured_image')

def get_product(handle):
    try:
        req = Request('https://lesmissnyc.com/products/' + handle + '.js', headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'})
        with urlopen(req, timeout=6) as response:
            product = json.load(response)
        return {field: product.get(field) for field in FIELDS}
    except (OSError, ValueError, TimeoutError):
        return None

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with ThreadPoolExecutor(max_workers=4) as pool:
            products = [p for p in pool.map(get_product, HANDLES) if p]
        body = json.dumps(products).encode('utf-8')
        self.send_response(200 if products else 503)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Cache-Control', 'public, max-age=60')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)
