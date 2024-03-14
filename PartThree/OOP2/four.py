#heirarchical inheritance
class Parent:
    def m1(self):
        print("Parent Class - m1 method") 


class Child1(Parent):
    def m2(self):
        print("Child1 - class : m2 method")

class Child2(Parent):
    def m3(self):
        print("Child2 - class : m3 method")

obj1=Child1()
obj1.m1()
obj1.m2()
#obj1.m3()

obj2=Child2()
obj2.m1()
obj2.m3()