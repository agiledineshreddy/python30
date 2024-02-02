class Test:
    def __init__(self):
        print("constructor method - special method")

    def m1(self):
        print('instance method - m1')

    def m2(self):
        print('instance method - m2')

t1=Test()
t2=Test()

t1.m1()
t1.m2()

t2.m1()
t2.m2()