from tkinter import *

root=Tk()
root.geometry("550x500")
root.title("Desktop Application")

l_id=Label(root,text="ID",font=("Forte",20))
l_id.place(x=50,y=50)
l_name=Label(root,text="Name",font=("Forte",20))
l_name.place(x=50,y=100)
l_dept=Label(root,text="Dpartment",font=("Forte",20))
l_dept.place(x=50,y=150)
l_salary=Label(root,text="Salary",font=("Forte",20))
l_salary.place(x=50,y=200)


e_id=Entry()
e_id.place(x=190,y=60,width=300)
e_name=Entry()
e_name.place(x=190,y=110,width=300)
e_dept=Entry()
e_dept.place(x=190,y=160,width=300)
e_salary=Entry()
e_salary.place(x=190,y=210,width=300)


insert=Button(root,text="INSERT",bg="black",fg="white",font=("Forte",20))
insert.place(x=50,y=300)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Forte",20))
search.place(x=300,y=300)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Forte",20))
update.place(x=50,y=400)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Forte",20))
delete.place(x=300,y=400)
