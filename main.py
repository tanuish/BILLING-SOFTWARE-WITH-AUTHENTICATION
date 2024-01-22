from tkinter import *
from tkinter import messagebox
import random
import os
import tempfile
from datetime import datetime
import smtplib
import requests
from twilio.rest import Client

#funtionality part
if not os.path.exists("Bills"):
  os.mkdir("Bills")


# for phone send  button in product frame 

def phone_fun():
  
  def phone_send_fun():
    # message_phone_fun=phone_textarea.get(1.0,END)
    # number=phone_number_entry_fun.get()
    # auth='RqxXKSQeHkTLfG8lu6pnIjBsEdgzbD5M4W9y3v1CJUwrihVatYgOrPMIt9kK6bCjv43cy7pL8YsEqiSB'
    # url='https://www.fast2sms.com/dev/bulk'
    
    # pram={
    #   'authorization':auth,
    #   'message':message_phone_fun,
    #   'numbers':number,
    #   'sender -id':'FSTSMS',
    #   'route':'p',
    #   'language':'english'
    # }
    # response=requests.get(url,params=pram)
    # dic=response.json()
    # result=dic.get('return')
     
   SID = 'ACde608470136de25bf2c411571078542b'
   AUTH_TOKEN = 'c7fecf4f6148e7498057967389c18da6'
   message_phone_fun=phone_textarea.get(1.0,END)
   number=phone_number_entry_fun.get()

   cl =Client(SID, AUTH_TOKEN)

   api=cl.messages.create(body= message_phone_fun, from_='+12562910517', to=number)
   if api==True:
    messagebox.showinfo('SEND Successfully','Message Sent Successfully')
    
   else:
      messagebox.showerror('ERROR','Something Went Wrong') 
  
    
  root2=Toplevel()
  root2.title('Send To Phone')
  root2.config(bg='grey20')
  root2.geometry('485x620+50+50')
  
  logoimage=PhotoImage(file='sender.png')
  img_lable_phone=Label(root2,image=logoimage,bg='grey20',fg='grey20')
  img_lable_phone.pack()
  
  phone_number_label_fun=Label(root2,text='PHONE NUMBER',font=('arial',18,'bold underline',),bg='grey20',fg='gold')
  phone_number_label_fun.pack(pady=10)
  
  phone_number_entry_fun=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=23)
  phone_number_entry_fun.pack()
  
  bill_label_fun=Label(root2,text='BILL DETAILS',font=('arial',18,'bold underline',),bg='grey20',fg='gold')
  bill_label_fun.pack(pady=10)
  
  phone_textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=11)
  phone_textarea.pack()
  
  #fun
  phone_textarea.delete(1.0,END)
  phone_textarea.insert(END,Text_area.get(1.0,END).replace("=","").replace('\t\t\t','\t\t'))
  
  phone_send_button=Button(root2,text='SEND',font=('arial',19,'bold'),bd=7,relief=GROOVE,bg='grey20',fg='white',command=phone_send_fun)
  phone_send_button.pack(pady=10)
  
  root2.mainloop()

# for mail send buttion in produt frame

