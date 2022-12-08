from app import db
from . import Order


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.relationship('Address', backref='Customer', uselist=False)
    # address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    orders = db.relationship('Order', backref='Customer')

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

        # db.session.add(self)
        # db.session.commit()


    # def setEmail(self, email):
    #     self.email = email
        # db.session.commit()

    def createOrder(self):
        order = Order.Order(self.id)
        return order.id
