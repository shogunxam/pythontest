from http.server import BaseHTTPRequestHandler
from phisingkiller import start_proces
import threading
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        t = threading.Thread(name='start_proces', target=start_proces)
        t.setDaemon(True)
        t.start()
        return
