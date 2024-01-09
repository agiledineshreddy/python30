

def home_page(name, flag):
    print("Welcome to Home Page")


def order_page(name, flag):
    print("Order Page")


def profile_page(name, flag):
    print("profile Page")


def product_page(name, flag):
    print("Product Page")


home_page("Rahul", True)
product_page("Rahul", True)
# for accessing profile page and order page - login required
profile_page("Rahul", False)
order_page("Rahul", False)
