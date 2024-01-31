class Emp:
    ''' Employee class is used to maintain employee records, created by Narasimha 31/Java/2024 '''

    eid = 101
    ename = 'Rahul'

    def get_details(self):
        print("Emplyee Detrails")

    def get_loc(self):
        print("Employee Loc - Bangalore")


# print all class members
# print(Emp.__dict__)

# print class - document string
print(Emp.__doc__)


# How to access class members
e1 = Emp()
print(e1)
print(id(e1))
print(type(e1))
