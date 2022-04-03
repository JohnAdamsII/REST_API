import requests

BASE_URL = "http://127.0.0.1:5000/"
GET_API_PATH = "/api/Henry"

# GET request
response = requests.get(BASE_URL + GET_API_PATH)
print(f'{response.request=} {response.url=} {response.status_code=} {response.reason=}')
print(f'{response.json()=}')
print(response.json().get('gender'))


# POST request
# response = requests.post(BASE_URL + API_PATH)
# print(str(response.request)+' '+response.url+' '+str(response.status_code))
# print(response.json())
