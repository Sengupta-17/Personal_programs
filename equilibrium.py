class Equilibrium:
    def __init__(self):
        self.arr=[]
        self.n=0
        self.ep=0
        self.f=0
        self.take_input()
    
    def take_input(self):
        self.n=int(input("Enter the size of the array:"))
        for i in range(0,self.n):
            x=int(input("Enter a non negative integer:"))
            self.arr.append(x)
        self.find_equilibrium()

    def find_equilibrium(self):
        lsum=0
        rsum=0
        if self.n==1:
            self.ep=1
            print(self.ep)
        else:
            for i in range(0,self.n):
                lsum=0
                rsum=0
                for j in range(0,i):
                    lsum+=self.arr[j]
                for k in range(i+1,self.n):
                    rsum+=self.arr[k]
                if lsum==rsum:
                    self.f=1
                    break
            if self.f==0:
                self.ep=-1
                print(self.ep)
            else:
                self.ep=i+1
                print(self.ep)