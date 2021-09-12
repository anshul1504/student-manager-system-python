from tkinter import *
import sqlite3
from tkinter import messagebox

t=Tk()
t.geometry("600x430+450+230")
t.resizable(0,0)
t.title("Manager")
t.configure(bg="white")
f55=None


u1=Label(text="Student Information Manager",font="arial 15 bold",bg="gold",bd=2,relief=SOLID)
u1.pack(fill=X)



def e():
    f3=Frame(bg="#074461",bd=3,relief=SOLID)
    f3.place(x=0,y=32,width=599,height=335)
    u1=Label(f3,text="\n\n\n\n\nWelcome to the \n\n\"STUDENT MANAGER SOFTWARE\"",font="arial 15 bold",bg="#074461",fg="gold")
    u1.place(x=120,y=0)
    
    
e()

def update():
    f3=Frame(bg="#074461",bd=3,relief=SOLID)
    f3.place(x=0,y=32,width=599,height=335)
    b11=Button(f3,text="<<",font="arial 11 bold",bd=0,relief=FLAT,bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=e)
    b11.place(x=5,y=10)
    s1=StringVar()
    u6=Label(f3,text="Enter Roll No:-",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u6.place(x=50,y=10,width=150,height=25)
    e1=Entry(f3,font=("",15),bd=2,relief=SOLID,textvariable=s1)
    e1.place(x=220,y=10,width=210,height=25)
    def update1():
        import sqlite3
        db=sqlite3.connect("insert.db")
        cr=db.cursor()
        r=cr.execute("select * from ins where Roll='"+s1.get()+"'")
        
        for r1 in r:
            s2=StringVar()
            s3=StringVar()
            s4=StringVar()
            
            u2=Label(f3,text="Name:-",font=("",15),bd=2,relief=SOLID,bg="cyan",fg="black")
            u2.place(x=140,y=70,width=150,height=25)
            u3=Entry(f3,bd=2,relief=SOLID,font=("",13),textvariable=s2)
            u3.insert(0,r1[1])
            u3.place(x=310,y=70,width=150,height=25)
            u4=Label(f3,text="Father Name:-",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
            u4.place(x=140,y=120,width=150,height=25)
            u5=Entry(f3,font=("",13),textvariable=s3,bd=2,relief=SOLID)
            u5.insert(0,r1[2])
            u5.place(x=310,y=120,width=150,height=25)
            u6=Label(f3,text="Contact No:-",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
            u6.place(x=140,y=170,width=150,height=25)
            u7=Entry(f3,font=("",13),textvariable=s4,bd=2,relief=SOLID)
            u7.insert(0,r1[3])
            u7.place(x=310,y=170,width=150,height=25)
            def update2():
                op=messagebox.askyesno("Exit","Do you really want to Update?")
                if op>0:
                    db=sqlite3.connect("insert.db")
                    cr=db.cursor()
                    cr.execute("update ins set Name='"+s2.get()+"',Father='"+s3.get()+"',Contact='"+s4.get()+"' where Roll='"+s1.get()+"'")
                    db.commit()
                    db.close()
                    
                    messagebox.showinfo("Update","Sucess")
                    s1.set("")
                    s2.set("")
                    s3.set("")
                    s4.set("")
                    update()
                
            
            b1=Button(f3,text="Update",font=("",15),bg="gold",bd=0,relief=FLAT,fg="black",activebackground="cyan",activeforeground="black",command=update2)
            b1.place(x=230,y=220,width=130,height=33)
            
            break
            
        else:
                        
            messagebox.showerror("Error","No search related data found")
            update()
            
        db.commit()
        db.close()
    
    
    b1=Button(f3,text="Search",font=("",15),bg="gold",fg="black",activebackground="cyan",bd=0,relief=FLAT,activeforeground="black",command=update1)
    b1.place(x=450,y=10,width=130,height=25)


def search():
    f3=Frame(bg="#074461",bd=3,relief=SOLID)
    f3.place(x=0,y=32,width=599,height=335)
    b11=Button(f3,text="<<",font="arial 11 bold",bd=0,relief=FLAT,bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=e)
    b11.place(x=5,y=10)
    s1=StringVar()
    u6=Label(f3,text="Roll No:-",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u6.place(x=80,y=10,width=100,height=25)
    e1=Entry(f3,font=("",15),textvariable=s1,bd=2,relief=SOLID)
    e1.place(x=210,y=10,width=210,height=25)
    
    def search1():
        import sqlite3
        db=sqlite3.connect("insert.db")
        cr=db.cursor()
        r=cr.execute("select * from ins where Roll='"+s1.get()+"'")
        if s1.get()=="":
                messagebox.showerror("search","Please Enter Your Rollno First")
        
        for r1 in r:          
            op=messagebox.askyesno("Exit","Do you really want to Search?")
            if op>0:
                u2=Label(f3,text="Name",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
                u2.place(x=140,y=90,width=150,height=25)
                u3=Label(f3,text=r1[1],font=("",13),bg="gold",fg="black",bd=2,relief=SOLID)
                u3.place(x=310,y=90,width=150,height=25)
                u4=Label(f3,text="Father Name",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
                u4.place(x=140,y=140,width=150,height=25)
                u5=Label(f3,text=r1[2],font=("",13),bg="gold",fg="black",bd=2,relief=SOLID)
                u5.place(x=310,y=140,width=150,height=25)
                u6=Label(f3,text="Contact No",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
                u6.place(x=140,y=190,width=150,height=25)
                u7=Label(f3,text=r1[3],font=("",13),bg="gold",fg="black",bd=2,relief=SOLID)
                u7.place(x=310,y=190,width=150,height=25)
                break           
            else:
                u2=Label(f3,text="Name",font=("",15),bg="#074461",fg="#074461")
                u2.place(x=0,y=90,width=590,height=25)
                u4=Label(f3,text="Father name",font=("",15),bg="#074461",fg="#074461")
                u4.place(x=0,y=140,width=590,height=25)
                u6=Label(f3,text="LIC",font=("",15),bg="#074461",fg="#074461")
                u6.place(x=0,y=190,width=590,height=25)
                
        db.commit()
        db.close()
        
        s1.set("")
        
   
    b1=Button(f3,text="Search",font=("",15),bd=2,relief=FLAT,bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=search1)
    b1.place(x=450,y=10,width=100,height=25)


def delete():
    f3=Frame(bg="#074461",bd=3,relief=SOLID)
    f3.place(x=0,y=32,width=599,height=335)
    b11=Button(f3,text="<<",font="arial 11 bold",bd=0,relief=FLAT,bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=e)
    b11.place(x=5,y=10)
    d1=StringVar()
    u6=Label(f3,text="Enter Roll No:-",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u6.place(x=30,y=100,width=150,height=25)
    e1=Entry(f3,font=("",15),textvariable=d1,bd=2,relief=SOLID)
    e1.place(x=200,y=100,width=200,height=25)
    def de1():
        if d1.get()=="":
            messagebox.showerror("Error","For deletion of  data required Rollno")
        else:
            op=messagebox.askyesno("Exit","Do you really want to Delete?")
            if op>0:
                import sqlite3
                db=sqlite3.connect("insert.db")
                cr=db.cursor()
                cr.execute("delete from ins where Roll='"+d1.get()+"'")
                db.commit()
                db.close()
                messagebox.showinfo("Delete","Sucess,your student information are deleted")
            d1.set("")
        
    b1=Button(f3,text="Delete",font=("",15),bd=0,relief=FLAT,bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=de1)
    b1.place(x=430,y=100,width=130,height=25)
    

def show1(f3):
    b11=Button(f3,text="<<",font="arial 11 bold",bd=0,relief=FLAT,bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=e)
    b11.place(x=5,y=10)
    u1=Label(f3,text="Roll",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u1.place(x=60,y=10,width=90,height=25)
    u2=Label(f3,text="Name",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u2.place(x=190,y=10,width=90,height=25)
    u3=Label(f3,text="Father Name",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u3.place(x=305,y=10,width=120,height=25)
    u4=Label(f3,text="Contact",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u4.place(x=450,y=10,width=90,height=25)
    import sqlite3
    db=sqlite3.connect("insert.db")
    cr=db.cursor()
    r=cr.execute("select * from ins")
    x=60
    y=50
    for r1 in r:
        Label(f3,text=r1[0],font=("",11),bg="#074461",fg="white",bd=1,relief=SOLID).place(x=x,y=y,width=90,height=20)
        x+=130
        Label(f3,text=r1[1],font=("",11),bg="#074461",fg="white",bd=1,relief=SOLID).place(x=x,y=y,width=90,height=20)
        x+=130
        Label(f3,text=r1[2],font=("",11),bg="#074461",fg="white",bd=1,relief=SOLID).place(x=x,y=y,width=90,height=20)
        x+=130
        Label(f3,text=r1[3],font=("",11),bg="#074461",fg="white",bd=1,relief=SOLID).place(x=x,y=y,width=90,height=20)
        x+=120
        y+=30
        x=60
    db.commit()
    db.close()

def show():
    f3=Frame(bg="#074461",bd=3,relief=SOLID)
    f3.place(x=0,y=32,width=599,height=335)
    global f55
    f55=f3
    show1(f3)


def ins1():
    present="no"
    if a1.get()=="" or a2.get()=="" or a3.get()=="" or a4.get()=="":
            messagebox.showerror("Error","No Data Found For Insertion\nPls Fill Detail Before Insertion")
    else:
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            db=sqlite3.connect("insert.db")
            cr=db.cursor()
            cr.execute("insert into ins values('"+a1.get()+"','"+a2.get()+"','"+a3.get()+"','"+a4.get()+"')")
            db.commit()
            db.close()
            messagebox.showinfo("Insert","Sucess,your Student all details store sucessfully")
            a1.set("")
            a2.set("")
            a3.set("")
            a4.set("")
        else:
            a1.set("")
            a2.set("")
            a3.set("")
            a4.set("")

a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()

def insert():
    f3=Frame(bg="#074461",bd=3,relief=SOLID)
    f3.place(x=0,y=32,width=599,height=335)
    u0=Label(f3,text="Roll No",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u0.place(x=120,y=50,width=150,height=25)
    u2=Label(f3,text="Name",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u2.place(x=120,y=100,width=150,height=25)
    u3=Label(f3,text="Father Name",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u3.place(x=120,y=150,width=150,height=25)
    u4=Label(f3,text="Contact Number",font=("",15),bg="cyan",fg="black",bd=2,relief=SOLID)
    u4.place(x=120,y=200,width=150,height=25)
    
    e1=Entry(f3,font=("",13),textvariable=a1,bd=3,relief=SOLID)
    e1.place(x=310,y=50,width=180,height=25)
    e2=Entry(f3,font=("",13),textvariable=a2,bd=3,relief=SOLID)
    e2.place(x=310,y=100,width=180,height=25)
    e3=Entry(f3,font=("",13),textvariable=a3,bd=3,relief=SOLID)
    e3.place(x=310,y=150,width=180,height=25)
    e4=Entry(f3,font=("",13),textvariable=a4,bd=3,relief=SOLID)
    e4.place(x=310,y=200,width=180,height=25)
    b1=Button(f3,text="Insert",font=("",13),bg="gold",bd=0,relief=FLAT,command=ins1)
    b1.place(x=210,y=250,width=130,height=30)
    b11=Button(f3,text="<<",font="arial 11 bold",bd=0,relief=FLAT,bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=e)
    b11.place(x=5,y=10)

def g():
    f2=Frame(bg="yellow",bd=2,relief=SOLID)
    f2.place(x=0,y=370,width=600,height=30)
    b1=Button(f2,text="Search",font="arial 13 bold",bg="lightgreen",bd=2,relief=FLAT,command=search)
    b1.place(x=0,height=30,width=120)
    b2=Button(f2,text="Update",font="arial 13 bold",bg="yellow",bd=2,relief=FLAT,command=update)
    b2.place(x=120,height=30,width=120)
    b3=Button(f2,text="Insert",font="arial 13 bold",bg="lightgreen",bd=2,relief=FLAT,command=insert)
    b3.place(x=240,height=30,width=120)
    b4=Button(f2,text="Delete",font="arial 13 bold",bg="yellow",bd=2,relief=FLAT,command=delete)
    b4.place(x=360,height=30,width=120)
    b5=Button(f2,text="Show All",font="arial 13 bold",bg="lightgreen",bd=2,relief=FLAT,command=show)
    b5.place(x=480,height=30,width=120)
g()

def j():
    f4=Frame(bg="#074461",bd=2,relief=SOLID)
    f4.place(x=0,y=400,width=600,height=30)
    b5=Button(f4,text="Exit",font="arial 13 bold",bg="lightblue",bd=2,relief=FLAT,command=t.destroy)
    b5.pack(side=BOTTOM,fill=X)
    
    
    
j()

t.mainloop()