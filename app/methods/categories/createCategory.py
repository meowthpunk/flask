from app.models.Category import Category
from app import db
from app.methods.restaurants import isExistedRestaurant
# Dish = models.Dish.Dish
# Category = models.Category.Category
# Ingredient = models.Ingredient.Ingredient

def createCategory(category):
    errors = {}
    category_info = category

    if "title" not in category:
        errors["title"] = "NOT_EXISTED"

    if "restaurant_id" not in category:
        errors["restaurant_id"] = "NOT_EXISTED"
    else:
        if isExistedRestaurant(category["restaurant_id"]) == False:
            errors["restaurant_id"] = "NOT_EXISTED_RESTAURANT_ID"

    if errors == {}:
        category = Category.create(category)

        try:
            category_info = category.getInfo()

            # if logo_flag:
            #     path = fileSave(logo, 'restaurant', f'{restaurant.id}.png')
            #     restaurant.setLogo(path)

        except:
            errors["main"] = category["error"]
            category_info = category["category"]

    # try:
    #     category_title = category["category_title"]
    # except:
    #     return {"error": "add-dish: category_title not exists"}



    # if category == None:
    #     return {"error": "add-dish: Category not found. Create category and try again."}

    return {"category": category_info, "errors": errors}
