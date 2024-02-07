class Account:
    min_bal = 500
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name 
        self.acc_bal = amount
    def open_acc(self):
        print("Account Opened Successfully")
    def deposit_amount(self,amount):
        self.acc_bal = self.acc_bal + amount 
    def withdrawl_amout(self):
        pass 
    def get_bal(self):
        return self.acc_bal - Account.min_bal

    @classmethod 
    def update_min_bal(cls):
        cls.min_bal = 600 

    @staticmethod
    def cal_interest():
        return 9 
    

a1=Account(101,'Rahul',5000)
a2=Account(102,'Sonia',6000)
a3=Account(103,'Priyanka',7000)

a1.deposit_amount(500)
a1.deposit_amount(100)

print(a1.get_bal())