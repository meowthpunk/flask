from app import app
# from test import test
# from app.methods import createDish as createDishMethod
# from app.methods import editDish as editDishMethod
# from app.methods import createCategory as createCategoryMethod
# from app.methods import editCategory as editCategoryMethod
# from app.methods import checkAPIkey
from app.methods import getRestaurants as getRestaurantsMethod
# from app.methods import getBanners as getBannersMethod
# import json
# import time

from flask import request

@app.route('/getRestaurants', methods=['GET'])
def getRestaurants():
    dump_object = getRestaurantsMethod()
    # banners = getBannersMethod(restaurant_link)
    print(dump_object)
    return {"ok": True, "dump": dump_object}
    # time.sleep(5)

# @app.route('/getBanners/')

    # verification = checkAPIkey(request.args.get("API_KEY"))
    #
    # if verification["ok"] == False:
    #     return {"ok": True, "error": verification["error"]}
    #
    #
