class Account:
    ''' Account class created by Narasimha - purpose is learning variables '''


    min_bal=500
    brach_name='Banalore'
    def __init__(self,id,name,amount):
        self.acc_id =id 
        self.acc_name=name 
        self.acc_bal = amount 

    def open_account(self):
        print('account opened success fully')
    def deposit_amount(self,amount):
        self.acc_bal  = self.acc_bal + amount
    
    def get_bal(self):
        return self.acc_bal

a1=Account(101,'Venkat',5001)

print(a1.__dict__)
print(a1.get_bal())
a1.open_account()
a1.deposit_amount(100)

print(a1.__dict__)

print(a1.get_bal())