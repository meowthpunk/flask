from app import app
# from test import test
# from app.methods import createDish as createDishMethod
# from app.methods import editDish as editDishMethod
# from app.methods import createCategory as createCategoryMethod
# from app.methods import editCategory as editCategoryMethod
# from app.methods import checkAPIkey
# from app.methods import getMenu as getMenuMethod
# from app.methods import getBanners as getBannersMethod
# import json
# import time
from app.methods import getUTCTime as getUTCTimeMethod

from flask import request

@app.route('/getUTCTime', methods=['GET'])
def getUTCTime():
    now_utc_time = getUTCTimeMethod()
    return {"ok": True, "dump": now_utc_time}
