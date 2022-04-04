import requests

BASE_URL = "http://127.0.0.1:5000/"
PUT_API_PATH = "/video/1"
GET_API_PATH = "/video/1"
DELETE_API_PATH = "/video/1"

# PUT request
response = requests.put(BASE_URL + PUT_API_PATH, {"likes": 10, "name": "my video", "views": 1000})
print(f'{response.request=} {response.url=} {response.status_code=} {response.reason=}')
print(f'{response.json()=}')

input()

# GET request
response = requests.get(BASE_URL + GET_API_PATH)
print(f'{response.request=} {response.url=} {response.status_code=} {response.reason=}')
print(f'{response.json()=}')
#print(response.json().get('KEY_NAME'))

input()

# DELETE request
response = requests.delete(BASE_URL + DELETE_API_PATH)
print(f'{response.request=} {response.url=} {response.status_code=} {response.reason=}')
print(f'{response}')

input()

response = requests.get(BASE_URL + GET_API_PATH)
print(f'{response.request=} {response.url=} {response.status_code=} {response.reason=}')
print(f'{response.json()=}')
