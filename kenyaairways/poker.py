class Olk:

    def __init__(self,amount):
        self.amount = amount

        print("You have:" , amount)

    def add_cash(self,addition):
        self.addition = addition
        self.new_amnt =  self.amount + addition

        print(("Your new balance is", self.new_amnt))

    
    def sub_cash(self,sub):
        self.sub = sub
        self.balance = self.amount - self.sub

        print("Your new balance is:" , self.balance)

    


class Loan(Olk):

    def __init__(self,loan):
        self.loan = loan
        
        super().__init__(amount)

        if amount >= 1000:
            print("You are eligible for a loan")
        else:
            print("You are not eligible for a loan")


ins_1 = Olk(100000)

ins_1

ins_1.add_cash(50000)

ins_1.sub_cash(2000)

ins_2 = Loan(50000,9000)





        