from flask import Flask, render_template, request
from flask_restful import Resource, Api
from datetime import datetime
import socket, os



app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/salvador")

def salvador():
    dt = str(datetime.now())
    ip = request.remote_addr
    return "Hello {}! Ip {} Datetime {} Local interface".format(ip, dt)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

