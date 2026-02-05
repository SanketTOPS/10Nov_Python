import tkinter
import sqlite3

tk=tkinter.Tk()
tk.title("DBApp")
tk.geometry("300x400")
tk.config(bg="lightblue")

lbl1=tkinter.Label(text="Name:",bg="lightblue",fg="red",font="Georgia 15 bold")
lbl1.grid(row=0,column=0)

lbl2=tkinter.Label(text="Subject:",bg="lightblue",fg="red",font="Georgia 15 bold")
lbl2.grid(row=1,column=0)

txt1=tkinter.Entry()
txt1.grid(row=0,column=1)

txt2=tkinter.Entry()
txt2.grid(row=1,column=1)


try:
    db=sqlite3.connect("tkdb.db")
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

def insertData():
    nm=txt1.get()
    sub=txt2.get()

    insert_q=f"insert into studinfo(name,sub)values('{nm}','{sub}')"
    try:
        db.execute(insert_q)
        db.commit()
        print("Record inserted!")
    except Exception as e:
        print(e)

btn=tkinter.Button(text="Save",fg="red",font="Georgia 15 bold",command=insertData)
#btn.grid(row=2,column=0)
btn.place(x=110,y=80)

tk.mainloop()