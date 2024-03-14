class Account:
    '''  Account class created by Narasimha - for Testing purpose '''

    min_bal = 500

    def open_account(self):
        pass

   
a1=Account()
a2=Account()
a3=Account()

#print objects
print(a1)
print(a2)
print(a3)

#print address
print(id(a1))
print(id(a2))
print(id(a3))

#print object members
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)

#print class members

print(Account.__dict__)