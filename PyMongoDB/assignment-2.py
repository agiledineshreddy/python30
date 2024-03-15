import requests
import pymongo
user_response = requests.get('https://jsonplaceholder.typicode.com/users')
user_List = user_response.json()

client = pymongo.MongoClient()
db = client['8am']
emp_col = db['emp']

emp_col.insert_many(user_List)
