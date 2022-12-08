from app import app
from app import db
from app.models.Restaurant import Restaurant

from app.methods import checkAPIkey as checkAPIkeyMethod

import json
import time
from flask import request



@app.route('/dashboard/checkApiKey', methods=['POST'])
def checkAPIkey():
    time.sleep(1)
    print(1)
    data = request.json
    print(data)

    verification = checkAPIkeyMethod(data["API_KEY"])

    return {"ok": True, "result": verification["ok"]}
