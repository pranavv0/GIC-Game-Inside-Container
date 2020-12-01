from tkinter import *
import hashlib
import os
import dash



"""def dashboard():
	screen3 = Toplevel(screen1)  
	screen3.geometry('1080x720')  
	screen3.title('Dashboard  | GIC  | Gaming Inside Container')

	Label(screen3, text = "Wecome to GIC  Gaming Inside Container: Dashboard", fg="white" , bg = "darkred", width = "1080", height = "3", font = ( "Calibri", 16)).pack()
	Label(text = "").pack()
	Label(screen3, text = "Here is some of the awesome games of windows running inside linux containner" , font = ( "Calibri", 12)).pack()
	Label(screen3, text = "").pack()
	
	Label(screen3, text="Counter Strike 1.6", fg="white" , bg = "darkred", font = ( "Calibri", 12)).place(x=20, y=30)
	Label(screen3, text="Solitaire", fg="white" , bg = "darkred", font = ( "Calibri", 12)).place(x=20, y=60)
	Label(screen3, text="Minecraft", fg="white" , bg = "darkred", font = ( "Calibri", 12)).place(x=20, y=90)


"""	

def login_verify():
	u1 = username_v.get()
	#print(u1)
	
	p1 = key_v.get()
	#print(p1)
	p1 = hashlib.sha512(p1.encode(encoding='ascii')).hexdigest()
	#print(p1)
	username_ventry1.delete(0, END)
	key_ventry1.delete(0, END)


	file = open('accounts.txt','r')
	accounts = file.read().split('\n')
	file.close()
	del accounts[-1]
	for acc in accounts:
		details = acc.split('/')
		if details[0] == u1 and details[1] == p1:
			print("Loggin success")
			dash.dashboard()
	else:
		print("key incorrect")
			
        
"""
/* 
	list_of_files=os.listdir()
	if u1 in list_of_files:
		file1 = open(u1,'r')
		verify=file1.read().splitlines()
		if p1 in verify:
			print("logged")
			#dashboard()
			#screen2.destroy()
		else:
			print("password not found")
	else:
		mainApp() 
    
*/
"""





def login():
    global screen2
    
    screen2 = Toplevel(screen1)
    screen2.geometry('1080x720')  
    screen2.title('Login  | GIC  | Gaming Inside Container')
    Label(screen2, text = "Wecome to GIC  Gaming Inside Container", fg="white" , bg = "darkred", width = "1080", height = "3", font = ( "Calibri", 16)).pack()
    Label(text = "").pack()
    

    Label(screen2, text = "Please enter details below to verify" , font = ( "Calibri", 12)).pack()
    Label(screen2, text = "").pack()
    
    global  username_v 
    global  key_v
    global username_ventry1
    global key_ventry1
    username_v = StringVar()
    key_v = StringVar()
       
    Label(screen2, text = "Username * ").pack()
    username_ventry1 = Entry(screen2, textvariable = username_v, width = 30)
    username_ventry1.pack()
    Label(screen2, text = "Key * ").pack()
    key_ventry1 = Entry(screen2, textvariable = key_v, width = 30)
    key_ventry1.pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
    


def register_user():
    username_info = username.get()
    password_info = key.get()
    password_info = hashlib.sha512(password_info.encode(encoding='ascii')).hexdigest()
    email_info = email.get()

    file = open("accounts.txt","a")
    file.write(username_info+ "/")
    file.write(password_info+ "/")
    file.write(email_info+ "\n")
    file.close()

    username_entry.delete(0, END)
    key_entry.delete(0, END)
    email_entry.delete(0, END)
     



def mainApp():
	global screen1
	global username
	global key
	global email
	global email_entry
	global username_entry
	global key_entry
	
	screen1 = Tk()  
	screen1.geometry('1080x720')  
	screen1.title('GIC  | Gaming Inside Container')

	Label(text = "Wecome to GIC  Gaming Inside Container", fg="white" , bg = "darkred", width = "1080", height = "3", font = ( "Calibri", 16)).pack()
	Label(text = "").pack()



	Label(text = "Please help us by registering yourself before you begin Gaming or verify if you already registered", font = ( "Calibri", 12)).pack()
	
    
	username = StringVar()
	email= StringVar()
	key = StringVar()
    
	Label(screen1, text = "").pack()
	Label(screen1, text = "Username * ").pack()
	username_entry = Entry(screen1, textvariable = username, width = 30)
	username_entry.pack()
	Label(screen1, text = "Email * ").pack()
	email_entry = Entry(screen1, textvariable = email, width = 30)
	email_entry.pack()
	Label(screen1, text = "Secret key * ").pack()
	key_entry = Entry(screen1, textvariable = key, width = 30)
	key_entry.pack()
	Label(screen1, text = "").pack()
	Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

	Button(screen1, text = "Login", width = 10, height = 1, command = login).pack()

	screen1.mainloop()



mainApp() 
