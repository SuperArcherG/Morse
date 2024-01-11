import socket
import os
from PIL import Image
from waitress import serve
from werkzeug.utils import secure_filename
from flask import Flask, flash, json, send_file, request, redirect, url_for
from contextlib import nullcontext
import requests


def get_local_ip():
    try:
        # Create a socket connection to an external server (doesn't actually connect)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Use a known external server (Google's public DNS server)
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        print("ERROR")
        return None

# Get and print the local IP address
local_ip = get_local_ip()

if local_ip:
    print(f"Local IP address: {local_ip}")
else:
    print("Failed to retrieve the local IP address.")


Prod = False
Port = 48763
DevPort = 48763
Ip = str(local_ip)
DevIP = str(local_ip)


app = Flask(__name__)

@app.route("/")
def root():
    # Detect all .txt files in the current working directory and list their names in an array
    txt_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.txt') and not f.startswith('r')]
    if not txt_files:
        return "NULL"
    txt_files = sorted(txt_files, key=lambda x: float(x.rsplit('.', 2)[0]))
    txt_files.reverse()
    name = txt_files.pop()
    print(name)
    file = open(os.getcwd()+"/"+name,"r").read()
    os.remove(os.getcwd()+"/"+name)
    return file


if __name__ == "__main__":
    if Prod:
        serve(app, host=Ip, port=Port)
    else:
        app.run(host=DevIP, port=DevPort, debug=True)
