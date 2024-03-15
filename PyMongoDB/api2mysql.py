import requests
import mysql.connector
user_response = requests.get('https://jsonplaceholder.typicode.com/users')
user_List = user_response.json()

new_users = []
for user in user_List:
    new_users.append((user['id'], user['name'], user['email']))


sql_st = ''' insert into user(id,name,email) values(%s,%s,%s) '''

dbcon = None
mycur = None


try:
    dbcon = mysql.connector.connect(
        host='localhost', user='root', password='root', database='8am')
    mycur = dbcon.cursor()
    mycur.executemany(sql_st, new_users)
    dbcon.commit()
except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    mycur.close()
    dbcon.close()
