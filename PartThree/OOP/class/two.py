class Test:
    ''' Test class created by Narasimha for Task No:44343 '''

    a = 100

    def m1(self):
        pass

    def m2(self):
        pass


print(Test.__doc__)

t1 = Test()  # t1 is ref variable or object.
print(t1)
print(id(t1))
print(type(t1))
print(Test.__dict__)
print(t1.a)
