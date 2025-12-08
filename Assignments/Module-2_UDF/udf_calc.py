def add(a,b):
    print("Sum:",a+b)

def sub(a,b):
    print("Sum:",a-b)
    
def mul(a,b):
    print("Sum:",a*b)
    
def div(a,b):
    print("Sum:",a/b)
    
no1=int(input("Enter Number1:"))
no2=int(input("Enter Number2:"))

print("Select your choice:")
print("1:Add")
print("2:Sub")
print("3:Mul")
print("4:Div")

choice=int(input("Select any one option:"))
if choice==1:
    add(no1,no2)
elif choice==2:
    sub(no1,no2)
elif choice==3:
    mul(no1,no2)
elif choice==4:
    div(no1,no2)
else:
    print("Error!Invalid choice...")