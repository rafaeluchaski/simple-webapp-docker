import os
import socket
import netifaces

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return '<h1><p style="color:' + os.environ.get('COLOR', 'black') + '">Bem Vindo ao Docker Build!</p></h1>'

@app.route('/id')
def hello():
    hostname = socket.gethostname()
    ip_addresses = [netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr'] for iface in netifaces.interfaces() if netifaces.AF_INET in netifaces.ifaddresses(iface)]
    return '<h1><p style="color:' + os.environ.get('COLOR', 'black') + '">Hostname: ' + hostname + '<br>' + 'Ip Addresses: ' + ', '.join(ip_addresses) + '</p></h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
