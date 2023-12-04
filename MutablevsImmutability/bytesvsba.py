l=[10,20,30,40]
b=bytes(l)
ba=bytearray(l)
print(type(l))
print(type(b))
print(type(ba))
#b[0]=101
ba[0] = 101

for value in ba:
    print(value)