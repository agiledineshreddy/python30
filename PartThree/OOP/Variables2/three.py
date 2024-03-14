class Test:
    a = 100   #static variable
    def __init__(self):
        self.b=200
        Test.e = 500  #static variable

    def m1(self):
        self.c=300
        Test.f = 600   #static variable
    
    @classmethod
    def m2(cls):
        cls.g=700
        Test.h=800

    @staticmethod
    def m3():
        pass 


t1=Test()
t1.m1()
t1.d = 400
#print(t1.__dict__)
Test.m2()
Test.i=900
print(Test.__dict__)