def email_fun():
  
  #send mail button fun
  def mail_send_fun():
    try:
        
      obj=smtplib.SMTP('smtp.gmail.com',587)
      obj.starttls()
      obj.login(emailid_label_entry.get(),emailid_password_entry.get())
      message_text= email_text_area.get(1.0,END)
      obj.sendmail(emailid_label_entry.get(),emailid_receiver_label_entry.get(),message_text)
      obj.quit()
      messagebox.showinfo('SUCCESS',"Bill is  Successfully sent",parent=root1)
      root1.destroy()
    
    except:
      messagebox.showerror("ERROR",'Something Went Wrong ,Try Again After Sometime',parent=root1)
      
  if Text_area.get(1.0,END)=='\n':
    messagebox.showerror('Error',"Bill is Emty")
  
  else:  
    root1=Toplevel()
    root1.grab_set()
    root1.title('Send Gmail ')
    root1.resizable(0,0)
    root1.config(bg="grey20")
    
    #frame for lable frame of sender 
    mail_sender_frame=LabelFrame(root1,text="SENDER",font=('arial',16,"bold"),bg="grey20",fg="gold",bd=6,relief=GROOVE)
    mail_sender_frame.grid(row=0,column=0,padx=40,pady=20)
    
    #inside label frame for sender information(gmail id label) 
    emailid_label=Label(mail_sender_frame,text="Sender's mail",font=('arial',14,"bold"),bg="grey20",fg="white")
    emailid_label.grid(row=0,column=0,padx=10,pady=8)
    
    #for email id entry
    emailid_label_entry=Entry(mail_sender_frame,font=('arial',14,"bold"),bd=2,relief=GROOVE,width=23)
    emailid_label_entry.grid(row=0,column=1,padx=10,pady=8)
    
    #inside label frame for sender information(gmail id password label) 
    emailid_password=Label(mail_sender_frame,text="Password",font=('arial',14,"bold"),bg="grey20",fg="white")
    emailid_password.grid(row=1,column=0,padx=10,pady=8)
                
    #for email id password entry
    emailid_password_entry=Entry(mail_sender_frame,font=('arial',14,"bold"),bd=2,relief=GROOVE,width=23)
    emailid_password_entry.grid(row=1,column=1,padx=10,pady=8)
    
    #frame for lable frame of Receiver 
    mail_recipient_frame=LabelFrame(root1,text="RECIPIENT",font=('arial',16,"bold"),bg="grey20",fg="gold",bd=6,relief=GROOVE)
    mail_recipient_frame.grid(row=1,column=0,padx=40,pady=20)
    
    #inside label frame for Receiver information(gmail id label) 
    emailid_receiver_label=Label(mail_recipient_frame,text="Email Address",font=('arial',14,"bold"),bg="grey20",fg="white")
    emailid_receiver_label.grid(row=0,column=0,padx=10,pady=8)
    
    #for Receiver email id entry
    emailid_receiver_label_entry=Entry(mail_recipient_frame,font=('arial',14,"bold"),bd=2,relief=GROOVE,width=23)
    emailid_receiver_label_entry.grid(row=0,column=1,padx=10,pady=8)
    
    #messagelabel 
    messagelabel=Label(mail_recipient_frame,text="Message",font=('arial',14,'bold'),bg='grey20',fg='white')
    messagelabel.grid(row=1,column=0,padx=10,pady=8)
    
    #email text area
    email_text_area=Text(mail_recipient_frame,font=('arial',14,'bold'),bd=2,relief=GROOVE,width=42,height=11)
    email_text_area.grid(row=2,column=0,columnspan=2)
    #fun
    email_text_area.delete(1.0,END)
    email_text_area.insert(END,Text_area.get(1.0,END).replace("=","").replace('\t\t\t','\t\t'))
    
    #mail send button
    mail_send_button=Button(root1,text="SEND",font=('arial',16,'bold'),bg='white',fg="black",bd=2,relief=GROOVE,width=15,command=mail_send_fun)
    mail_send_button.grid(row=2,column=0,columnspan=2,pady=10) 
    root1.mainloop() 



# for print button in product frame 

def print_button_fun():
  
  if Text_area.get(1.0,END)=="\n":
    messagebox.showerror('Error','Bill is Emty')
  else:
    file=tempfile.mktemp(".txt")
    open(file,'w').write(Text_area.get(1.0,END))
    os.startfile(file,'print')


# for clear button in bill frame 

def clear_fun():
  #delete value
  
  makeup_kit_entry.delete(0,END)
  facewash_entry.delete(0,END)
  bodylotion_entry.delete(0,END)
  facecream_entry.delete(0,END)
  handwash_entry.delete(0,END)
  foundation_entry.delete(0,END)
  
  Rice_entry.delete(0,END)
  Daal_entry.delete(0,END)
  Wheat_entry.delete(0,END)
  sugar_entry.delete(0,END)
  masala_entry.delete(0,END)
  Oil_entry.delete(0,END)
  
  Tomato_entry.delete(0,END)
  patato_entry.delete(0,END)
  Onion_entry.delete(0,END)
  lady_finger_entry.delete(0,END)
  ceavage_entry.delete(0,END)
  pumkin_entry.delete(0,END)
  
  #insert value 
  
  makeup_kit_entry.insert(0,0)
  facewash_entry.insert(0,0)
  bodylotion_entry.insert(0,0)
  facecream_entry.insert(0,0)
  handwash_entry.insert(0,0)
  foundation_entry.insert(0,0)
  
  Rice_entry.insert(0,0)
  Daal_entry.insert(0,0)
  Wheat_entry.insert(0,0)
  sugar_entry.insert(0,0)
  masala_entry.insert(0,0)
  Oil_entry.insert(0,0)
  
  Tomato_entry.insert(0,0)
  patato_entry.insert(0,0)
  Onion_entry.insert(0,0)
  lady_finger_entry.insert(0,0)
  ceavage_entry.insert(0,0)
  pumkin_entry.insert(0,0)
  
  name_entry.delete(0,END)
  phone_entry.delete(0,END)
  bill_number_entry.delete(0,END)
  Text_area.delete(1.0,END)
  
  cosmetic_price_entry.delete(0,END)
  grocery_price_entry.delete(0,END)
  vagetable_price_entry.delete(0,END)
  
  cosmetic_tax_entry.delete(0,END)
  grocery_tax_entry.delete(0,END)
  vagetable_tax_entry.delete(0,END)
    
