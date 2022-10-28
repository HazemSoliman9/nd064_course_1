import http
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/status")
def status():
    http.status_code = 200
    return {
        "result": "OK - healthy"
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0')
