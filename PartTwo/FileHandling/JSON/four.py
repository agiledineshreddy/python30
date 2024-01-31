# read json file, and print all user names
import json

filename = 'user.json'
fp = open(filename, 'r')

users = json.load(fp)
print(type(users))
for user in users:
    print(user['name'])