# for exit buttion in bill frame

def exit_fun():
  root.destroy()        
  
#for search bill fun in bill frame 
def search_bill_fun():
  for i in os.listdir("Bills/"):
    if i.split('.')[0]==bill_number_entry.get():
      f=open(f"Bills/{i}","r")
      Text_area.delete(1.0,END)
      for data in f:
        Text_area.insert(END,data)
      f.close()
      break
  
  else:
    messagebox.showerror('Error',"invalid Bill Number ") 
         
         
#for Save  fun in bill frame   
def Save():
  global billnumber
  
  if Text_area.get(1.0,END)=='\n':
    messagebox.showerror('Error',"'Bill is Emty")
  else:
    
    result =messagebox.askyesno('confirm',"Do  you want to Save the bill ")
 
    if result:
      bill_contant_savefun=Text_area.get(1.0,END)
      file=open(f'Bills/{billnumber}.txt','w')
      file.write(bill_contant_savefun)
      file.close()
      messagebox.showinfo('Success',f'Bill Number {billnumber} is Save Successfully')
      billnumber=random.randint(100,1000)

#for random value 
billnumber=random.randint(100,1000)


#for total buttion fun  in bill frame
def total():
  
  global makeup_kit_cosmetic_price,facecream_cosmetic_price,facewash_cosmetic_price,bodylotion_cosmetic_price,handwash_cosmetic_price,foundation_cosmetic_price
    
    
    # for total(button) cosmetics price in bill frame
     
  makeup_kit_cosmetic_price =int(makeup_kit_entry.get())*35
  
  facewash_cosmetic_price =int(facewash_entry.get())*95
  
  bodylotion_cosmetic_price =int(bodylotion_entry.get())*110
  
  facecream_cosmetic_price =int(facecream_entry.get())*65
  
  handwash_cosmetic_price =int(handwash_entry.get())*100
  
  foundation_cosmetic_price =int(foundation_entry.get())*125
  
  total_cosmetics_price= makeup_kit_cosmetic_price + facecream_cosmetic_price + bodylotion_cosmetic_price +facewash_cosmetic_price+handwash_cosmetic_price+foundation_cosmetic_price 
   
  cosmetic_price_entry.delete(0,END)
  
  cosmetic_price_entry.insert(0,f"{total_cosmetics_price} Rs") 
  
  #for cosmetics tax
  
  cosmetictax=total_cosmetics_price*0.08
  cosmetic_tax_entry.delete(0,END)
  cosmetic_tax_entry.insert(0,f'{cosmetictax} Rs')
  
  global rice_grocery_price,Daal_grocery_price,Wheat_grocery_price,sugar_grocery_price,masala_grocery_price,Oil_grocery_price
  # for grocery price in bill frame
   
  rice_grocery_price = int(Rice_entry.get())*50
  
  Daal_grocery_price = int(Daal_entry.get())*150
  
  Wheat_grocery_price = int(Wheat_entry.get())*25
  
  sugar_grocery_price = int(sugar_entry.get())*44
  
  masala_grocery_price = int(masala_entry.get())*200
  
  Oil_grocery_price = int(Oil_entry.get())*140  
  
  total_Grocery_price = rice_grocery_price + Daal_grocery_price + Wheat_grocery_price+sugar_grocery_price+masala_grocery_price+Oil_grocery_price
 
  grocery_price_entry.delete(0,END)
 
  grocery_price_entry.insert(0,f"{total_Grocery_price} Rs")
  
  # for grocery tax
  grocerytax=total_Grocery_price*0.08
  
  grocery_tax_entry.delete(0,END)
  
  grocery_tax_entry.insert(0,f'{grocerytax} Rs')
  
  global Tomato_vagetable_price,patato_vagetable_price,Onion_vagetable_price,lady_finger_vagetable_price,ceavage_vagetable_price,pumkin_vagetable_price
  # for vegatable price in bill frame 
  
  Tomato_vagetable_price =int(Tomato_entry.get())*20
  
  patato_vagetable_price =int(patato_entry.get())*20
  
  Onion_vagetable_price =int(Onion_entry.get())*20
  
  lady_finger_vagetable_price =int(lady_finger_entry.get())*60
  
  ceavage_vagetable_price =int(ceavage_entry.get())*40
  
  pumkin_vagetable_price =int(pumkin_entry.get())*20
  
  total_vegatable_price = Tomato_vagetable_price+patato_vagetable_price+Onion_vagetable_price+lady_finger_vagetable_price+ceavage_vagetable_price+pumkin_vagetable_price
  
  vagetable_price_entry.delete(0,END)
  
  vagetable_price_entry.insert(0,f'{total_vegatable_price} Rs')
  
  #for vagetable tax 
  vagetabletax=total_vegatable_price*0.08
  vagetable_tax_entry.delete(0,END)
  vagetable_tax_entry.insert(0,f'{vagetabletax} Rs')
  
  # for toatal bill
  global total_bill
  total_bill=total_cosmetics_price+total_Grocery_price+total_vegatable_price+cosmetictax+grocerytax+vagetabletax
  
    
