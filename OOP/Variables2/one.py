class Test:

    def __init__(self):
        pass

    def m1(self):
        pass
    
    @classmethod
    def m2(cls):
        pass

    @staticmethod
    def m3():
        pass 


t1=Test()
print(t1.__dict__)
print(Test.__dict__)