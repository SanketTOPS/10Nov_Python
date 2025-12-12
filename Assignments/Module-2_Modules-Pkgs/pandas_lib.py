import pandas

stdata={
    "ID":[1,2,3,4,5],
    "NAME":["Sanket","Nirav","Ashok","Mitesh","Darshan"],
    "SUBJECT":["Python","PHP","JAVA","HTML","CSS"]
}

x=pandas.DataFrame(stdata)
print(x)