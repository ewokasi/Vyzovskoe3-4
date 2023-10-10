import requests

response = requests.post("http://localhost:3000/json")
print(response.json)