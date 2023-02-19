#from flask import Flask
#from phishingkiller import start_proces
#import threading
#app = Flask(__name__)

#@app.route('/')
#def home():    
#    t = threading.Thread(name='start_proces', target=start_proces)
#    t.setDaemon(True)
#    t.start()
#    return 'Process running'


from http.server import BaseHTTPRequestHandler
from phishingkiller import start_process
import threading
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        t = threading.Thread(name='start_process', target=start_process, args=(self.wfile.write,))
        t.setDaemon(True)
        t.start()
        return
