from app import app
from app import db
from app.models.Restaurant import Restaurant
# from app.models.Category import Category
# from app.models.Dish import Dish
# from test import test
from app.methods import createDish as createDishMethod
from app.methods import editDish as editDishMethod
from app.methods import createCategory as createCategoryMethod
from app.methods import editCategory as editCategoryMethod
from app.methods import checkAPIkey
from app.methods import getMenu as getMenuMethod
import json
import time

from flask import request

# @app.route('/getMenu', methods=['GET'])
# def getMenu():
#     # print(getMenuMethod())
#     # time.sleep(5)
#
#     verification = checkAPIkey(request.args.get("API_KEY"))
#
#     if verification["ok"] == False:
#         return {"ok": True, "error": verification["error"]}
#
#
#     return {"ok": True, "menu": getMenuMethod()}

@app.route('/dashboard/getRestaurants', methods=['GET'])
def getDashboardRestaurants():
    data = request.json

    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}


    restaurants  = db.session.query(Restaurant).all()

    dump = []

    for restaurant in restaurants:
        dump.append(restaurant.getInfo())



    return {"ok": True, "restaurants": dump}

@app.route('/dashboard/getMenu/<restaurant_id>', methods=['GET'])
def getDashboardMenu(restaurant_id):

    # time.sleep(5)


    data = request.json

    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}


    restaurant  = db.session.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

    menu = {
        "dishes": [],
        "categories": [],
    }

    for category in restaurant.categories:
        menu["categories"].append(category.getInfo())
        for dish in category.dishes:
            menu["dishes"].append(dish.getInfo())



    return {"ok": True, "menu": menu}
