from urllib import response
from flask import Flask
from flask import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
    )
# @app.route("/metrics")
# def metrics():
#     return {
#         "data": {
#             "UserCount": 140,
#             "UserCountActive": 23
#         }
#     }
if __name__ == "__main__":
    app.run(host='0.0.0.0')
