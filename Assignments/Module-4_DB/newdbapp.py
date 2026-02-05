import sqlite3

try:
    db=sqlite3.connect("newdb.db")
    print("Database connected!")
except Exception as e:
    print(e)

#Table Create
tbl_create="create table studinfo(id integer primary key autoincrement,name text,sub text)"
try:
    db.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print(e)


#Insert Data
def insertdata():
    n=int(input("Enter number of students:"))

    for i in range(n):
        name=input("Enter Name:")
        sub=input("Enter Subject:")

        insert_q=f"insert into studinfo(name,sub)values('{name}','{sub}')"
        try:
            db.execute(insert_q)
            db.commit()
            print("Record inserted!")
        except Exception as e:
            print(e)


insertdata()
