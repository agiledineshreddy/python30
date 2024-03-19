import requests

product_resp = requests.get('https://dummyjson.com/products')
product_data = product_resp.json()
product_List = product_data['products']

products=[]
for product in product_List:
    products.append((product['id'],product['title'],product['brand'],product['category'],product['price']))


print(products)