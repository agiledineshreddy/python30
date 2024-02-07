#Hybrid Inheritance

class GP:
    def m1(self):
        print("GP class- m1 method") 

class Parent1(GP):
    def m2(self):
        print("Parent1 class - m2 method") 

class Parent2(GP):
    def m3(self):
        print("Parent2 class - m3 method") 


class Child(Parent1,Parent2):
    def m4(self):
        print("Child Class - m4 method")


obj=Child()
obj.m1()  
obj.m2()
obj.m3()
obj.m4()