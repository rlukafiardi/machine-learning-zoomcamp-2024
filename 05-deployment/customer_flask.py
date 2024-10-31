import requests

url = 'http://localhost:1313/predict'

customer = {
    "job": "student",
    "duration": 280,
    "poutcome": "failure"
}

response = requests.post(url, json=customer).json()
print("subscription probability:", response)
      



