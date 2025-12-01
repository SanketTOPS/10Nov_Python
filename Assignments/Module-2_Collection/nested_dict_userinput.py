stdata={}

n=int(input("Enter number of students:"))

for i in range(n):
    sid=input("Enter Student's ID:")
    sname=input("Enter Student's Name:")
    ssub=input("Enter Student's Subject:")
    stdata[sid]={
        "name":sname,
        "sub":ssub
    }
"""for j in stdata.items():
    print(j)"""
    
print(stdata)