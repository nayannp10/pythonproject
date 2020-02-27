"""Imporing tkinter"""
from tkinter import*
from tkinter import messagebox
"""Importing os"""
import os
"""defining class"""
class Login:
    """this function is made for the window of tkinter"""
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        """I have fixed height and width of window"""
        self.root.geometry("1260x720+1+1")
        """I have made frame inside the window for login sysytem"""
        f1=Frame(self.root,bd=9,relief=RIDGE, bg="light blue")
        f1.place(x=320, y=200, height=295, width=600)
        """variables set"""
        self.username=StringVar()
        self.password=StringVar()
        """title inside the frame"""
        title=Label(f1,text="Login System:",font=("Arial",28,"bold"),fg="light blue", bg="dark blue").grid(row=0,column=2, pady= 8)
        """setting Label and Entry field for username and passcode"""
        lbusername = Label(f1, text="Username:", font=("Arial", 18, "bold"), fg="blue").grid(row=2, column=1, padx=14, pady= 15)
        txtusername = Entry(f1,bd=8, textvariable=self.username, relief=SUNKEN,width=35,font=("calibri 14")).place(x=170,y=80)

        lbpasscode = Label(f1, text="Passcode:", font=("Arial", 18, "bold"), fg="blue").grid(row=3, column=1, padx=14,pady=15)
        txtpasscode = Entry(f1, bd=8, textvariable=self.password, relief=SUNKEN,show="#",width=35, font=("calibri 14")).place(x=170,y=140)
        """Placement of Buttons they are Login, Exit, Register"""
        btnlog = Button(f1,text="Login", font = ("arial",16, "bold"),bd=8, width=10, command=self.loginfun).place(x=50,y=210)
        btnexit = Button(f1, text="Exit", font=("arial", 16, "bold"), bd=8, width=10, command=self.exitfunc).place(x=390, y=210)
        btnregister =  Button(f1, text="Register", font=("arial", 16, "bold"), command = self.register, bd=8, width=10).place(x=220, y=210)
    """setting function for login button"""
    def loginfun(self):
        empty = ["", " "]
        username_input = self.username.get()
        password_input = self.password.get()
        if username_input in empty or password_input in empty:
            Login.not_filled(self)
        else:
            list_of_files = os.listdir()
            if username_input + ".txt" in list_of_files:
                filetrp = open(username_input + ".txt", "r")
                if password_input in filetrp:
                    self.root.destroy()
                    import Softwaref
                    Softwaref.Fileapp()
                else:
                    messagebox.showerror("Wrong password","Password is incorrect")
            else:
                messagebox.showerror("Error","Invalid username or password")
    """setting function for exit button"""
    def exitfunc(self):
        lastop=messagebox.askyesno("Exit","Do you want to exit ?")
        if lastop > 0:
            self.root.destroy()
        else:
            return
    """setting function for register button"""
    def register(self):
        empty = [""," "]
        username_input = self.username.get()
        password_input = self.password.get()
        if username_input in empty or password_input in empty:
            Login.not_fill(self)
        else:
            try:
                file = open(str(username_input) + ".txt", "x")
            except FileExistsError:
                Login.user_exist(self)
            else:
                file.write(username_input + "\n")
                file.write(password_input)
                file.close()
                messagebox.showinfo("Registered", "Your file has been saved")

    """arranging messagebox for the above entry field"""
    def user_exist(self):
        messagebox.showerror("User Exist", "User already exist")
    def not_fill(self):
        messagebox.showerror("Not Filled", "Username or Password must be filled")
    def not_filled(self):
        messagebox.showerror("Not Filled", "Username or Password must be filled")
root=Tk()
"""Calling class Login(root)"""
ob = Login(root)
root.mainloop()