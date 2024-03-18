import requests
import pymongo
import mysql.connector

product_resp = requests.get('https://dummyjson.com/products')
product_data = product_resp.json()
product_List = product_data['products']

# print only samsumg products
laptop_products = filter(
    lambda product: product['category'] == 'laptops', product_List)

client = pymongo.MongoClient()
db = client['8am']
product_col = db['product']

product_col.insert_many(laptop_products)
