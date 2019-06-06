from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')