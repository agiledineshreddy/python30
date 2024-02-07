class Test:
    a = 100   #static variable
    def __init__(self):
        self.b=200

    def m1(self):
        self.c=300
    
    @classmethod
    def m2(cls):
        pass

    @staticmethod
    def m3():
        pass 


t1=Test()
t1.m1()
t1.d = 400
print(t1.__dict__)
print(Test.__dict__)

