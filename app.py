import os
import socket

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return '<h1><p style="color:' + os.environ.get('COLOR', 'black') + '">Bem Vindo ao Docker Build!</p></h1>'

@app.route('/id')
def hello():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    return '<h1><p style="color:' + os.environ.get('COLOR', 'black') + '">Hostname: ' + hostname + '<br>' + 'IP Address: ' + ip_addr + '</p></h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
