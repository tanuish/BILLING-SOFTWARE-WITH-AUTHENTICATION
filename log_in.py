from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
#fun part


def reset_password():
    rootln.destroy()
    import forget
      
def login_button_function():
    if login_name_entry.get()=='' or login_password_entry.get()=='':
        messagebox.showerror("Error","All fields Are Required")
    else:
        try:    
           con=pymysql.connect(host='localhost',user='root',password='2603')
           mycursor=con.cursor()
        except:
            messagebox.showerror("Error","Database Connectivity Issue, Please Try again")
            return
        query="use userdata"
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(login_name_entry.get(),login_password_entry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','invalid username or password')
        else:
            messagebox.showinfo("welecome","Login is Successful")
            rootln.destroy()
            import main
                
def signup_page_move():
    rootln.destroy()
    import signup
    
#for login ussername fixed  or removed using cursle 
def login_name_entry_fun(event):
    if login_name_entry.get() == "username":
        login_name_entry.delete(0,END)
         
#for login ussername fixed  or removed using cursle
def login_password_entry_fun(odded):
    if login_password_entry.get()== "password":
        login_password_entry.delete(0,END)

#for eye in password to close or open 
def  hide_eye():
    openeye.config(file="closeye.png")
    login_password_entry.config(show="*")
    eyebutton.config(command=SHOW)

# for show eye fun 
def SHOW():
        openeye.config(file="openeye.png")
        login_password_entry.config(show="")
        eyebutton.config(command=hide_eye)


#gui part 
rootln=Tk()
rootln.title("Login page")
width= rootln.winfo_screenwidth()
height= rootln.winfo_screenheight()
rootln.geometry("%dx%d" % (width,height))#to full size of screen 
# rootln.attributes('-fullscreen',True)
# rootln.iconbitmap('icon.ico')


#rootln.geometry("990x660+50+50")
bgimage=PhotoImage(file="login.png")
bglabel=Label(rootln,image=bgimage)
bglabel.place(x=0,y=0)


#login label  label 
login_label_frame=Frame(rootln,bg="white")
login_label_frame.pack(pady=180)

#namelabel  in login_label_frame
login_user_lebel=Label(login_label_frame,text='USER LOGIN',font=('Times New Roman',23,'bold'),height=2,width=15,bd=3,bg="white")
login_user_lebel.grid(row=0,column=0) 

# login name entry in login_label_frame
login_name_entry=Entry(login_label_frame,font=('Times New Roman',13,'bold'),bd=2,width=22)
login_name_entry.grid(row=1,column=0,pady=10)
login_name_entry.insert(0,"username")
login_name_entry.bind("<FocusIn>",login_name_entry_fun)# bind use for fixed the word inside the entry box 


#login password  entry in login_label_frame
login_password_entry=Entry(login_label_frame,font=('Times New Roman',13,'bold'),bd=2,width=22)
login_password_entry.grid(row=2,column=0,pady=10)
login_password_entry.insert(0,"password")
login_password_entry.bind("<FocusIn>",login_password_entry_fun)

# button for openeye or closeeye in password entry
openeye=PhotoImage(file="openeye.png")
eyebutton=Button(login_label_frame,image=openeye,bd=0,cursor="hand2",command=hide_eye,bg="white",activebackground="white")
eyebutton.place(x=218,y=139)

# forget button 
forget_button=Button(login_label_frame,text="forgot password?",font=('Times New Roman',13,'bold'),bg="white",activebackground="white",bd=0,cursor="hand2",command=reset_password)
forget_button.grid(row=3,column=0,sticky="w",padx=10)

# login button 
login_button=Button(login_label_frame,text="LOGIN",font=('Times New Roman',13,'bold'),width=10,bg="white",activebackground="white",bd=2,cursor="hand2",command=login_button_function)
login_button.grid(row=4,column=0 ,)

# or lable 
or_lable=Label(login_label_frame,text="---------------or---------------",font=("Time New Roman",17,"bold"),bg="white")
or_lable.grid(row=5,column=0)

#sign in label 
signin_label=Label(login_label_frame,height=4,width=10,bg="white")
signin_label.grid(row=6,column=0)
#google sign in 
google=PhotoImage(file="google.png")
google_signin=Button(login_label_frame,image=google,bd=0,bg="white",cursor="hand2")
google_signin.place(x=120,y=283)

#facebook 
facebook=PhotoImage(file="facebook.png")
facebook_signin=Label(login_label_frame,image=facebook,bd=0,bg="white")
facebook_signin.place(x=60,y=283)

#twitter 
twitter=PhotoImage(file="twitter.png")
twitter_signin=Label(login_label_frame,image=twitter,bd=0,bg="white")
twitter_signin.place(x=180,y=283)

# create new account logo
create_label=Label(login_label_frame,)
create_label.grid(row=7,column=0)

#create new button 
dont_have=Label(login_label_frame,text="Dont have an account?",fg="red",bg="white")
dont_have.place(x=10,y=330) 

#create button 
create_button=Button(login_label_frame,text="create new account?",fg="blue",bg="white",bd=0,activebackground="white",cursor="hand2",command=signup_page_move)
create_button.place(x=160,y=330  )
rootln.mainloop()