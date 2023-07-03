from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Desktop Application")

l_id=Label(root,text="ID",font=("Forte",20))
l_id.place(x=50,y=50)
l_name=Label(root,text="Name",font=("Forte",20))
l_name.place(x=50,y=100)
l_dept=Label(root,text="Dpartment",font=("Forte",20))
l_dept.place(x=50,y=150)
l_salary=Label(root,text="Salary",font=("Forte",20))
l_salary.place(x=50,y=200)
