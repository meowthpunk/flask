from app import app
from app.methods import createOrder as createOrderMethod
from app.console.console_logs import ConsoleLogs, serverDecorator


from flask import request

# @serverDecorator("GET_MENU")
@app.route('/createOrder', methods=['POST'])
def createOrder():
    data = request.json
    responce = createOrderMethod(data["dump"])
    responce["order_pay_url"] = 'https://www.tinkoff.ru/'
    print(responce)

    return {"ok": True, "dump": responce}
