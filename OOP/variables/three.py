class Account:
    ''' Account class created by Narasimha - purpose is learning variables '''


    min_bal=500
    brach_name='Banalore'
    def __init__(self,id,name,amount):
        self.acc_id =id 
        self.acc_name=name 
        self.acc_bal = amount 

    def open_account(self):
        pass
    def deposit_amount(self):
        pass

a1=Account(101,'Venkat',50001)
a2=Account(102,'Vamsi',6001)
a3=Account(103,'Ahmad',70001)

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)