# BILL (button) in bill frame 
  
def bill_fun(): 
  if name_entry.get()=='' or phone_entry.get()=='':
    messagebox.showerror('Error','Custumer details are required')
    
  elif cosmetic_price_entry.get()=='' and grocery_price_entry.get()== '' and vagetable_price_entry.get()=='':
      messagebox.showerror('Error','No Product are Selected ')
  
  elif cosmetic_price_entry.get()=='0 Rs' and grocery_price_entry.get()== '0 Rs' and vagetable_price_entry.get()=='0 Rs':
      messagebox.showerror('Error','No Product are Selected ')
  
  else:
    Text_area.delete(1.0,END)

    Text_area.insert (END,f"\t\t**WELLCOME CUSTOMER**\n")  
    Text_area.insert(END,f'\nBill Number : {billnumber}\n') 
    Text_area.insert(END,f'\nCustomer Name : {name_entry.get()}\n')
    Text_area.insert(END,f'\nCustomer Phone NO : {phone_entry.get()}\n') 
    Text_area.insert(END,f'\n=======================================================')
    Text_area.insert(END,f'\nProducts\t\t\tQuantity\t\t\tPrice')
    Text_area.insert(END,f'\n=======================================================\n')
    
    #for cosmetics
    if makeup_kit_entry.get()!='0':
      Text_area.insert(END,f'makeupkit\t\t\t{makeup_kit_entry.get()}\t\t\t{makeup_kit_cosmetic_price}Rs\n') 
    
    if facewash_entry.get()!='0':
      Text_area.insert(END,f'facewash\t\t\t{facewash_entry.get()}\t\t\t{facewash_cosmetic_price}Rs\n')  
    
    if bodylotion_entry.get()!='0':
      Text_area.insert(END,f'bodylotion\t\t\t{bodylotion_entry.get()}\t\t\t{bodylotion_cosmetic_price}Rs\n')
      
    if facecream_entry.get()!='0':
      Text_area.insert(END,f'facecream\t\t\t{facecream_entry.get()}\t\t\t{facecream_cosmetic_price}Rs\n')
      
    if handwash_entry.get()!='0':
      Text_area.insert(END,f'handwash\t\t\t{handwash_entry.get()}\t\t\t{handwash_cosmetic_price}Rs\n')
      
    if foundation_entry.get()!='0':
      Text_area.insert(END,f'foundation\t\t\t{foundation_entry.get()}\t\t\t{foundation_cosmetic_price}Rs\n')
    
    # for grocery
    if Rice_entry.get()!='0':
      Text_area.insert(END,f'Rice\t\t\t{Rice_entry.get()}\t\t\t{rice_grocery_price}Rs\n')
    
    if Daal_entry.get()!='0':
      Text_area.insert(END,f'Daal\t\t\t{Daal_entry.get()}\t\t\t{Daal_grocery_price}Rs\n')
    
    if Wheat_entry.get()!='0':
      Text_area.insert(END,f'Wheat\t\t\t{Wheat_entry.get()}\t\t\t{Wheat_grocery_price}Rs\n')
      
    if sugar_entry.get()!='0':
      Text_area.insert(END,f'sugar\t\t\t{sugar_entry.get()}\t\t\t{sugar_grocery_price}Rs\n')
      
    if masala_entry.get()!='0':
      Text_area.insert(END,f'masala\t\t\t{masala_entry.get()}\t\t\t{masala_grocery_price}Rs\n')
    
    if Oil_entry.get()!='0':
      Text_area.insert(END,f'Oil\t\t\t{Oil_entry.get()}\t\t\t{Oil_grocery_price}Rs\n')


  #for vagetables
    
    if Tomato_entry.get()!='0':
      Text_area.insert(END,f'Tomato\t\t\t{Tomato_entry.get()}\t\t\t{Tomato_vagetable_price}Rs\n')
    
    if patato_entry.get()!='0':
      Text_area.insert(END,f'Patato\t\t\t{patato_entry.get()}\t\t\t{patato_vagetable_price}Rs\n')
    
    if Onion_entry.get()!='0':
      Text_area.insert(END,f'Onion\t\t\t{Onion_entry.get()}\t\t\t{Onion_vagetable_price}Rs\n')
      
    if lady_finger_entry.get()!='0':
      Text_area.insert(END,f'Lady Finger\t\t\t{lady_finger_entry.get()}\t\t\t{lady_finger_vagetable_price}Rs\n')
      
    if ceavage_entry.get()!='0':
      Text_area.insert(END,f'Ceavage\t\t\t{ceavage_entry.get()}\t\t\t{ceavage_vagetable_price}Rs\n')
    
    if pumkin_entry.get()!='0':
      Text_area.insert(END,f'Pumkin\t\t\t{pumkin_entry.get()}\t\t\t{pumkin_vagetable_price}Rs\n')

    Text_area.insert(END,f'\n-------------------------------------------------------')
  
  #for tax price in fun 
  
    if cosmetic_tax_entry.get()!='0.0 Rs':
      Text_area.insert(END,f'\nCosmetic tax \t\t\t\t{cosmetic_tax_entry.get()}')
    
    if grocery_tax_entry.get()!='0.0 Rs':
      Text_area.insert(END,f'\nGrocery tax\t\t\t\t{grocery_tax_entry.get()}')
      
    if vagetable_tax_entry.get()!='0.0 Rs':
      Text_area.insert(END,f'\nVagetable tax\t\t\t\t{vagetable_tax_entry.get()}')    
      
    #for total bill 
    Text_area.insert(END,f'\n\nTotal Bill\t\t\t\t{total_bill}Rs') 
    Text_area.insert(END,f'\n=======================================================') 
      
    
    
                          
