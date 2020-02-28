from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle
class Employee_management_system:
    def __init__(self):
        '''Function to create class constructor method :param window: Main window of an application'''
        self.general_font = "-family Ubuntu -size 11 -weight bold"
        self.slogan_font = "-family {Source Code Variable} -size 11 -weight normal"
        self.title_font = "-family {Viner Hand ITC} -size 24 -weight normal -slant italic"
        self.window = Tk()
        self.window.attributes("-a", 0.97)  # transparency level
        self.window.geometry("821x514+264+46")
        self.window.resizable(0, 0)  # unbale to resize
        self.window.iconbitmap("download.ico")  # putting a different icon in the tkinter
        self.window.title("Employee Management System")
        self.window.configure(background="#50D0B3")
        self.mainframe = Frame(self.window, bd="2", bg="#50D0B3")
        self.mainframe.place(relx=0.004, rely=0.008, relheight=0.982, relwidth=0.993)
        self.title_label = Label(self.mainframe, bg="#50D0B3", font=self.title_font, text="Employee Management system")
        self.title_label.place(relx=0.012, rely=0.02, height=57, width=795)
        self.cursor = []
        try:
            f = open("register.txt", "rb")
            pickle.load(f)
            self.indication = 1  # indicating if file has some then file opens login
            self.loggingin_interface()
        except Exception:
            self.indication = 0  # otherwise file opens registration
            self.registration()

    def loggingin_interface(self):
        """The main design of login interface is here where frames are created and kept accordingly. :return : None"""
        self.loginframe1 = Frame(self.mainframe, bd="2", bg="#50D0B3")
        self.loginframe1.place(relx=0.015, rely=0.143, relheight=0.842, relwidth=0.975)
        self.loginpage_frame = Frame(self.loginframe1, bd="2", bg="#50D0B3")
        self.loginpage_frame.place(relx=0.497, rely=0.009, relheight=0.976, relwidth=0.497)
        icon = PhotoImage(file="icon.png")
        self.usericon_lbl = Label(self.loginpage_frame, image=icon, bg="#50D0B3")
        self.usericon_lbl.place(relx=0.314, rely=0.036, height=166, width=176)
        self.login_btn = ttk.Button(self.loginpage_frame, text="Login", command=self.Validation)
        self.login_btn.place(relx=0.423, rely=0.805, height=34, width=124)
        self.enter_username = ttk.Entry(self.loginpage_frame)
        self.enter_username.place(relx=0.362, rely=0.518, relheight=0.065, relwidth=0.542)
        self.enter_username.focus()  # focusing on the username
        self.enter_password = ttk.Entry(self.loginpage_frame, show="*")
        self.enter_password.place(relx=0.365, rely=0.619, relheight=0.065, relwidth=0.542)
        self.username1 = Label(self.loginpage_frame, text="Username :", font=self.general_font, bg="#50D0B3")
        self.username1.place(relx=0.081, rely=0.52, height=27, width=95)
        self.password1 = Label(self.loginpage_frame, bg="#50D0B3", text="Password:", font=self.general_font)
        self.password1.place(relx=0.084, rely=0.614, height=27, width=95)
        self.popuphelp = Label(self.loginpage_frame, text="Problem while logging \n in?", bg="#50D0B3", cursor="hand2")
        self.popuphelp.place(relx=0.666, rely=0.718, height=30, width=125)
        self.popuphelp.bind("<Button-1>", self.helptologin)
        image = PhotoImage(file="sidepic.png")
        self.sidewal = Label(self.loginframe1, image=image, bg="#50D0B3")
        self.sidewal.place(relx=0.018, rely=0.08, height=339, width=358)
        self.slogan = Label(self.loginframe1, text="We appreciate your Hard works.", bg="#50D0B3", font=self.slogan_font)
        self.slogan.place(relx=0.026, rely=0.887, height=37, width=355)
        self.window.mainloop()

    def helptologin(self, *args):
        """"The help window generally shows the way to login :return None"""
        messagebox.showinfo("Help Window", "Please contact the system admin Arya Pokharel.")

    def Validation(self):
        """
        Validation to different information inserted by the user. Firstly a dictionary is created and the dictionary is
        updated. Secondly the info provided was checked which was by the user during registration :return None
        """
        self.user_get = str(self.enter_username.get())
        b = str(self.enter_password.get())
        data_load = open("register.txt", "rb")
        test = pickle.load(data_load)
        authentication = {}
        for i in test:
            username = i["username"]
            password = i["password"]
            authentication.update({username: password})
        usrs = []
        for i in authentication:
            usrs.append(i.upper())
        if self.user_get.upper() in usrs:
            if authentication[self.user_get.upper()] == b:
                self.first_login_intrfc()
            else:
                messagebox.showinfo("Error", "Enter the correct password")
                self.enter_password.delete(0, END)
                self.enter_password.focus()
        else:
            messagebox.showerror("Error", "Please provide the right username")
            self.enter_username.delete(0, END)
            self.enter_password.delete(0, END)
            self.enter_username.focus()

    def registration(self):
        """Function that registers the user. :return None"""
        font10 = "-family P052 -size 12 -weight bold"
        font13 = "-family {Source Code Pro} -size 12"
        font9 = "-family {Source Code Pro} -size 14 -weight bold"
        self.registration_frame = Frame(self.mainframe, bg="#50D0B3", bd=2)
        self.registration_frame.place(relx=0.010, rely=0.150, relheight=0.830, relwidth=0.981)
        if self.indication == 1:
            self.btn = Button(self.registration_frame, text="Back", bg="#50D0B3", command=self.back_reg)
            self.btn.place(relx=0.02, rely=0.893, height=30, width=50)
        else:
            pass
        self.Separator_vertical = ttk.Separator(self.registration_frame, orient="vertical")
        self.Separator_vertical.place(relx=0.489, rely=0.015, relheight=0.962)
        self.usr_reg_title = Label(self.registration_frame, bg="#50D0B3", font=font9, text="User Registration")
        self.usr_reg_title.place(relx=0.022, rely=0.03, height=47, width=355)
        self.Separator_horizontal = ttk.Separator(self.registration_frame)
        self.Separator_horizontal.place(relx=0.011, rely=0.863, relwidth=0.969)
        self.name_lbl = Label(self.registration_frame, font=font10, bg="#50D0B3", text="Name :")
        self.name_lbl.place(relx=0.034, rely=0.218, height=27, width=75)
        self.name_ent = Entry(self.registration_frame)
        self.name_ent.place(relx=0.133, rely=0.215, height=29, relwidth=0.293)
        self.mobile_lbl_reg = Label(self.registration_frame, bg="#50D0B3", text="Number :", font=font10)
        self.mobile_lbl_reg.place(relx=0.020, rely=0.337, height=27, width=85)
        self.test = StringVar()  # checking valid information for this entry
        self.mobile_ent = Entry(self.registration_frame, textvariable=self.test)
        self.mobile_ent.place(relx=0.135, rely=0.334, height=29, relwidth=0.293)
        self.test.trace_variable("w", self.input_validation)
        self.username_lbl_reg = Label(self.registration_frame, font=font10, bg='#50D0B3', text="Username :")
        self.username_lbl_reg.place(relx=0.020, rely=0.456, height=27, width=90)
        self.enter_username_reg = Entry(self.registration_frame)
        self.enter_username_reg.place(relx=0.138, rely=0.456, height=29, relwidth=0.293)
        self.pass_lbl = Label(self.registration_frame, text="Password :", bg="#50D0B3", font=font10)
        self.pass_lbl.place(relx=0.014, rely=0.58, height=27, width=95)
        self.pass_ent = Entry(self.registration_frame, show='*')
        self.pass_ent.place(relx=0.138, rely=0.58, height=29, relwidth=0.293)
        self.pass_confirm_lbl = Label(self.registration_frame, bg="#50D0B3", text="Confirm :", font=font10)
        self.pass_confirm_lbl.place(relx=0.01, rely=0.696, height=27, width=95)
        self.pass_confirm_ent = Entry(self.registration_frame, show="*")
        self.pass_confirm_ent.place(relx=0.139, rely=0.696, height=29, relwidth=0.293)
        self.register_btn = Button(self.registration_frame, text="Register", bg="#50D0B3",
                                   command=self.validation_regis)
        self.register_btn.place(relx=0.183, rely=0.891, height=37, width=123)
        image = PhotoImage(file="regwal.png")
        self.wallpaper = Label(self.registration_frame, image=image, bg="#50D0B3")
        self.wallpaper.place(relx=0.497, rely=0.025, height=327, width=385)
        self.slogan_reg = Label(self.registration_frame, bg="#50D0B3", font=font13, text="Employees are precious.")
        self.slogan_reg.place(relx=0.509, rely=0.901, height=27, width=375)
        self.window.mainloop()

    def validation_regis(self):
        """Function which validates the information of users in registration and stores only it if it is correct.
        :return: None"""
        a = self.name_ent.get()
        b = self.mobile_ent.get()
        c = self.enter_username_reg.get()
        d = self.pass_ent.get()
        e = self.pass_confirm_ent.get()
        blank = [a.strip(), b.strip(), c.strip(), d.strip(), e.strip()]  # no blank spaces allowed
        try:
            load1 = open("register.txt", "rb")
            test = pickle.load(load1)
            self.users = []
            if test != []:
                for i in test:
                    self.users.append(i["username"])
        except Exception:
            self.users = []

        if c.upper() in self.users:
            messagebox.showinfo("Error", f"User {c} already exist")
        elif "" in blank:
            messagebox.showerror("Error", "You must provide all the credentials")
        elif len(c) < 5 or len(c) > 15:
            messagebox.showerror("Error", "Username must be between 5 - 15 in length.")
        elif len(b) < 10:
            messagebox.showerror("Error", "Wrong Phone Number , Please Provide correct number")
        elif len(d) < 5 or len(d) > 30:
            messagebox.showerror("Error", "Password must be between 5 - 30 in length")
        elif d != e:
            messagebox.showerror("Error", "Password do not match !")
        else:
            if self.indication == 0:
                test = open("register.txt", "wb+")
                pickle.dump([], test)
            test = open("register.txt", "rb")
            data = pickle.load(test)
            file = {"name": a.upper(), "phone": b.upper(), "username": c.upper(), "password": d}
            data.append(file)
            write_file = open("register.txt", "wb")
            pickle.dump(data, write_file)
            write_file.close()
            messagebox.showinfo("Congratulations !", "Registration Successful !")
            self.registration_frame.place_forget()
            self.loggingin_interface()

    def first_login_intrfc(self):
        """Fuction where user can log in only if the credentials are correct :return: None"""
        self.indication = 1
        self.loginpage_frame.place_forget()
        self.interface_1st_win_frame = Frame(self.mainframe, bg="#50D0B3", bd=2)
        self.interface_1st_win_frame.place(relx=0.010, rely=0.150, relheight=0.830, relwidth=0.981)
        self.TSeparator1 = ttk.Separator(self.interface_1st_win_frame, orient="vertical")
        self.TSeparator1.place(relx=0.238, rely=0.024, relheight=0.946)
        self.Frame3 = Frame(self.interface_1st_win_frame, bd=2)
        self.Frame3.place(relx=0.249, rely=0.026, relheight=0.948, relwidth=0.74)
        self.logoutbtn = ttk.Button(self.interface_1st_win_frame, text="Log out", command=self.log_out)
        self.logoutbtn.place(relx=0.068, rely=0.518, height=30, width=98)
        self.enttuser = Label(self.interface_1st_win_frame, bg="#50D0B3",text=f"Logged in as :{self.enter_username.get()}")
        self.enttuser.place(relx=0.020, rely=0.419, height=36, width=180)
        self.Label31 = Label(self.interface_1st_win_frame, text="Manage\n with\n Ease", bg="#50D0B3",font="Algerian 18")
        self.Label31.place(relx=0.03, rely=0.081, height=100, width=145)
        self.Frame5 = Frame(self.interface_1st_win_frame, bg="#85c0e9", bd="2")
        self.Frame5.place(relx=0.01, rely=0.624, relheight=0.353, relwidth=0.22)
        self.Frame5.configure(background="#50D0B3")
        self.TButton4 = ttk.Button(self.Frame5, text="User Registration", command=self.registration)
        self.TButton4.place(relx=0.040, rely=0.058, height=40, width=158)
        self.employeremove = ttk.Button(self.Frame5, text="Remove Employee", command=self.remove)
        self.employeremove.place(relx=0.040, rely=0.381, height=40, width=158)
        self.emprege = ttk.Button(self.Frame5, text="Employee Registration", command=self.employee_registration)
        self.emprege.place(relx=0.040, rely=0.697, height=40, width=158)
        self.scroll_x = Scrollbar(self.Frame3, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Frame3, orient=VERTICAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.employee_tree = ttk.Treeview(self.Frame3, column=(
            'first_name', 'last_name', 'Department', 'Mobile', "Employee_id"),
                                          xscrollcommand=self.scroll_x.set,
                                          yscrollcommand=self.scroll_y.set)
        self.employee_tree.heading('first_name', text="First Name")
        self.employee_tree.heading('last_name', text="Last Name")
        self.employee_tree.heading('Department', text="Department")
        self.employee_tree.heading('Mobile', text="Cell Number")
        self.employee_tree.heading('Employee_id', text="Employee ID")
        self.employee_tree['show'] = 'headings'
        self.employee_tree.column('first_name', width=120)
        self.employee_tree.column('last_name', width=120)
        self.employee_tree.column('Department', width=120)
        self.employee_tree.column('Mobile', width=120)
        self.employee_tree.column('Employee_id', width=120)
        self.scroll_x.config(command=self.employee_tree.xview)
        self.scroll_y.config(command=self.employee_tree.yview)
        self.employee_tree.bind(('<ButtonRelease-1>'), self.pointer)
        self.employee_tree.pack(fill=BOTH, expand=True)
        self.viewit()

    def viewit(self):
        """ Function loads the data inside the Tree view.. :return: None """
        try:
            query = open("Employee.txt", "rb")
            result = pickle.load(query)
        except Exception:
            query = open("Employee.txt", "wb+")
            result = pickle.dump([], query)
            result = []
        self.employee_tree.delete(*self.employee_tree.get_children())
        for row in result:
            self.employee_tree.insert('', END, values=(row["first_name"], row["last_name"], row["Department"],
                                                       row["Mobile"], row["Employee_id"]))

    def pointer(self, event):
        """Function that highlights the tree view entries :param event: Select the pointed part :return: None"""
        try:
            point = self.employee_tree.focus()
            content = self.employee_tree.item(point)
            row = content['values']
            if len(row) != 0:
                point1 = row[3]
                self.cursor = [point1]
        except Exception:
            self.cursor = []

    def employee_registration(self):
        """Function where every detail of the employee is stored within with departmental combobox included
        :return: None
        """
        try:
            a = open("Employee.txt", "rb")
            pickle.load(a)
        except Exception:
            test = []
            a = open("Employee.txt", "wb")
            pickle.dump(test, a)

        font9 = "-family {Segoe UI Black} -size 11 -weight bold -slant roman"
        self.interface_1st_win_frame.place_forget()
        self.Frame1 = Frame(self.mainframe, bd=2, bg="#50D0B3")
        self.Frame1.place(relx=0.008, rely=0.15, relheight=0.841, relwidth=0.982)
        self.Label1 = Label(self.Frame1, font=font9, text="Employee Registration", bg="#50D0B3")
        self.Label1.place(relx=0.027, rely=0.022, height=46, width=792)
        self.frstname = Entry(self.Frame1)
        self.frstname.place(relx=0.188, rely=0.182, height=34, relwidth=0.276)
        self.frstname_1 = Entry(self.Frame1)
        self.frstname_1.place(relx=0.661, rely=0.176, height=34, relwidth=0.276)
        try:
            load = open("department.txt", "rb")
            a = pickle.load(load)
            load.close()
        except Exception:
            write = open("department.txt", "wb")
            pickle.dump([], write)
            write.close()
        load = open("department.txt", "rb")
        values = pickle.load(load)
        load.close()
        self.deparmentalcombo = ttk.Combobox(self.Frame1, values=values, state="readonly")
        self.deparmentalcombo.place(relx=0.188, rely=0.308, relheight=0.079, relwidth=0.28)
        if values != []:
            self.deparmentalcombo.set(values[0])
        else:
            self.deparmentalcombo.set("None")
        self.frstname_2 = Entry(self.Frame1)
        self.frstname_2.place(relx=0.188, rely=0.44, height=34, relwidth=0.276)
        self.name_first = Label(self.Frame1, text="First Name:", bg="#50D0B3")
        self.name_first.place(relx=0.041, rely=0.18, height=36, width=112)
        self.nm_ls = Label(self.Frame1, bg="#50D0B3", text="Last Name:")
        self.nm_ls.place(relx=0.497, rely=0.185, height=36, width=112)
        self.Label3 = Label(self.Frame1, text="Department:", bg="#50D0B3")
        self.Label3.place(relx=0.044, rely=0.308, height=36, width=112)
        self.depa = Label(self.Frame1, bg="#50D0B3", text="Cell Number:")
        self.depa.place(relx=0.502, rely=0.301, height=36, width=112)
        self.test = StringVar()
        self.frstname_4 = Entry(self.Frame1, textvariable=self.test)
        self.frstname_4.place(relx=0.662, rely=0.301, height=34, relwidth=0.276)
        self.test.trace_variable("w", self.input_validation)
        self.employid = Label(self.Frame1, text="Employee ID:", bg="#50D0B3")
        self.employid.place(relx=0.045, rely=0.44, height=36, width=112)
        self.TSeparator0 = ttk.Separator(self.Frame1)  # drawing of separation of frame
        self.TSeparator0.place(relx=0.007, rely=0.681, relwidth=0.984)
        self.depa = Label(self.Frame1, text="Add Department:", bg="#50D0B3")
        self.depa.place(relx=0.044, rely=0.710, height=36, width=112)
        self.departent = Entry(self.Frame1)
        self.departent.place(relx=0.188, rely=0.710, height=34, relwidth=0.276)
        self.TButton010 = ttk.Button(self.Frame1, text="Add Department", command=self.department)
        self.TButton010.place(relx=0.488, rely=0.710, height=40, width=148)
        self.TButton010 = ttk.Button(self.Frame1, text="Remove Department", command=self.removedep)
        self.TButton010.place(relx=0.688, rely=0.710, height=40, width=148)
        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.007, rely=0.831, relwidth=0.984)
        self.logoutbtn = ttk.Button(self.Frame1, text="Register", command=self.submit)
        self.logoutbtn.place(relx=0.408, rely=0.555, height=40, width=90)
        self.logoutbtn3 = ttk.Button(self.Frame1, text="Back", command=self.back_regem)
        self.logoutbtn3.place(relx=0.008, rely=0.845, height=40, width=90)

    def submit(self):
        """Function that validates the employee entered data :return: None"""
        a = self.frstname.get()
        b = self.frstname_1.get()
        c = self.deparmentalcombo.get()
        d = self.frstname_2.get()
        e = self.frstname_4.get()
        test = open("Employee.txt", "rb")
        data = pickle.load(test)
        list = [a.strip(), b.strip(), c.strip(), e.strip(), d.strip()]
        list3 = []
        for i in data:
            list3.append(i["Mobile"])
        if c == "None":
            messagebox.showinfo("Error", "You Need to add a department First")
        elif e in list3:
            messagebox.showerror("Error", "Employee Already Exists")
        elif "" in list:
            messagebox.showinfo("Error", "You cannot leave any details blank")
        else:
            test = open("Employee.txt", "rb")
            data = pickle.load(test)
            file = {"first_name": a.upper(), "last_name": b.upper(), "Department": c.upper(), "Mobile": e,
                    "Employee_id": d.upper()}
            data.append(file)
            write_file = open("Employee.txt", "wb")
            pickle.dump(data, write_file)
            write_file.close()
            messagebox.showinfo("Congratulations", "You've successfully registered..")
            self.back_regem()
            self.viewit()

    def input_validation(self, *args):
        """Function that validates the input by only allowing integer as response on entry. :return None """
        a = self.test.get()
        try:
            b = int(a)
        except Exception:
            self.test.set(a[:-1])

    def log_out(self):
        """Function that help to get back to login interface :return: None """
        self.loggingin_interface()

    def back_reg(self):
        """ Function that helps to get back to login interface from user registration :return: None """
        self.registration_frame.place_forget()
        self.first_login_intrfc()

    def back_regem(self):
        """"Function that helps to get back to login interface from employee registration :return None"""
        self.Frame1.place_forget()
        self.first_login_intrfc()

    def remove(self):
        """Function that removes employee from file and from tree view. :return: None"""
        if self.cursor == []:
            messagebox.showerror("Error", "Please select an Employee to remove")
        else:
            load = open("Employee.txt", "rb")
            result = pickle.load(load)
            final = []
            for i in result:
                if str(i["Mobile"]) == str(self.cursor[0]):
                    print("Removed")
                else:
                    final.append(i)
            final_load = open("Employee.txt", "wb")
            pickle.dump(final, final_load)
            final_load.close()
            messagebox.showinfo("Successful", "Employee removed successfully")
            self.viewit()

    def department(self):
        """Function that help to add and read the department :return: None """
        test = self.departent.get()
        read = open("department.txt", "rb")
        values = pickle.load(read)
        read.close()
        if test.strip() == "":
            messagebox.showinfo("Error", "Please Specify department to add")
        elif test.upper() in values:
            messagebox.showinfo("Error", "Department already Exists")
        elif test.upper() == "NONE":
            messagebox.showinfo("Error", "Invalid Department")
        else:
            values.append(test.upper())
            write = open("department.txt", "wb")
            pickle.dump(values, write)
            write.close()
            self.deparmentalcombo.config(values=values)
            self.deparmentalcombo.set(self.departent.get())

        self.departent.delete(0, END)

    def removedep(self):
        '''Function that helps to remove department :return: None'''
        load = open("department.txt", "rb")
        result = pickle.load(load)
        a = self.departent.get()
        b = a.upper()
        if b in result:
            result.remove(b)
            final_load = open("department.txt", "wb")
            pickle.dump(result, final_load)
            final_load.close()
            messagebox.showinfo("Successful", "Department removed successfully")
            self.deparmentalcombo.configure(values=result)
            if result != []:
                self.deparmentalcombo.set(result[0])
            else:
                self.deparmentalcombo.set("None")
        else:
            messagebox.showinfo("Error", "There is no such department registered !")

        self.departent.delete(0, END)

a = Employee_management_system()