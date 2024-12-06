import requests

url = "http://127.0.0.1:8000/greet"
data = {'name': 'Routify'}
response = requests.get(url)
print(response.text)
