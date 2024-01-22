from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#fun parts

def clear():
    email_signup_entry.delete(0,END)
    username_signup_entry.delete(0,END)
    password_signup_entry.delete(0,END)
    confirm_password_signup_entry.delete(0,END)
    check.set(0)

def connect_database():
     if email_signup_entry.get()=='' or username_signup_entry.get()=='' or password_signup_entry.get()=='' or confirm_password_signup_entry.get()=='':
         messagebox.showerror("Error","All fields Are Required")
     elif password_signup_entry.get() != confirm_password_signup_entry.get():
         messagebox.showerror("Error","Password Mismatch")
     elif check.get()==0:
         messagebox.showerror('Error',"Please accept Terms & Conditions")
     else:
         try:
              con=pymysql.connect(host='localhost',user='root',password='2603')# for create databases 
              mycursor=con.cursor()
         except:
             messagebox.showerror("Error","Database Connectivity Issue, Please Try again")    
             return 
         
         try:
             query="create database userdata"
             mycursor.execute(query)
             query="use userdata"
             mycursor.execute(query)
             query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'         
             mycursor.execute(query)
         except:
             mycursor.execute('use userdata') 
             
         query= 'select * from data where username=%s'# for copy right to get excuete 
         mycursor.execute(query,(username_signup_entry.get()))  
         
         row=mycursor.fetchone()   # fatch data from data base to be copy right
         if row !=None:
             messagebox.showerror('Error','Username Already exists')
         else:    
              query='insert into data(email,username,password) values(%s,%s,%s)'
              mycursor.execute(query,(email_signup_entry.get(),username_signup_entry.get(),password_signup_entry.get()))
              con.commit()
              con.close()
              messagebox.showinfo('Success','Registration is successful')      
              clear()
              rootsn.destroy()
              import log_in

         
def login_page():
    rootsn.destroy()
    import log_in

# gui part  
rootsn=Tk()
rootsn.title("Signup page")
width= rootsn.winfo_screenwidth()
height= rootsn.winfo_screenheight()
rootsn.geometry("%dx%d" % (width, height))    #  to full size of screen
sgimage=ImageTk.PhotoImage(file="login.png")
snimage_lable=Label(rootsn,image=sgimage)
snimage_lable.place(x=0,y=0)



#DETAILS FRAME 
details_signup_frame=Frame(rootsn,bg="white")
details_signup_frame.pack(pady=130)

#namelabel  in signin_label_frame
signin_user_lebel=Label(details_signup_frame,text='CREATE AN ACCOUNT',font=('Times New Roman',20,'bold'),bd=3,bg="white")
signin_user_lebel.grid(row=0,column=0,pady=10) 


# email sign up
email_signup_label=Label(details_signup_frame,text="Email:",font=("arials",13,"bold"))
email_signup_label.grid(row=1,column=0,sticky="w",padx=15,pady=(10,0))

# email sign up entry 
email_signup_entry=Entry(details_signup_frame,width=30,font=("arials",13,"bold"))
email_signup_entry.grid(row=2,column=0,sticky="w",padx=15)

# usser name sign up
username_signup_label=Label(details_signup_frame,text="Username:",font=("arials",13,"bold"))
username_signup_label.grid(row=3,column=0,sticky="w",padx=15,pady=(20,0))

# username sign up entry 
username_signup_entry=Entry(details_signup_frame,width=30,font=("arials",13,"bold"))
username_signup_entry.grid(row=4,column=0,sticky="w",padx=15)

#password name sign up

password_signup_label=Label(details_signup_frame,text="Password:",font=("arials",13,"bold"))
password_signup_label.grid(row=5,column=0,sticky="w",padx=15,pady=(20,0))

# password sign up entry 
password_signup_entry=Entry(details_signup_frame,width=30,font=("arials",13,"bold"))
password_signup_entry.grid(row=6,column=0,sticky="w",padx=15)

#confirm_password name sign up

confirm_password_signup_label=Label(details_signup_frame,text="Confirm Password:",font=("arials",13,"bold"))
confirm_password_signup_label.grid(row=7,column=0,sticky="w",padx=15,pady=(20,0))

#confirm_password sign up entry 
confirm_password_signup_entry=Entry(details_signup_frame,width=30,font=("arials",13,"bold"))
confirm_password_signup_entry.grid(row=8,column=0,sticky="w",padx=15)

#term and condition checkbutton
check=IntVar()
termsandcondition=Checkbutton(details_signup_frame,text="I agree to the terms & conditions",font=("arials",13,"bold"),cursor="hand2",variable=check)
termsandcondition.grid(row=9,column=0,sticky="w",pady=20)

# sign in button 
signin_button=Button(details_signup_frame,text="Sign Up",font=("arials",13,"bold"),bg="red",fg='WHITE',width=25,height=1,command=connect_database)
signin_button.grid(row=10,column=0,pady=10)

# login button 
signin_login_button=Button(details_signup_frame,text="LogIn",font=("arials",13,"bold underline"),command=login_page)
signin_login_button.grid(row=11,column=0,sticky="e",padx=(0,25),pady=(0,10))

#  have a acount lable
signin_haveaccount_lable=Label(details_signup_frame,text="have already account?",font=("arials",13,"bold underline"))
signin_haveaccount_lable.place(x=20,y=447)


rootsn.mainloop()