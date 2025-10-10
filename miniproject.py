# To create the BankAccount class
class bank:
    def __init__(self):
        self.bal =0 #Initialize balanced to 0
        print("Welcome to the SBI")
    def d(self):
        ng=float(input("Enter amount to be Deposited: "))
        self.balance +=ng
    def w(self):
        ng=float(input("Enter amount to be Withdrawn: "))
        if self.bal>=ng:
            self.bal-=ng
            print("\n You Withdrew: ",ng)
        else:
            print("\nInsufficient balance")

      def display(self):
          print("\nNet Available Balance=",self.bal)


 #driver code
s = BankAccount()  #Create an object of BankAccount

s.deposit()       #Deposit money
s.withdraw()      #Withdraw money
s.display()       #display money
          
        
