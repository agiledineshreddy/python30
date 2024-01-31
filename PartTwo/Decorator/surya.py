#how to access inner function outside

def outer():
    print('Outer Funciton')
    def inner():
        print("inner")

    return inner

surya=outer()
surya()
surya()
surya()
surya()