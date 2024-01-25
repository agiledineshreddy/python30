# read json file, print all male users
import json
filename = 'user.json'
fp = open(filename, 'r')

users = json.load(fp)
print(type(users))

for user in users:
    if user['gender'] == "Male":
        print(user['name'], user['id'], user['gender'])


""" for user in list(filter(lambda user: user['gender'] == 'Male', users)):
    print(user['name'], ":", user['id']) """
