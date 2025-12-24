class sanket:
    sid:int
    ssub:str
    
    def s_getdata(self):
        self.sid=input("Enter Sanket's ID:")
        self.ssub=input("Enter Sanket's Subject:")
        
class ashok:
    aid:int
    asub:str
    
    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class gopal:
    gid:int
    gsub:str
    
    def g_getdata(self):
        self.gid=input("Enter Gopal's ID:")
        self.gsub=input("Enter Gopal's Subject:")


class tops(sanket,ashok,gopal):
    def printdata(self):
        print("--------Sanket's Data--------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Subject:",self.ssub)
        print("--------Ashok's Data--------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("--------Gopal's Data--------")
        print("Gopal's ID:",self.gid)
        print("Gopal's Subject:",self.gsub)
    
tp=tops()
tp.s_getdata()
tp.a_getdata()
tp.g_getdata()
tp.printdata()
