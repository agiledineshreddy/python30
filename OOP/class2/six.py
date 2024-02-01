class Account:

   

    def deposit_amount(self,amount):
        #print("Amount deposited successfully", amount)
        self.acc_bal = amount
   
   

a1=Account()

a1.deposit_amount(5000)
print(a1.__dict__)
a2=Account()
a2.deposit_amount(45000)
print(a2.__dict__)