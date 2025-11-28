stdata={}

n=int(input("Enter number of pairs:"))

for i in range(n):
    key=input("Enter your Key's:")
    value=input("Enter your Value's:")
    stdata[key]=value
    
print(stdata)