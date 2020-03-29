import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector # module for connecting python to database
win=tk.Tk()#---->made the box, win is object,Tk() is class
win.title("Database Connectivity")#--->title of box

conn=mysql.connector.connect(host='localhost', username='root', password='ilovemomanddad',database ='dta_bse')
# connects with database 'dta_bse'
cursors=conn.cursor() # cursor defined
name=ttk.Label(win, text="Enter your name :")#--->Label is class
name.grid(row=0,column=0,sticky=tk.W)#--->sticky used to stick to left(West)


ename=ttk.Label(win, text="Enter your email :")
ename.grid(row=1,column=0,sticky=tk.W)

age=ttk.Label(win, text="Enter your age :")
age.grid(row=2,column=0,sticky=tk.W)

gender=ttk.Label(win, text="Enter your gender :")
gender.grid(row=3,column=0,sticky=tk.W)



name_var=tk.StringVar()#--->name_var for storing the input....StringVar means input is str type
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)#---->name_entrybox is variable for box
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()#---->when we start program cursor will be here first

ename_var=tk.StringVar()
ename_entrybox=ttk.Entry(win,width=16,textvariable=ename_var)
ename_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

gender_var=tk.StringVar()#---->gender_var for storing input
gender_entrybox=ttk.Combobox(win,width=16,textvariable=gender_var,state='readonly')#---->readonly so that person cant write anything on combobox
gender_entrybox['values']=('Male','Female','Others')#---->values of combobox
gender_entrybox.grid(row=3,column=1)
gender_entrybox.current(0)#---->sets the default value to Male because it is at 0th position in tuple

usertype=tk.StringVar() 
user=ttk.Radiobutton(win, text='Student',value='Student',variable=usertype)
user.grid(row=4,column=0)
user=ttk.Radiobutton(win, text='Teacher',value='teacher',variable=usertype)
user.grid(row=4,column=1)#---->one variable usertype is initialised for both beacuse person can either be student or teacher

check=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text='Check it !!!',variable=check)
checkbtn.grid(row=5,columnspan=3)#--->columnspan used so that it does not affect columns of other rows...instead use 3 columns alone

def fun():
    win.destroy()
# que="CREATE DATABASE dta_bse"
# cursors.execute(que)
# q = "SELECT * FROM DATABAS"
# cursors.execute(q)

# quer="CREATE TABLE DATA(name VARCHAR(255),ename VARCHAR(255),age INT,gender VARCHAR(255))"
# cursors.execute(quer)
global var
var=0
def action():
    n_ame=name_var.get()
    e_name=ename_var.get()
    a_ge=age_var.get()
    print(n_ame)        
    print(e_name)
    print(a_ge)
    g_ender=gender_var.get() 
    print(g_ender)
    user_type=usertype.get()
    print(user_type)
    
    query="INSERT INTO DATABAS VALUES(%s,%s,%s,%s)"
    values=(n_ame,e_name,a_ge,g_ender)
    cursors.execute(query,values)
    conn.commit()  # it finally adds values to table
    global var
    msg=tk.messagebox.askquestion('Exit App','Do you want to add more records ?',icon ='warning')
    if msg == 'no':
        conn.close()
        var=1
  
    name_entrybox.delete(0,tk.END)#----->once data got submitted it clears the box    
    ename_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    if var==1:
        fun()


cr_button=ttk.Button(win,text='Submit',command=action)#---->action command initiates go to line 50
cr_button.grid(row=6,column=0)

win.mainloop()    
