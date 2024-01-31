def smart_division(func):
    def inner(a, b):
        if b == 0:
            print("Can't Divide by Zero")
        else:
            return func(a, b)
    return inner


@smart_division
def division(a, b):
    return a/b


print(division(10, 5))
print(division(10, 0))
