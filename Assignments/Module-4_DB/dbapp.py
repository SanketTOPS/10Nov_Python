import sqlite3

try:
    db=sqlite3.connect("tops.db")
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
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('hitesh','java'),('ashok','php'),('mahesh','html')"
try:
    db.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

#Update Data
"""update_data="update studinfo set name='jitesh',sub='js' where id=4"
try:
    db.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where id=8"
try:
    db.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

#Show Data
cr=db.cursor()
select_data="select * from studinfo"
try:
    cr.execute(select_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i[1])
except Exception as e:
    print(e)
    

