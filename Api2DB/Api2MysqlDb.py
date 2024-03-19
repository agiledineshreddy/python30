import requests

import mysql.connector

product_resp = requests.get('https://dummyjson.com/products')
product_data = product_resp.json()
product_List = product_data['products']

apple_Products=filter(lambda product: product['brand']=="Apple",product_List)

products=[]
for product in apple_Products:
    products.append((product['id'],product['title'],product['brand'],product['category'],product['price']))


db_con=None
my_cursor=None
try:
    db_con=mysql.connector.connect(host="localhost",user="root",password="root",database="8am")
    my_cursor=db_con.cursor()
    sql_st=''' insert into product(id,name,brand,category,price) values(%s,%s,%s,%s,%s);'''
     
    my_cursor.executemany(sql_st,products)
    db_con.commit()

except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    my_cursor.close()
    db_con.close()