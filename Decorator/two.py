# Decorator
'''
What is Decorator?
Decorator is function, it take function as agrument, and return modified function.
'''


def login_req(func):
    def inner(name, flag):
        if flag != True:
            print("Login Required! Please Login")
        else:
            return func(name, flag)

    return inner


def home_page(name, flag):
    print("Welcome to Home Page")


@login_req
def order_page(name, flag):
    print("Order Page")


@login_req
def profile_page(name, flag):
    print("profile Page")


def product_page(name, flag):
    print("Product Page")


home_page("Rahul", True)
product_page("Rahul", True)
# for accessing profile page and order page - login required
profile_page("Rahul", True)
order_page("Rahul", True)
