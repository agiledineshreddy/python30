import requests

user_response = requests.get('https://jsonplaceholder.typicode.com/users')
print(user_response)
print(type(user_response))
user_List = user_response.json()
print(user_List)
print(type(user_List))
