import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

# get data from api 

data = response.json()
print(data)