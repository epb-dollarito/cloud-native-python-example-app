import os

from flask import Flask
from flask import Response


app = Flask(__name__)


ENVIRONMENTAL = os.getenv('ENVIRONMENTAL')


@app.route('/')
def index():
    return f"This is the amazing app EVER, speaking at wdi {ENVIRONMENTAL} and have github integration."
 

@app.route("/healthz")
def healthz():
    resp = Response("ok")
    resp.headers['Custom-Header'] = 'Awesome'
    # this is awesome tying things
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
