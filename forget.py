from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#fun parts
def submit_fun():
    if username_signup_entry.get()==""or password_signup_entry.get()=="" or confirm_password_signup_entry.get()=="":
        messagebox.showerror("ERROR","All Fields Are Requried")
    elif  password_signup_entry.get()!=confirm_password_signup_entry.get():
        messagebox.showerror("ERROR","Password and Confirm Password Are Not Matching")
    else:
        con=pymysql.connect(host='localhost',user='root', password='2603',database='userdata')
        mycursor=con.cursor()
        query= "select * from data where username=%s"
        mycursor.execute(query,(username_signup_entry.get()))
        row= mycursor.fetchone()
        if row==None:
            messagebox.showerror("Error",'Incorrect username')
        else:
            query="update data set password=%s where username=%s"    
            mycursor.execute(query,(password_signup_entry.get(),username_signup_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Password Is Reset,Please login With New Password")
            rootfg.destroy()
            
            
rootfg=Tk()
rootfg.title("foreget password")
width= rootfg.winfo_screenwidth()
height= rootfg.winfo_screenheight()
rootfg.geometry("%dx%d" % (width, height))  # to full size of screen
sgimage=ImageTk.PhotoImage(file="login.png")
snimage_lable=Label(rootfg,image=sgimage)
snimage_lable.place(x=0,y=0)


#DETAILS FRAME 
details_signup_frame=Frame(rootfg,bg="white")
details_signup_frame.pack(pady=130)

#reset password logo
resetpasswordlogo=Label(details_signup_frame,text="RESET PASSWORD",font=("arials",21,"bold"))
resetpasswordlogo.grid(row=2,column=0,sticky='w',padx=15,pady=(20,0))
#usser name sign up
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

#submit button 
submit_button=Button(details_signup_frame,text='SUBMIT',font=("arials",13,"bold"),bg="white",fg="black",cursor="hand2",command=submit_fun)
submit_button.grid(row=9,column=0,pady=20)

rootfg.mainloop()