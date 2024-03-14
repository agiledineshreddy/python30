class Test:
    a=10          #static var

    def __init__(self):
        self.b=200     #instance var 
    def m1(self):
        self.c=300     #instance var 

t1=Test()
t1.d=400         #instance var
print(t1.__dict__)

t1.m1()
print(t1.__dict__)
