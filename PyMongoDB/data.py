import requests
user_response = requests.get('https://jsonplaceholder.typicode.com/users')
user_List = user_response.json()

# trasnfermation
new_users = []
for user in user_List:
    new_users.append((user['id'], user['name'], user['email']))

print(new_users)

sql_st = ''' insert into user(id,name,email) values(%s,%s,%s) '''
