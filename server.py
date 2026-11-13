"""Local concept server: public Shopify product data only; no credentials or cart proxy."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
import json, os
from urllib.error import URLError
os.chdir(os.path.dirname(os.path.abspath(__file__)))
HANDLES=['swan-charm','pink-ballet-slippers-charm','necklace-base','custom-style-bundle-1']
def get_product(handle):
    try:
        req=Request('https://lesmissnyc.com/products/'+handle+'.js',headers={'User-Agent':'Mozilla/5.0','Accept':'application/json'})
        with urlopen(req,timeout=8) as response:
            p=json.load(response)
        return {k:p.get(k) for k in ('handle','title','price','price_varies','compare_at_price','available','featured_image')}
    except (URLError,TimeoutError,ValueError, OSError): return None
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split('?')[0]=='/api/products':
            with ThreadPoolExecutor(max_workers=4) as pool: products=[p for p in pool.map(get_product,HANDLES) if p]
            body=json.dumps(products).encode();self.send_response(200 if products else 503);self.send_header('Content-Type','application/json; charset=utf-8');self.send_header('Cache-Control','public, max-age=60');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
        else: super().do_GET()
if __name__=='__main__': ThreadingHTTPServer(('0.0.0.0',8000),Handler).serve_forever()
