from flask import Flask
import flask

import chat

app = Flask(__name__)


@app.route("/")
def hello_world():
    return flask.redirect("static/chat.html")


@app.route("/api/chat", methods=["POST"])
def api_chat():
    req = flask.request.json
    if not req:
        return flask.abort(400)
    return flask.jsonify({
        "answer": chat.chat(req["history"], req["user"], req["settings"])
    })


@app.route("/api/corelate", methods=["POST"])
def api_corelate():
    req = flask.request.json
    if not req:
        return flask.abort(400)
    return flask.jsonify({
        "corelation": chat.vector(req["a"], req["b"])
    })
