import pymongo

client = pymongo.MongoClient()
db = client['8am']
user_col = db['user']

user_list = user_col.find({})

# print(type(user_list))


for user in user_list:
    print(user)
