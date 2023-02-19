from flask import Flask
from phishingkiller import start_process, getLatestValue
import threading
app = Flask(__name__)

@app.route('/')
def home():    
    return 'Hello, world! /strat to start and /state for state'

@app.route('/start')
def start():
    t = threading.Thread(name='start_process', target=start_process, args=(print,))
    t.setDaemon(True)
    t.start()
    return 'Starting...'

@app.route('/state')
def state():
    return getLatestValue()

#from http.server import BaseHTTPRequestHandler
#from phishingkiller import start_process, getLatestValue
#import threading
#class handler(BaseHTTPRequestHandler):
#    def do_GET(self):
#        path = self.path.split("?",1)[0]
#        if path == '/state':
#            self.send_response(200)
#            self.send_header('Content-type','text/plain')
#            self.end_headers()
#            self.wfile.write(getLatestValue().encode('utf-8'))
#        elif path == '/start':
#            self.send_response(200)
#            self.send_header('Content-type','text/plain')
#            self.end_headers()
#            self.wfile.write('Starting...'.encode('utf-8'))
#            t = threading.Thread(name='start_process', target=start_process, args=(self.wfile.write,))
#            t.setDaemon(True)
#            t.start()
#        else:
#            self.send_response(200)
#            self.send_header('Content-type','text/plain')
#            self.end_headers()
#            self.wfile.write('Hello, world! /strat to start /state for state '.encode('utf-8'))
#        return
