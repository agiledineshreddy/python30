class Account:
    def __init__(self,id,name,amount):
        self.acc_id= id 
        self.acc_name=name
        self.acc_bal = amount
        print('Account class - constructor method executing automatically')

    def open_account(self):
        print('Account opened Succuessfullly')
        
    def deposit_amount(self,amount):
        self.acc_bal = self.acc_bal + amount 

    def get_bal(self):
        return self.acc_bal


a1=Account(101,'Venkat',5000)
a2=Account(102,'Dinesh',15000)


print(a1.__dict__)
print(a2.__dict__)

a1.deposit_amount(500)
a1.deposit_amount(50)
a1.deposit_amount(200)

print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())