from http.server import BaseHTTPRequestHandler
from phisingkiller import start_proces
import threading
    
from flask import Flask
from phisingkiller import start_proces
import threading
app = Flask(__name__)

@app.route('/')
def home():    
    t = threading.Thread(name='start_proces', target=start_proces)
    t.setDaemon(True)
    t.start()
     return 'Process running'
