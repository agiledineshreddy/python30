class Bank:
    bank_name = "Kotak Mahindra"

    def __init__(self, name,code):
        self.branch_name=name 
        self.branch_code=code 
    


b1=Bank('Marathahallli',345)
print(b1.__dict__)
print("*******************")
print(Bank.__dict__)