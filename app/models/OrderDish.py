from app import db

# order_dish = db.Table('order_dish',
#     db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
#     db.Column('dish_id', db.Integer, db.ForeignKey('dish.id')),
#     db.Column('counter', db.Integer)
# )

class OrderDish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))
    counter = db.Column(db.Integer)


    def __init__(self, order_id, dish_id, counter):
        self.order_id = order_id
        self.dish_id = dish_id
        self.counter = counter

        # db.session.add(self)
        # db.session.commit()

    # def addDish(self, dish_id):
    #     dish = db.session.query(Dish.Dish).filter(Dish.Dish.id == dish_id).first()
    #     self.dishes.append(dish)
