from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def root():
    return "OK: multi-service up"

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000)
