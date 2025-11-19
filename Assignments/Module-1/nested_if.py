a=int(input("Enter A:"))
b=int(input("Enter B:"))

if a!=0 and b!=0: #root - parent
    if a>b: #child
        print("Sum:",a+b)
    else:
        print("Sub:",a-b)
else:
    print("Error!")