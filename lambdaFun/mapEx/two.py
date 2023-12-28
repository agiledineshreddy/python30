prices = [98, 198, 298, 398]


def addone(price):
    return price+1


# map(funciton,sequence)
obj = map(addone, prices)
newprices = list(obj)
print(newprices)