# gui particon.ico
 
root=Tk()
root.title('Retail Billing Software')
root.geometry("1270x685")
root.attributes('-fullscreen',True)
root.iconbitmap('icon.ico')

# heading label retail billing system
heading_label =Label(root,text="RETAIL BILLING SOFTWARE",font=('Times New Roman',30,'bold'),bg='grey20',fg='gold',bd=12,relief=GROOVE)
heading_label.pack(fill=X)

#custumer details label 
custumer_label_frame=LabelFrame(root,text='Customer Details',font=('Times New Roman',15,'bold'),bg='grey20',fg='gold',bd=8,relief=GROOVE)
custumer_label_frame.pack(fill=X)

#namelabel  in custumer details label
name_lebel=Label(custumer_label_frame,text='Name',font=('Times New Roman',15,'bold'),bg='grey20',fg='white')
name_lebel.grid(row=0,column=0,padx=20) 

#name entry in custumer details label
name_entry=Entry(custumer_label_frame,font=('arial',15),bd=7)
name_entry.grid(row=0,column=1,padx=8)

#pnonelabel  in custumer details label
phone_lebel=Label(custumer_label_frame,text='Phone Number',font=('Times New Roman',15,'bold'),bg='grey20',fg='white')
phone_lebel.grid(row=0,column=2,padx=20,pady=2) 

#phone entry in custumer details label
phone_entry=Entry(custumer_label_frame,font=('arial',15),bd=7)
phone_entry.grid(row=0,column=3,padx=10)

#billlabel  in custumer details label
bill_number_lebel=Label(custumer_label_frame,text='Bill Number',font=('Times New Roman',15,'bold'),bg='grey20',fg='white')
bill_number_lebel.grid(row=0,column=4,padx=20,pady=2) 

#entry in custumer details label
bill_number_entry=Entry(custumer_label_frame,font=('arial',15),bd=7)
bill_number_entry.grid(row=0,column=5,padx=8)

#search button custumer details label 
search_button=Button(custumer_label_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,command=search_bill_fun)
search_button.grid(row=0,column=6,padx=38,pady=8)

#PRODUCT FRAME 
product_frame =Frame(root)
product_frame.pack(fill=X)



#1 cosmectics frame in product frame
cosmetics_frame=LabelFrame(product_frame,text='COSMETICS',font=('Times New Roman',15,'bold'),bg='grey20',fg='gold',bd=8,)
cosmetics_frame.grid(row=0,column=0,) 


# cosmetics items

# 1 MAKEUP KIT in cosmetic frame

