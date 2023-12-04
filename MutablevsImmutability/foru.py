list=[1,20,40,255]
b = bytes(list)
print(id(b))
print(type(b))
print(b)
b[0] = 10
for value in b:
    print(value)