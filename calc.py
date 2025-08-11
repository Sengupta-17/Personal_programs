class Calculator:
    def __init__(self):
        self.a=0
        self.b=0
        self.menu()

    def menu(self):
        c=int(input("""Enter your choice for your desired opertion:
                 1) Enter 1 for addition
                 2) Enter 2 for subtraction
                 3) Enter 3 for multiplication
                 4) Enter 4 for division
                 5) Enter 5 to exit
              """))
        if c==1:
            self.addition()
        elif c==2:
            self.subtraction()
        elif self.c==3:
            self.multiply()
        elif self.c==4:
            self.divide()
        else:
            print("Invalid Input!!")
            self.menu()

    def addition(self):
        self.a=int(input("Enter value of 1st number"))
        self.b=int(input("Enter value of 2nd number"))
        print(self.a,"+",self.b,"=",self.a+self.b)
        self.menu()

    def subtraction(self):
        self.a=int(input("Enter value of 1st number"))
        self.b=int(input("Enter value of 2nd number"))
        print(self.a,"-",self.b,"=",self.a-self.b)
        self.menu()

    def multiply(self):
        self.a=int(input("Enter value of 1st number"))
        self.b=int(input("Enter value of 2nd number"))
        print(self.a,"*",self.b,"=",self.a*self.b)
        self.menu()

    def divide(self):
        self.a=int(input("Enter value of 1st number"))
        self.b=int(input("Enter value of 2nd number"))
        print(self.a,"/",self.b,"=",self.a/self.b)
        self.menu()