makeup_kit =Label(cosmetics_frame,text='makeup kit',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
makeup_kit.grid(row=0,column=0,pady=9)

# makeup_kit_entry entry box in cosmetic frame

makeup_kit_entry= Entry(cosmetics_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
makeup_kit_entry.grid(row=0,column=1,pady=9)
makeup_kit_entry.insert(0,0)

# 2 face wash in cosmetic frame

facewash =Label(cosmetics_frame,text='face wash',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
facewash.grid(row=1,column=0,pady=9)


# face wash entry box in cosmetic frame

facewash_entry= Entry(cosmetics_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
facewash_entry.grid(row=1,column=1,pady=9)
facewash_entry.insert(0,0)

# 1 bodylotion in cosmetic frame

bodylotion =Label(cosmetics_frame,text='bodylotion',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
bodylotion.grid(row=2,column=0,pady=9)

# bodylotion entry box in cosmetic frame

bodylotion_entry = Entry(cosmetics_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
bodylotion_entry.grid(row=2,column=1,pady=9)
bodylotion_entry.insert(0,0)

# 1 face cream in cosmetic frame

facecream =Label(cosmetics_frame,text='face cream',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
facecream.grid(row=3,column=0,pady=9)

# face cream entry box in cosmetic frame

facecream_entry = Entry(cosmetics_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
facecream_entry.grid(row=3,column=1,pady=9)
facecream_entry.insert(0,0)
# 5 handwash in cosmetic frame

handwash=Label(cosmetics_frame,text='hand wash',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
handwash.grid(row=4,column=0,pady=9)

# handwash entry box in cosmetic frame

handwash_entry = Entry(cosmetics_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
handwash_entry.grid(row=4,column=1,pady=9)
handwash_entry.insert(0,0)

# 5 foundation in cosmetic frame

foundation=Label(cosmetics_frame,text='Foundation',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
foundation.grid(row=5,column=0,pady=9)

# foundation entry box in cosmetic frame

foundation_entry = Entry(cosmetics_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
foundation_entry.grid(row=5,column=1,pady=9)
foundation_entry.insert(0,0)

# 2in (middle) Grocery frame in product frame
Grocery_frame=LabelFrame(product_frame,text='GROCERY',font=('Times New Roman',15,'bold'),bg='grey20',fg='gold',bd=8)
Grocery_frame.grid(row=0,column=1) 

#grocery items

# 1 RICE  in grocery items

Rice =Label(Grocery_frame,text='Rice',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
Rice.grid(row=0,column=0,pady=9)

# Rice entry box in grocery items

Rice_entry = Entry(Grocery_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
Rice_entry.grid(row=0,column=1,pady=9)
Rice_entry.insert(0,0)
#  face wash in grocery items

Daal =Label(Grocery_frame,text='Daal',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
Daal.grid(row=1,column=0,pady=9)

# face wash entry box in grocery items

Daal_entry = Entry(Grocery_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
Daal_entry.grid(row=1,column=1,pady=9)
Daal_entry.insert(0,0)
# Wheat in grocery items

Wheat=Label(Grocery_frame,text='Wheat',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
Wheat.grid(row=2,column=0,pady=9)

# Wheat entry box in grocery items

Wheat_entry = Entry(Grocery_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
Wheat_entry.grid(row=2,column=1,pady=9)
Wheat_entry.insert(0,0)

#  sugar in grocery items

sugar =Label(Grocery_frame,text='Sugar',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
sugar.grid(row=3,column=0,pady=9)

# suger entry box in grocery items

sugar_entry = Entry(Grocery_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
sugar_entry.grid(row=3,column=1,pady=9)
sugar_entry.insert(0,0)
# 5 masala in grocery items

masala=Label(Grocery_frame,text='masala',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
masala.grid(row=4,column=0,pady=9)

# masala entry box in grocery items

masala_entry = Entry(Grocery_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
masala_entry.grid(row=4,column=1,pady=9)
masala_entry.insert(0,0)


# 5 Oil in grocery items

Oil=Label(Grocery_frame,text='Oil',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
Oil.grid(row=5,column=0,pady=9)

#Oil entry box in grocery items

Oil_entry = Entry(Grocery_frame,font=('Times New Roman',15,'bold'),width=10,bd=5)
Oil_entry.grid(row=5,column=1,pady=9)
Oil_entry.insert(0,0)


#vagetables frame in product frame

vagetables_frame=LabelFrame(product_frame,text='VAGETABLES',font=('Times New Roman',15,'bold'),bg='grey20',fg='gold',bd=8)
vagetables_frame.grid(row=0,column=2) 

# Vagetables items

# 1 tomato in vagetables frame

Tomato =Label(vagetables_frame,text='Tomato',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
Tomato.grid(row=0,column=0,pady=9)

# Tomato entry box in vagetables frame

Tomato_entry = Entry(vagetables_frame,font=('Times New Roman',15,'bold'),width=11,bd=5)
Tomato_entry.grid(row=0,column=1,pady=9)
Tomato_entry.insert(0,0)

# 2 patato in vagetables frame

patato =Label(vagetables_frame,text='Potato',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
patato.grid(row=1,column=0,pady=9)

# patato entry box in vagetables frame

patato_entry= Entry(vagetables_frame,font=('Times New Roman',15,'bold'),width=11,bd=5)
patato_entry.grid(row=1,column=1,pady=9)
patato_entry.insert(0,0)

# 3 Onion in vagetables frame

Onion =Label(vagetables_frame,text='Onion',font=('Times New Roman',15,'bold'),
                 bg='grey20',fg='white')
Onion.grid(row=2,column=0,pady=9)

# Onion entry box in vagetables frame

Onion_entry = Entry(vagetables_frame,font=('newtimes roman',15,'bold'),width=10,bd=5)
Onion_entry.grid(row=2,column=1,pady=9)
Onion_entry.insert(0,0)
# 1 lady finger in vagetables frame

lady_finger=Label(vagetables_frame,text='Ladyfinger',font=('newtimes roman',15,'bold'),
                 bg='grey20',fg='white')
lady_finger.grid(row=3,column=0,pady=9)

# lady finger entry box in vagetables frame

lady_finger_entry = Entry(vagetables_frame,font=('newtimes roman',15,'bold'),width=10,bd=5)
lady_finger_entry.grid(row=3,column=1,pady=9)
lady_finger_entry.insert(0,0)
# 5 ceavage in vagetables frame

ceavage=Label(vagetables_frame,text='Cavage',font=('newtimes roman',15,'bold'),
                 bg='grey20',fg='white')
ceavage.grid(row=4,column=0,pady=9)

# ceavage entry box in vagetables frame

ceavage_entry = Entry(vagetables_frame,font=('newtimes roman',15,'bold'),width=10,bd=5)
ceavage_entry.grid(row=4,column=1,pady=9)
ceavage_entry.insert(0,0)

# 5 pumkin in vagetables frame

pumkin=Label(vagetables_frame,text='Pumkin',font=('newtimes roman',15,'bold'),
                 bg='grey20',fg='white')
pumkin.grid(row=5,column=0,pady=9)

#pumkin entry box in vagetables frame

pumkin_entry = Entry(vagetables_frame,font=('newtimes roman',15,'bold'),width=10,bd=5)
pumkin_entry.grid(row=5,column=1,pady=9)
pumkin_entry.insert(0,0)
#bill frame in product frame 

Bill_frame =Frame(product_frame,bd=8,relief=GROOVE)
Bill_frame.grid(row=0,column=3,padx=10)

#bill area label in bill frame  

bill_area_label = Label(Bill_frame,text="Bill Area",font=('newtimes roman',15,'bold'),bd=6,relief=GROOVE,bg="grey20",fg='gold')
bill_area_label.pack(fill=X)


#scrollbar in text area

scrollbar =Scrollbar(Bill_frame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

#text area in bill frame

Text_area =Text(Bill_frame,height=18,width=55,yscrollcommand=scrollbar.set)
Text_area.pack(padx=20)
scrollbar.config(command=Text_area.yview)


# side button of product frame

sidebutton_frame =Frame(product_frame,bd=8,relief=GROOVE)
sidebutton_frame.grid(row=0,column=4)

# send Lebel

send_lebel=Label(sidebutton_frame,text="Send",font=('times new roman',20,"bold"),bg='grey20',fg="gold",bd=7,relief=GROOVE)
send_lebel.grid(row=0,column=0,pady=30)
# pnone send button 
phone_BUtton =Button(sidebutton_frame,text="Phone",font=('times new roman',14,'bold'),bg="grey20",bd=5,relief=GROOVE,fg="white",width=10,command=phone_fun)
phone_BUtton.grid(row=1,column=0,pady=20)

# Email send button 
email_BUtton =Button(sidebutton_frame,text="Email",font=('times new roman',14,'bold'),bg="grey20",bd=5,relief=GROOVE,fg="white",width=10,command=email_fun)
email_BUtton.grid(row=2,column=0,pady=20)

# print send button 
print_BUtton =Button(sidebutton_frame,text="Print",font=('times new roman',14,'bold'),bg="grey20",bd=5,relief=GROOVE,fg="white",width=10,command=print_button_fun)
print_BUtton.grid(row=3,column=0,pady=20)


#billmanu frame
billmanu_frame =LabelFrame(root,text="Bill menu",font=('times new roman',15,"bold"),bd=8,bg='grey20',fg="gold",relief=GROOVE)
billmanu_frame.pack(fill=X,padx=14)

#bill manu items

#cosmetic price in billmanu frame
 
cosmetic_price_label =Label(billmanu_frame,text="cosmetic price",font=('times new roman',15,'bold'),bg='grey20',fg='white',)
cosmetic_price_label.grid(row=0,column=0,sticky='w')

#cosmetic price entry in billmanu frame 

cosmetic_price_entry =Entry(billmanu_frame,font=('times new roman',15,'bold'),bd=5,relief=GROOVE,width=10)
cosmetic_price_entry.grid(row=0,column=1,pady=2,padx=10)

#grocery price in billmanu frame

grocery_price_frame=Label(billmanu_frame,text="grocery price",font=('times new roman',15,"bold"),bg='grey20',fg='white')
grocery_price_frame.grid(row=1,column=0,sticky='w')

#grocery price entry in bill manu frame

grocery_price_entry=Entry(billmanu_frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,width=10)
grocery_price_entry.grid(row=1,column=1,pady=2,padx=10)

#vegatable price in bill manu frame 

vagetable_price_label=Label(billmanu_frame,text='vagetable price',font=('times new roman',15,'bold'),fg='white',bg='grey20')
vagetable_price_label.grid(row=2,column=0,sticky='w')

#vagetable price entry in bill manu frame 

vagetable_price_entry =Entry(billmanu_frame,font=('times new roman',15,'bold'),bd=5,relief=GROOVE,width=10)
vagetable_price_entry.grid(row=2,column=1,pady=2,padx=10)


#cosmetic tax in billmanu frame
 
cosmetic_tax_label =Label(billmanu_frame,text="cosmetic Tax",font=('times new roman',15,'bold'),bg='grey20',fg='white',)
cosmetic_tax_label.grid(row=0,column=2,sticky='w')

#cosmetic tax entry in billmanu frame 

cosmetic_tax_entry =Entry(billmanu_frame,font=('times new roman',15,'bold'),bd=5,relief=GROOVE,width=10)
cosmetic_tax_entry.grid(row=0,column=3,pady=2,padx=10)

#grocery tax in billmanu frame

grocery_tax_frame=Label(billmanu_frame,text="grocery tax",font=('times new roman',15,"bold"),bg='grey20',fg='white')
grocery_tax_frame.grid(row=1,column=2,sticky='w')

#grocery tax entry in bill manu frame

grocery_tax_entry=Entry(billmanu_frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,width=10)
grocery_tax_entry.grid(row=1,column=3,pady=2,padx=10)

#vegatable tax in bill manu frame 

vagetable_tax_label=Label(billmanu_frame,text='vagetable tax',font=('times new roman',15,'bold'),fg='white',bg='grey20')
vagetable_tax_label.grid(row=2,column=2,sticky='w')

#vagetable price entry in bill manu frame 

vagetable_tax_entry =Entry(billmanu_frame,font=('times new roman',15,'bold'),bd=5,relief=GROOVE,width=10)
vagetable_tax_entry.grid(row=2,column=3,pady=2,padx=10)

#buton in bill manu frame 

button_frame=Frame(billmanu_frame,bd=8,relief=GROOVE)
button_frame.grid(row=0,column=4,rowspan=3,padx=10)

# Total button 

total_button=Button(button_frame,text="Total",font=('arial',14,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10,command=total)
total_button.grid(row=0,column=0,padx=10,pady=20)

# bill button
 
bill_button=Button(button_frame,text="Bill",font=('arial',14,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10,command=bill_fun)
bill_button.grid(row=0,column=1,padx=9,pady=20)

# reset button
 
Reset_button=Button(button_frame,text="Reset",font=('arial',14,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10)
Reset_button.grid(row=0,column=2,padx=9,pady=20)

# Clear button 
clear_button=Button(button_frame,text="Clear",font=('arial',14,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10,command=clear_fun)
clear_button.grid(row=0,column=3,padx=9,pady=20)

# Save button 
save_button=Button(button_frame,text="Save",font=('arial',14,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10,command=Save)
save_button.grid(row=0,column=4,padx=9,pady=20)

# EXIT button 
exit_button=Button(button_frame,text="Exit",font=('arial',14,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=10,command=exit_fun)
exit_button.grid(row=0,column=5,padx=10,pady=20)

root.mainloop()