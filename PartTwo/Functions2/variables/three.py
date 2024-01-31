a=100

def f1():
    global b
    b=200
    print(a)
    print(b)


def f2():
    print(a)
    print(b)

f1()
f2()
print(a)