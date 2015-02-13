from flask import Flask
import os

app = Flask(__name__)

port = int(os.getenv("VCAP_APP_PORT") or 5000)

@app.route("/")
def hello():
    return ("Hello, world. I'm in Flask, running on port %i." % port)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
