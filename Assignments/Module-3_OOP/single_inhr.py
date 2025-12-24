class father:
    car:int
    bal:int
    
    def getdata(self):
        self.car=input("Enter car details:")
        self.bal=input("Enter bank balance details:")
    
class son(father):
    def printdata(self):
        print("Car:",self.car)
        print("Bank Balance:",self.bal)


sn=son()
sn.getdata()
sn.printdata()
