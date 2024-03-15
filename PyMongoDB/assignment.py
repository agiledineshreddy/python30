import requests
import mysql.connector
# user_response = requests.get('https://jsonplaceholder.typicode.com/users')
# user_List = user_response.json()
dbcon = None
mycur = None
try:
    dbcon = mysql.connector.connect(
        host='localhost', user='root', password='root', database='8am')
    mycur = dbcon.cursor()
except mysql.connector.DatabaseError as err:
    if err:
        print(err)
