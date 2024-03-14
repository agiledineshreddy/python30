class Account:
    acc_Bal = 50000

    def open_acc(self):
        print('Account Opened Successfully')

    def deposit(self):
        print('Amount Deposited Successfully')

    def withdrawl(self):
        print('Insufficient Bal')

    def get_bal(self):
        print(self.acc_Bal)


a1 = Account()
# how to access class members - using object/ref vairable
print(a1.acc_Bal)

a1.open_acc()
a1.deposit()
a1.withdrawl()
a1.get_bal()
