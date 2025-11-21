"""for i in range(5,0,-1):
    for j in range(i):
        print("* ",end=" ")
    print("")"""
    
    
for i in range(1,6):
    print(*range(1,i+1))