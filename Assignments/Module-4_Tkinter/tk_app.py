import tkinter
from tkinter import ttk,messagebox

window=tkinter.Tk()

window.title("MyApp")
window.geometry("400x500")
window.config(bg="lightblue")

#tkinter.Label(text="Firstname").pack()

flbl=tkinter.Label(text="Firstname",bg="lightblue",fg='red',font='Constantia 15 bold')
#flbl.pack()
#flbl.place(x=0,y=0)
flbl.grid(row=0,column=0,sticky='w')

llbl=tkinter.Label(text="Lastname",bg="lightblue",fg='red',font='Constantia 15 bold')
#llbl.place(x=0,y=20)
llbl.grid(row=1,column=0,sticky='w')

ftxt=tkinter.Entry()
ftxt.grid(row=0,column=1,sticky='w')

ltxt=tkinter.Entry()
ltxt.grid(row=1,column=1,sticky='w')

m=tkinter.Radiobutton(value=0,text="Male",bg="lightblue",fg='red',font='Constantia 15 bold')
m.grid(row=2,column=0,sticky='w')
f=tkinter.Radiobutton(value=1,text="Female",bg="lightblue",fg='red',font='Constantia 15 bold')
f.grid(row=2,column=1,sticky='w')

g=tkinter.Checkbutton(text="Gujarati",bg="lightblue",fg='red',font='Constantia 15 bold')
g.grid(row=3,column=0,sticky='w')

h=tkinter.Checkbutton(text="Hindi",bg="lightblue",fg='red',font='Constantia 15 bold')
h.grid(row=4,column=0,sticky='w')

e=tkinter.Checkbutton(text="English",bg="lightblue",fg='red',font='Constantia 15 bold')
e.grid(row=5,column=0,sticky='w')

city=['Rajkot','Baroda','Surat','Jamnagar','Junagadh']
com=ttk.Combobox(values=city)
com.grid(row=6,column=0,sticky='w')

def btnClick():
    #print("Button Clicked!")
    #messagebox.showerror("Error!","Something went wrong...")
    #messagebox.showinfo("Success!","Signup Successfully!")
    #messagebox.showwarning("Warning!","Your disk is full!")
    print("Firstname:",ftxt.get())
    print("Lasstname:",ltxt.get())

btn=tkinter.Button(text="Submit",bg="black",fg='red',font='Constantia 15 bold',command=btnClick)
#btn.grid(row=10,column=0,sticky='w')
btn.place(x=160,y=250)

window.mainloop()

