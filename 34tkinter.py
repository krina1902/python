from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_tkinter"
        )
def insert_data():
    if e_name.get()=="" or e_dept.get()=="" or e_salary.get()=="":
         msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into emp(name,dept,salary) values(%s,%s,%s)"
        argu=(e_name.get(),e_dept.get(),e_salary.get())
        cursor.execute(query,argu)
        conn.commit()
        conn.close()
        e_name.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        msg.showinfo("Insert Status","Insert Data Successfully")

def search_data():
     e_name.delete(0,"end")
     e_dept.delete(0,"end")
     e_salary.delete(0,"end")
     if e_id=="":
        msg.showinfo("Search Status","Id is Mandatory")
     else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from emp where id=%s"
        argu=(e_id.get(),)
        cursor.execute(query,argu)
        row=cursor.fetchall()
        if row:
            for i in row:
                e_name.insert(0,i[1])
                e_dept.insert(0,i[2])
                e_salary.insert(0,i[3])
        else:
            msg.showinfo("Search Status","Id Is Not Found")
        conn.close()

def update_data():
    if e_id.get()=="" or e_name.get()=="" or e_dept.get()=="" or e_salary.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update emp set name=%s,dept=%s,salary=%s where id=%s"
        argu=(e_name.get(), e_dept.get(),e_salary.get(),e_id.get())
        cursor.execute(query,argu)
        conn.commit()
        conn.close()
        e_name.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        e_id.delete(0,"end")
        msg.showinfo("Update Status","Data Updated Successfully")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","Id Is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from emp where id=%s"
        argu=(e_id.get(),)
        cursor.execute(query,argu)
        conn.commit()
        conn.close()
        e_name.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        e_id.delete(0,"end")
        msg.showinfo("Delete Status","Data Deleted Successfully")



        
root=Tk()
root.geometry("550x500")
root.title("Desktop Application")
root.resizable(width=False ,height=False)

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


insert=Button(root,text="INSERT",bg="black",fg="white",font=("Forte",20),command=insert_data)
insert.place(x=50,y=300)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Forte",20),command=search_data)
search.place(x=300,y=300)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Forte",20),command=update_data)
update.place(x=50,y=400)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Forte",20),command=delete_data)
delete.place(x=300,y=400)
