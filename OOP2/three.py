class GrandParent:
    def m1(self):
        print("Grand Parent class - m1 method")

class Parent(GrandParent):
    def m2(self):
        print("Parent class - m2 method")

class Child(Parent):
    def m3(self):
        print("Child class - m3 method")


obj=Child()
obj.m1()
obj.m2()
obj.m3()