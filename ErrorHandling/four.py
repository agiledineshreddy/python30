# how to create custom/user defined errors
class InsuffientFundsError(Exception):
    def __init__(self, arg):
        self.msg = arg


amount = int(input("Enter Amount::::"))

if amount > 5000:
    raise InsuffientFundsError("Less Account Balance")
else:
    print("Transaction Success!")
