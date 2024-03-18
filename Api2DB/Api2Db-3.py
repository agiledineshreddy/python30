import requests
import pymongo
import mysql.connector

product_resp = requests.get('https://dummyjson.com/products')
product_data = product_resp.json()
product_List = product_data['products']

# print only samsumg products
skincare_products = []

for product in product_List:
    if product['category'] == 'skincare':
        print(product['title'])
