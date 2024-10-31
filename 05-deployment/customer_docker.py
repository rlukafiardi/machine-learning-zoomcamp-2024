import requests

url = 'http://localhost:1313/predict'

customer = {
    "job": "management",
    "duration": 400,
    "poutcome": "success"
}

response = requests.post(url, json=customer).json()
print("subscription probability:", response)
      



