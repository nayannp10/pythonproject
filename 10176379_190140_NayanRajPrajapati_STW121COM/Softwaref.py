"""importing tkinter"""
from tkinter import*
from tkinter import ttk,messagebox
"""importing os"""
import os
"""defining class Fileapp"""
class Fileapp:
    """this function is made for window of Employment management system"""
    def __init__(self):
        self.root=Tk()
        self.root.title("Employment Management System")
        """I have fixed height and width of window"""
        self.root.geometry("1500x600+1+1")
        """Giving name to the title of tkinter window """
        title=Label(self.root,text="Employment Management System",pady=9, font=("Cambria",34,"bold"),bd=9,relief=GROOVE,fg="Dark blue",bg="Light blue").pack(fill=X)
        """creating frame for Employment Management System and giving some font styles, size, etc"""
        employeeframe=Frame(self.root,bd=12,relief=GROOVE,bg="light blue")
        employeeframe.place(x=20,y=100,width=1120)
        """labeling and creating entry form for all the important fields"""
        title_emp=Label(employeeframe,text="Employee Details  :",font=("Cambria",22,"bold"),fg="Dark blue").grid(row=0,column=0,pady=18)
        #=All variables
        self.empid=StringVar()
        self.name=StringVar()
        self.gender=StringVar()
        self.add=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.dept=StringVar()
        self.age=StringVar()

        title_empID= Label(employeeframe, text="Employee ID :", font=("Cambria", 18, "bold")).grid(row=1, column=0,padx=18,sticky="w")
        txt_empID= Entry(employeeframe,textvariable=self.empid,bd=10,relief=GROOVE,width=21,font="Arial 16 bold").grid(row=1,column=1,pady=10)

        title_empname= Label(employeeframe, text="Employee Name :", font=("Cambria", 18, "bold")).grid(row=2, column=0,padx=18,sticky="w")
        txt_empname= Entry(employeeframe,textvariable=self.name,bd=10,relief=GROOVE,width=21,font="Arial 16 bold").grid(row=2,column=1,pady=10)

        title_empadd = Label(employeeframe, text="Address :", font=("Cambria", 18, "bold")).grid(row=3, column=0,padx=18, sticky="w")
        txt_empadd = Entry(employeeframe, textvariable=self.add, bd=10, relief=GROOVE, width=21,font="Arial 16 bold").grid(row=3, column=1, pady=10)

        title_empage= Label(employeeframe, text="Age :", font=("Cambria", 18, "bold")).grid(row=4, column=0,padx=18, sticky="w")
        txt_empage = Entry(employeeframe, textvariable=self.age, bd=10, relief=GROOVE, width=21,font="Arial 16 bold").grid(row=4, column=1, pady=10)

        title_empcont = Label(employeeframe, text="Contact no. :", font=("Cambria", 18, "bold")).grid(row=1,column=2,padx=18,sticky="w")
        txt_empcont = Entry(employeeframe, textvariable=self.contact, bd=10, relief=GROOVE, width=21, font="Arial 16 bold").grid(row=1, column=3,pady=10)

        title_empdate = Label(employeeframe, text="DOB(DD/MM/YYYY) :", font=("Cambria", 18, "bold")).grid(row=2, column=2,padx=18,sticky="w")
        txt_empdate = Entry(employeeframe,textvariable=self.date,bd=10, relief=GROOVE, width=21, font="Arial 16 bold").grid(row=2, column=3,pady=10)


        title_empgender = Label(employeeframe, text="Gender :", font=("Cambria", 18, "bold")).grid(row=3,column=2,padx=18,sticky="w")

        title_dept = Label(employeeframe, text="Department :", font=("Cambria", 18, "bold")).grid(row=4,column=2,padx=18,sticky="w")
        """I have used combobox for Gender and Department"""
        gendercombo = ttk.Combobox(employeeframe,width=18,textvariable=self.gender)
        gendercombo['values']=("Male","Female","Others")
        gendercombo.place(x=815,y=230)

        deptcombo = ttk.Combobox(employeeframe, width=18,textvariable=self.dept)
        deptcombo['values'] = ("Operation","Faculty","Admin","Exam","IT")
        deptcombo.place(x=815, y=297)
        """Fixing button frames"""
        btnframe=Frame(self.root, bd=9,relief=GROOVE,bg="light blue")
        btnframe.place(x=225,y=490)
        """Fixing buttons in button frame they are save, delete, exit"""
        btnsave=Button(btnframe,text="Save",font="Cambria 15 bold",bd=8,width=15,command=self.savedata).grid(row=0,column=0,padx=10,pady=9)
        btdelete = Button(btnframe, text="Delete", font="Cambria 15 bold", bd=8, width=15,command=self.delete).grid(row=0, column=2, padx=10,pady=9)
        btnback = Button(btnframe, text="Exit", font="Cambria 15 bold", bd=8, width=15,command=self.exit).grid(row=0, column=3, padx=10,pady=9)
        """Creating File frame to view saved files"""
        Fileframe=Frame(self.root,bd=11,relief=GROOVE)
        Fileframe.place(x=1161,y=100,width=320,height=477)
        """Code below is done for the File Frame and for scroll bar in File frame"""
        filetitle=Label(Fileframe,text="Files",font="Cambria 18 bold",bd=6,relief=SUNKEN).pack(side=TOP,fill=X)
        scroll_y=Scrollbar(Fileframe,orient=VERTICAL)
        self.file_list=Listbox(Fileframe,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>", self.getdata)
        self.showfiles()
        self.root.mainloop()
    """Creating function to save data in .txt file"""
    def savedata(self):
        if self.empid.get()=="":
            messagebox.showerror("Error","ID no. must be filled !!")
        elif self.name.get()=="":
            messagebox.showerror("Error","Name must be filled !!")
        elif self.age.get()=="":
            messagebox.showerror("Error","Age must be included")
        elif self.gender.get()=="":
            messagebox.showerror("Error", "Gender must be mentioned")
        elif self.dept.get()=="":
            messagebox.showerror("Error","Departmant must be filled !!!")
        elif self.contact.get()=="":
            messagebox.showerror("Error","Contact should be given")
        elif self.date.get()=="":
            messagebox.showerror("Error", "DOB must be filled !!")
        else:
            g=open("files/"+str(self.empid.get())+".txt","w")
            g.write(
                    str(self.empid.get())+","+
                    str(self.add.get()) + "," +
                    str(self.age.get()) + "," +
                    str(self.dept.get()) + "," +
                    str(self.gender.get()) + "," +
                    str(self.contact.get()) + "," +
                    str(self.date.get()) + "," +
                    str(self.name.get())
                    )
            g.close()
            messagebox.showinfo("Successful","Your data has been saved")
            self.showfiles()
    """Creating function to show files in File frame which i have mentioned above"""
    def showfiles(self):
        files=os.listdir("files/")
        self.file_list.delete(0, END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END,i)
    """Creating function to show data in the entry field after clicking the files shown in File frame"""
    def getdata(self,e):
        get_cursor=self.file_list.curselection()
        print(self.file_list.get(get_cursor))
        g1=open("files/"+self.file_list.get(get_cursor))
        value=[]
        for g in g1:
            value=g.split(",")
        """Indexing saved information in entry field"""
        self.empid.set(value[0])
        self.name.set(value[1])
        self.gender.set(value[2])
        self.add.set(value[3])
        self.contact.set(value[4])
        self.date.set(value[5])
        self.dept.set(value[6])
        self.age.set(value[7])

    """creating function for deleting files of saved .txt files"""
    def delete(self):
        present="no"
        if self.empid.get()=="":
            messagebox.showerror("Error","Student ID must be Required!!")
        else:
            g =os.listdir("files/")
            if len(g)>0:
                for i in g:
                    if i.split(".")[0]==self.empid.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Delete","Do you really want to delete?")
                    if ask>0:
                        os.remove("files/"+self.empid.get()+".txt")
                        messagebox.showinfo("Successful","Successfully Deleted")
                        self.showfiles()
                else:
                    messagebox.showinfo("Error","File not found!!")
    """creating function for exit button to quit the page"""
    def exit(self):
        ask=messagebox.askyesno("Exit","Do you really want to exit?")
        if ask>0:
            self.root.destroy()

