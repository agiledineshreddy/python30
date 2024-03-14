class Account:
    def __init__(self):
        print('Account class - constructor method executing automatically')



a1=Account()
a2=Account()
a3=Account()

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)