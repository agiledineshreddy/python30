import requests

import mysql.connector

product_resp = requests.get('https://dummyjson.com/products')
product_data = product_resp.json()
product_List = product_data['products']

db_con=None
my_cursor=None
try:
    db_con=mysql.connector.connect(host="localhost",user="root",password="root",database="8am")
    my_cursor=db_con.cursor()
    sql_st=''' 
            create table product(
            id int,
            name varchar(60),
            brand varchar(32),
            category varchar(32),
            price int
            );

     '''
    my_cursor.execute(sql_st)
    db_con.commit()

except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    my_cursor.close()
    db_con.close()