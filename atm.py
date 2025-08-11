class Atm:

    __counter=1
    def __init__(self):
        self.__bal=0
        self.__pin=""
        self.__invalid=0
        print("Account ID:",id(self))
        self.sno=Atm.__counter
        Atm.__counter=Atm.__counter+1
        self.__menu()

    def __menu(self):
        user_input=input("""
                         Hello, How would you like to proceed?
                         1. Enter 1 to create ATM pin
                         2. Enter 2 to deposit cash
                         3. Enter 3 to withdraw cash
                         4. Enter 4 to check balance
                         5. Enter 5 to exit
                         """)
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.check_bal()
        else:
            print("Thank you. Have a nice day!")

    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if(type(new)==int):
            Atm.__counter=new
        else:
            print("Invalid input, counter can only be integer type!")
    
    def get_pin(self):
        return self.__pin

    def set_pin(self,new_pin):
        if type(new_pin==int):
            self.__pin=new_pin
            print("Pin set succesfully")
        else:
            print("Invalid input type! Not allowed.")
    
    def create_pin(self):
        self.__pin=input("Create a 6-digit pin:")
        conf=input("Re enter your set pin:")
        if self.__pin==conf:
            print("Pin set succesfully")
        else:
            print("Pin doesn't match. Try again!")
            self.__menu()

    def deposit(self):
        temp=input("Enter your pin:")
        if temp==self.__pin:
            self.__invalid=0
            amount=int(input("Enter amount to be deposited:"))
            self.__bal=self.__bal+amount 
            print("Money deposit successfull!")
        else:
            print("Invalid Pin! Try again!")
            self.__invalid+=1
        if self.__invalid==3:
            print("3 INCORRECT PINS INPUT. CARD BLOCKED FOR THE NEXT 24 HOURS!")
        else:
            self.__menu()
    
    def withdraw(self):
        temp=input("Enter your pin:")
        if temp==self.__pin:
            self.__invalid=0
            amount=input("Enter amount you wish to withdraw:")
            if amount>self.__bal:
                print("Insuffient funds!")
            else: 
                self.__bal=self.__bal-amount 
                print("Money withdraw successfull!")
        else:
            print("Invald pin! Try again!")
            self.__invalid+=1
        if self.__invalid==3:
            print("3 INCORRECT PINS INPUT. CARD BLOCKED FOR THE NEXT 24 HOURS!")
        else:
            self.__menu()
    
    def check_bal(self):
        temp=input("Enter your pin:")
        if temp==self.__pin:
            self.__invalid=0
            print("Balance of Account=",self.__bal)
        else:
            print("Invald pin! Try again!")
            self.__invalid+=1
        if self.__invalid==3:
            print("3 INCORRECT PINS INPUT. CARD BLOCKED FOR THE NEXT 24 HOURS!")
        else:
            self.__menu()