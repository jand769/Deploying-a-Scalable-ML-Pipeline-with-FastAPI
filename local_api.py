import requests

# Base URL
url = "http://127.0.0.1:8000"

# TODO: send a GET using the URL
response_get = requests.get(url)

# TODO: print the status code
print(f"GET Status Code: {response_get.status_code}")

# TODO: print the welcome message
print(f"GET Response: {response_get.json()}")

# Input data for POST request
data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
response_post = requests.post(f"{url}/data/", json=data)

# TODO: print the status code
print(f"POST Status Code: {response_post.status_code}")

# TODO: print the result
print(f"POST Response: {response_post.json()}")
