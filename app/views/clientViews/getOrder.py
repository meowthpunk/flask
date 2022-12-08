from app import app
# from test import test
# from app.methods import createDish as createDishMethod
# from app.methods import editDish as editDishMethod
# from app.methods import createCategory as createCategoryMethod
# from app.methods import editCategory as editCategoryMethod
# from app.methods import checkAPIkey
from app.methods import getOrder as getOrderMethod
# import json
# import time

from flask import request

@app.route('/getOrder/<id>', methods=['GET'])
def getOrder(id):
    secret_key = request.args.get('secret_key')

    if (secret_key):
        order = getOrderMethod(id, secret_key)

        if(order != "error_secret_key"):
            return {"ok": True, "dump": order}
        return {
            "ok": True,
            "dump": {
                "error": "NOT_VALID_SECRET_KEY"
                }
            }



    return {"ok": True, "dump": {"error": "NOT_EXISTED_SECRET_KEY"}}
