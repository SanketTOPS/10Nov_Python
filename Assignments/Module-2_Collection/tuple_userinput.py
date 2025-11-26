data=[]

n=int(input("Enter number of subjects:"))

for i in range(n):
    x=input("Enter Subject Name:")
    data.append(x)
    
print(tuple(data))