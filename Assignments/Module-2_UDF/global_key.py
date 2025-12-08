x=34
print("X:",x)

def getVal():
    global x
    x+=10
    print("X:",x)
    
getVal()