

class MyAtm:
    def __init__(self):
        self.pin=""
        self.__balance=0
        #self.menu()

    def getbalance(self):                    # using this value can get
        return self.__balance

    def setbalance(self,newvalue):           # using this value can change
        if type(newvalue) == int:          #why we add condition here? ..because firstly code check amount isin int. or not if itis in int. then next process continue
          self.__balance = newvalue
        else:
          print("don't break rule")

    def menu(self):
        userinput=input("""
        How can i help you?
        1) Press 1 to create pin
        2) Press 2 to change pin
        3) Press 3 to check balance
        4) press 4 to withdraw
        """)

        if userinput == "1":
           self.createpin()
        elif userinput == "2":
            self.changepin()
        elif userinput == "3":
            self.checkbalance()
        elif userinput == "4":
            self.withdraw()

    def createpin(self):
        userpin=input("Enter your pin")
        self.pin=userpin

        userbalance=int(input("Enter the amount"))
        self.__balance=userbalance

        print("Pin create sucessfully")


    def changepin(self):
        oldpin=input("Enter your pin")
        if self.pin==oldpin:
            newpin=input("Enter new pin")
            self.pin=newpin
            print("New pin set")
        else:
            print("Check your pin again")

    def checkbalance(self):
        userpin=input("Enter your pin")
        if self.pin==userpin:
            print("Total balance is ",self.__balance)
        else:
            print("check pin again")

    def withdraw(self):
        userpin=input("Enter your pin")
        if self.pin==userpin:
            amount=int(input("Enter amount"))
            if amount<=self.__balance:
                self.__balance=self.__balance-amount
                print("here is your cash",amount)
                print("Remaining balance is",self.__balance)
            else:
                print("Not sufficient balance")
        else:
            print("Check pin")

obj=MyAtm()

obj.getbalance()

obj.setbalance("ghapla")
