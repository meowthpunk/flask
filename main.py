from flask import Flask, jsonify
import os
from config import GAVNO

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": f"Welcome to your {GAVNO} app 🚅"})

@app.route('/aaaa/')
def index():
    return jsonify({"Choo Choo": f"Welcome to your {GAVNO} app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
