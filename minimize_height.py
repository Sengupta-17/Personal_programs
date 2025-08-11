class Minimize:
    def __init__(self):
        self.n=0
        self.k=0
        self.arr=[]
        self.take_input()

    def take_input(self):
        self.n=int(input("Enter the size of the array:"))
        for i in range(0,self.n):
            x=int(input("Enter the height of the tower:"))
            self.arr.append(x)
        self.k=int(input("Enter value of k:"))
        self.modify()

    def modify(self):
        self.arr.sort()
        maxl=max(self.arr)
        minl=min(self.arr)
        for i in range(0,self.n):
            if i==self.n-1:
                self.arr[i]-=self.k
                break
            if i==0:
                self.arr[i]+=self.k
            elif self.arr[i]-self.k<minl:
                self.arr[i]+=self.k
            elif self.arr[i]+self.k>maxl:
                self.arr[i]-=self.k
            elif self.arr[i]+self.k<maxl:
                if self.arr[i+1]-self.k<self.arr[i]+self.k:
                    self.arr[i]-=self.k
            else:
                self.arr[i]-=self.k
        self.display()
    def display(self):
        maxl=max(self.arr)
        minl=min(self.arr)
        min_diff=maxl-minl
        print("Minimum difference after modifying heights of towers=",min_diff)