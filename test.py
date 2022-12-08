import requests
# print(10)
r = requests.get("http://flask-production-5c88.up.railway.app/getRestaurants")
print(r.json())
