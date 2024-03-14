class Parent1:
    def m1(self):
        print("Parent1 - m1 method")

    def m2(self):
        print("Parent1 - m2 method")


class Parent2:
    def m3(self):
        print("Parent2 - m3 method")

    def m2(self):
        print("Parent2 - m2 method")


class Child(Parent2, Parent1):
    def m4(self):
        print("Child - m4 method")


obj = Child()
obj.m2()
""" obj.m1()
# obj.m2()
obj.m3()
obj.m4() """
