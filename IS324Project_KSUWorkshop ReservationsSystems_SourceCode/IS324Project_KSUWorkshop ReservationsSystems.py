import hashlib
from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import messagebox
import re
import csv
from random import randint
from tkinter import ttk


# Part 1 : database :
conn = sqlite3.connect('KSUWorkshop.db')

c = conn.cursor()
c.execute(''' Create table IF NOT EXISTS student(
StuID Char(9) Primary Key,
FName    CHAR (30),
LName    CHAR (30),
Password CHAR (30),
Email    CHAR (30),
PhoneNo CHAR(15)
 ); ''')

c.execute(''' Create table IF NOT EXISTS Workshop(
WorkshopID    Char(5) Primary Key ,
WorkshopName  CHAR (30),
WorkshopLoc   CHAR (30),
WorkshopCap   INT,
WorkshopDate Date,
WorkshopTime CHAR(5)
); ''')

c.execute(''' Create table IF NOT EXISTS reservation(
reserveID   Char(5) Primary Key,
StuID   CHAR(9),
WorkshopID  CHAR(5),
FOREIGN KEY(StuID) REFERENCES student(StuID) ,
FOREIGN KEY(WorkshopID) REFERENCES Workshop(WorkshopID) 
 ); ''')

c.execute('''CREATE TABLE IF NOT EXISTS admin (
adminID TEXT PRIMARY KEY,
password TEXT);''')
admin_id = "admin"
password = "123456"
admin_password_hash = hashlib.sha256(password.encode()).hexdigest()
# Check if the adminID already exists in the table
c.execute("SELECT adminID FROM admin WHERE adminID = ?", (admin_id,))
existing_admin = c.fetchone()
if existing_admin:
    # If the adminID exists update the password
    c.execute("UPDATE admin SET password = ? WHERE adminID = ?", (admin_password_hash, admin_id))
else:
    # If the adminID doesn't exist, insert
    c.execute("INSERT INTO admin (adminID, password) VALUES (?, ?)", (admin_id, admin_password_hash))

print("student : ")
c.execute("Select * from student")
print(c.fetchall())
print("Workshop :")
c.execute("Select * from Workshop")
print(c.fetchall())
print("reservation : ")
c.execute("Select * from reservation")
print(c.fetchall())
conn.commit()
conn.close()

# ___________________________________________________
# Part 2 : students sign up window:
class KSUWorkshop:
    def __init__(self):
        self.Signup_window()
    def Signup_window(self):

            self.main_window = tk.Tk()
            self.main_window.geometry('450x350')
            self.main_window.title("KSU Workshops Reservation System signup")
            # Signup label
            self.label_1 = tk.Label(self.main_window, text="Student Sign up", bg="#008DC3", fg='white', width=27,font=("bold", 22))
            self.label_1.place(x=0, y=0)
            # StudentID label
            self.label_5 = tk.Label(self.main_window, text="StudentID:", bg="#008DC3", fg='white', width=17,font=("bold", 10))
            self.label_5.place(x=50, y=80)
            self.StuIDentry = tk.Entry(self.main_window, width=30)
            self.StuIDentry.place(x=200, y=80)
            # First name label
            self.label_3 = tk.Label(self.main_window, text="First Name:", bg="#008DC3", fg='white', width=17,font=("bold", 10))
            self.label_3.place(x=50, y=110)
            self.fNameEntry = tk.Entry(self.main_window, width=30)
            self.fNameEntry.place(x=200, y=110)
            # Last name label
            self.label_4 = tk.Label(self.main_window, text="Last Name", bg="#008DC3", fg='white', width=17,font=("bold", 10))
            self.label_4.place(x=50, y=140)
            self.lNameEntry = tk.Entry(self.main_window, width=30)
            self.lNameEntry.place(x=200, y=140)
            # Password label
            self.label_5 = tk.Label(self.main_window, text="Password:", bg="#008DC3", fg='white', width=17,font=("bold", 10))
            self.label_5.place(x=50, y=170)
            self.passEntry = tk.Entry(self.main_window, width=30)
            self.passEntry.place(x=200, y=170)
            # Email label
            self.label_6 = tk.Label(self.main_window, text="Email address:", bg="#008DC3", fg='white', width=17,font=("bold", 10))
            self.label_6.place(x=50, y=200)
            self.emailEntry = tk.Entry(self.main_window, width=30)
            self.emailEntry.place(x=200, y=200)
            # Phone number label
            self.label_7 = tk.Label(self.main_window, text="Phone number:", bg="#008DC3", fg='white', width=17,font=("bold", 10))
            self.label_7.place(x=50, y=230)
            self.PhoneNoEntry = tk.Entry(self.main_window, width=30)
            self.PhoneNoEntry.place(x=200, y=230)
            # Submit button
            tk.Button(self.main_window, text='Submit', width=17, bg='#008DC3', fg='white', command=self.save_Stu_Info).place(x=70, y=270)
            # Login button
            tk.Button(self.main_window, text="Login", bg="#008DC3", fg='white', width=17, command=lambda :[self.main_window.destroy(),self.login_window()]).place(x=230, y=270)
            self.main_window.mainloop()

    def save_Stu_Info(self):
        try:
            if len(self.StuIDentry.get()) == 0 or len(self.passEntry.get()) == 0 or len(self.fNameEntry.get()) == 0 or len(self.lNameEntry.get()) == 0 or len(self.emailEntry.get()) == 0 or len(self.PhoneNoEntry.get()) == 0:
                messagebox.showinfo("missing input", "Try Again, Enter your Information")
            else:
             conn = sqlite3.connect('KSUWorkshop.db')
            c = conn.cursor()
            # student id
            StuID = str(self.StuIDentry.get())
            reg = "^[0-9]{9}$"
            x = re.search(re.compile(reg), StuID)
            # validate StuID
            if not x:
                messagebox.showinfo("Invalid studentID", "StudentID must be consists of 9 digits, Try Again")
                return
            # first&last Name
            fName = str(self.fNameEntry.get())
            lName = str(self.lNameEntry.get())
            if not fName or not lName:
                messagebox.showinfo("missing input", "first name and last name should not be empty, Try Again")
                return
            # validate password
            password = str(self.passEntry.get())
            reg = "^[A-Za-z0-9]{6,100}$"
            pat = re.compile(reg)
            x = re.search(pat, password)
            if not x:
                password = ''
                messagebox.showinfo("invalid password format", "password must consists at least of 6 digits or letters, Try Again")
                return
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # validate phone
            PhoneNo = str(self.PhoneNoEntry.get())
            reg2 = "^(05)[0-9]{8}$"
            y = re.search(re.compile(reg2), PhoneNo)
            if not y:
                messagebox.showinfo("Invalid Phone Number", "Phone Number must be consists of 10 digits and starts with \'05\', Try Again")
                return
            # validate email
            email = str(self.emailEntry.get())
            reg = r"^([a-zA-Z0-9\._-]+){8}(@student\.ksu\.edu\.sa)$"
            z = re.search(re.compile(reg), email)
            if not z:
                messagebox.showinfo("invalid Email", "Email should be in formate of xxxxxxxx@student.ksu.edu.sa, Try Again")
                return
            # insert and check if id is existed
            id = c.execute(f"SELECT StuID FROM student WHERE StuID = {StuID}")
            if len(id.fetchall()) == 0:
                sql = """INSERT INTO student VALUES('{}','{}','{}','{}','{}','{}')
                """.format(StuID, fName, lName, password_hash, email, PhoneNo)
                c.execute(sql)
                conn.commit()
                messagebox.showinfo("Registration successfully", "Student registration successfully")

            else:
                messagebox.showinfo("ID already exist", "The entered id is Already exist, Try Again")
            conn.close()
        except sqlite3.Error:
            messagebox.showinfo("database error", "DataBase Error")

        except:
            messagebox.showinfo("error", "Student registration Was Unsuccessfully, Try Again")

        # ___________________________________________________
        # Part 3 : login window :
    def login_window(self):

        self.main_window = tk.Tk()
        self.main_window.geometry('400x200')
        self.main_window.title("KSU Workshops Reservation System login")
        self.userVar = tk.StringVar()
        self.passwordVar = tk.StringVar()
        self.IDLabel = tk.Label(self.main_window, text="ID :", bg="#008DC3", fg='white', width=17, font=("bold", 10))
        self.IDLabel.place(x=20, y=60)
        self.IDEntry = tk.Entry(self.main_window, textvariable=self.userVar, width=30)
        self.IDEntry.place(x=170, y=60)

        self.PassLabel = tk.Label(self.main_window, text="Password :", bg="#008DC3", fg='white', width=17,font=("bold", 10))
        self.PassLabel.place(x=20, y=90)
        self.PassEntry = tk.Entry(self.main_window, textvariable=self.passwordVar, show='*', width=30)
        self.PassEntry.place(x=170, y=90)

        loginButton = tk.Button(self.main_window, text="Login", bg="#008DC3", fg='white', width=17 , command=self.login)
        loginButton.place(x=150, y=140)

        self.main_window.mainloop()

    def login(self):
        if len(self.userVar.get()) == 0 or len(self.passwordVar.get()) == 0:
            messagebox.showinfo("missing input", "try Again, Enter ID and Password")
        else:
            reg = "^[0-9]{9}$"
            x1 = re.search(re.compile(reg), str(self.userVar.get()))

            if not x1 and self.userVar.get() != "admin":
                messagebox.showinfo("Error", "Invalid ID or password, Try Again")
                self.userVar.set("")
                self.passwordVar.set("")
                return
            conn = sqlite3.connect('KSUWorkshop.db')
            c = conn.cursor()
            c.execute('SELECT * FROM student WHERE StuID = ? ', (self.userVar.get(),))
            check = c.fetchone()
            if check is None and self.userVar.get() == "admin":
                c.execute('SELECT * FROM admin WHERE adminID = ?', (self.userVar.get(),))
                admin_check = c.fetchone()
                if admin_check is not None:
                    stored_admin_password_hash = admin_check[1]
                    entered_admin_password_hash =self.passwordVar.get()
                    entered_admin_password_hash = hashlib.sha256(entered_admin_password_hash.encode()).hexdigest()
                    if entered_admin_password_hash == stored_admin_password_hash:
                        self.main_window.destroy()
                        self.admin_Window()
                        conn.close()
                        return
            if check is None:
                messagebox.showinfo("Error", "Invalid ID or password, Try Again")
                self.userVar.set("")
                self.passwordVar.set("")
            else:
                stored_password_hash = check[3]
                entered_password = self.passwordVar.get()
                entered_password_hash = hashlib.sha256(entered_password.encode()).hexdigest()
                if entered_password_hash == stored_password_hash:
                    try:
                        self.main_window.destroy()
                    except:
                        pass
                    self.Student_Window(self.userVar.get())
                else:
                    messagebox.showinfo("Error", "Invalid ID or password, Try Again")
                    self.userVar.set("")
                    self.passwordVar.set("")
                    return
            conn.close()

    # ___________________________________________________
    # Part 4 : admin window
    def admin_Window(self):
        self.main_window = tk.Tk()
        self.main_window.geometry('450x350')
        self.main_window.title("Admin Window")

        # Workshop label
        self.label_8 = tk.Label(self.main_window, text="Register New Workshop", width=27, bg="#008DC3", fg='white', font=("bold", 22))
        self.label_8.place(x=0, y=0)
        # Workshop name
        self.label_9 = tk.Label(self.main_window, text="Workshop Name:", bg="#008DC3", fg='white', width=17, font=("bold", 10))
        self.label_9.place(x=50, y=80)
        self.WorkshopNameEntry = tk.Entry(self.main_window, width=30)
        self.WorkshopNameEntry.place(x=200, y=80)
        # Workshop Location
        self.label_10 = tk.Label(self.main_window, text="Workshop Location:", bg="#008DC3", fg='white', width=17, font=("bold", 10))
        self.label_10.place(x=50, y=110)
        self.WorkshopLocEntry = tk.Entry(self.main_window, width=30)
        self.WorkshopLocEntry.place(x=200, y=110)
        # Workshop Capacity
        self.label_11 = tk.Label(self.main_window, text="Workshop Capacity:", bg="#008DC3", fg='white', width=17, font=("bold", 10))
        self.label_11.place(x=50, y=140)
        self.WorkshopCapEntry = tk.Entry(self.main_window, width=30)
        self.WorkshopCapEntry.place(x=200, y=140)
        # Workshop Date
        self.label_12 = tk.Label(self.main_window, text="Workshop Date:", bg="#008DC3", fg='white', width=17, font=("bold", 10))
        self.label_12.place(x=50, y=170)
        self.WorkshopDateEntry = tk.Entry(self.main_window, width=30)
        self.WorkshopDateEntry.place(x=200, y=170)
        # Workshop Time
        self.label_13 = tk.Label(self.main_window, text="Workshop Time:", bg="#008DC3", fg='white', width=17, font=("bold", 10))
        self.label_13.place(x=50, y=200)
        self.WorkshopTimeEntry = tk.Entry(self.main_window, width=30)
        self.WorkshopTimeEntry.place(x=200, y=200)

        # Create button
        self.CreateButton = (tk.Button(self.main_window, text='save', width=10, bg="#008DC3", fg='white', command=self.addWorkshopToDB))
        self.CreateButton.place(x=70, y=250)
        # Logout button
        self.LogoutButton = (tk.Button(self.main_window, text='Logout', width=10, bg="#008DC3", fg='white', command=lambda :[self.main_window.destroy(),self.Signup_window()]))
        self.LogoutButton.place(x=180, y=250)
        # Backup Button
        self.backupButton = tk.Button(self.main_window, text="Backup", width=10, bg="#008DC3", fg='white', command=self.backup_function)
        self.backupButton.place(x=290, y=250)

        self.main_window.mainloop()

    def addWorkshopToDB(self):
        try:
            conn = sqlite3.connect('KSUWorkshop.db')
            c = conn.cursor()
            # Workshop id
            WorkshopID = str(randint(10000, 99999))

            # Workshop Name
            WorkshopName = str(self.WorkshopNameEntry.get())
            if not WorkshopName:
                messagebox.showinfo("missing input", "Workshop name should not be empty, Try Again")
                return
            # Workshop Location
            WorkshopLoc = str(self.WorkshopLocEntry.get())
            if not WorkshopLoc:
                messagebox.showinfo("missing input", "Workshop Location should not be empty, Try Again")
                return
            # Workshop Date
            WorkshopDate = str(self.WorkshopDateEntry.get())
            # validate date
            reg = "^(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}$"
            x = re.search(re.compile(reg), WorkshopDate)
            if not x:
                messagebox.showinfo("invalid Date format", "Entered date must be dd/mm/yyyy, Try Again")
                return
            # Workshop Time
            WorkshopTime = str(self.WorkshopTimeEntry.get())
            # validate time
            reg = "^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"
            x = re.search(re.compile(reg), WorkshopTime)
            if not x:
                messagebox.showinfo("invalid Time format", "Entered Time must be in form of hh:MM, Try Again")
                return
            # Workshop Capacity
            WorkshopCap = str(self.WorkshopCapEntry.get())
            if not WorkshopCap:
                messagebox.showinfo("missing input", "Workshop capacity should not be empty, Try Again")
                return
            reg = "^[0-9]*$"
            x = re.search(re.compile(reg), WorkshopCap)

            if not x:
                messagebox.showinfo("Invalid input", "Workshop capacity must be digits, Try Again")
                return

            # insert and check if id is existed
            ID1 = c.execute(f"SELECT WorkshopID FROM Workshop WHERE WorkshopID = {WorkshopID}")
            if len(ID1.fetchall()) == 0:
                sql = """INSERT INTO Workshop VALUES('{}','{}','{}','{}','{}','{}')
                """.format(WorkshopID, WorkshopName, WorkshopLoc, WorkshopCap, WorkshopDate, WorkshopTime)
                c.execute(sql)
                conn.commit()
                conn.close()
                messagebox.showinfo("New Workshop Added", "New Workshop has been registered")
                self.WorkshopDateEntry.delete(0, END)
                self.WorkshopNameEntry.delete(0, END)
                self.WorkshopLocEntry.delete(0,  END)
                self.WorkshopCapEntry.delete(0,  END)
                self.WorkshopTimeEntry.delete(0, END)

            else:
                messagebox.showinfo("ID already exist", "The entered ID is exist , Try Again")
            conn.close()
        except sqlite3.Error:
            messagebox.showinfo("database error", "Error in Database")

        except:
            messagebox.showinfo("error", "Add new Workshop Was Unsuccessfully, Try Again")

    # Backup button
    def backup_function(self):
        try:
            conn = sqlite3.connect('KSUWorkshop.db')
            csv_file = open("backup.csv", 'w')
            csvwriter = csv.writer(csv_file, lineterminator="\n")

            # Fetch data from tables
            c = conn.cursor()
            c.execute("SELECT * FROM student")
            student_data = c.fetchall()

            c.execute("SELECT * FROM Workshop")
            Workshop_data = c.fetchall()

            c.execute("SELECT * FROM reservation")
            reservation_data = c.fetchall()

            c.execute("SELECT * FROM admin")
            Admin_data = c.fetchall()

            # Write data to CSV
            csvwriter.writerow([" StuID ", " FirstName ", " LastName ", " Password ", " Email ", " PhoneNo "])
            csvwriter.writerows(student_data)

            csvwriter.writerow(["WorkshopID", "WorkshopName", "WorkshopLoc", "WorkshopCap", "WorkshopDate", "WorkshopTime"])
            csvwriter.writerows(Workshop_data)

            csvwriter.writerow(["reserveID", "StuID", "WorkshopID"])
            csvwriter.writerows(reservation_data)

            csvwriter.writerow(["adminID", "password"])
            csvwriter.writerows(Admin_data)

            conn.commit()
            csv_file.close()
            conn.close()

            messagebox.showinfo("Backup","Backup successfully")
        except :
            messagebox.showinfo("error", "Backup Was Unsuccessfully, Try Again")

    # ___________________________________________________
    # Part 5 : students window :
    def Student_Window(self, uid):
        self.main_window = tk.Tk()
        self.main_window.geometry('900x400')
        self.main_window.title("Student Workshops window")

        # create a notebook
        self.notebook = ttk.Notebook(self.main_window)
        self.notebook.pack(pady=10, expand=True)

        # create frames
        self.frame1 = ttk.Frame(self.notebook, width=800, height=400)
        self.frame2 = ttk.Frame(self.notebook, width=600, height=400)

        # add frames to notebook
        self.notebook.add(self.frame1, text='Book a Workshop')
        self.notebook.add(self.frame2, text='View my Workshops')

        # tab1: book a Workshop
        conn = sqlite3.connect('KSUWorkshop.db')
        self.Tv = ttk.Treeview(self.frame1, columns=(1, 2, 3, 4, 5 ,6), show='headings', height=8)

        self.Tv.heading(1, text="Workshop ID")
        self.Tv.column(1, minwidth=20, width=100, anchor=CENTER, stretch=NO)
        self.Tv.heading(2, text="Workshop Name")
        self.Tv.column(2, minwidth=20, width=150, anchor=CENTER, stretch=NO)
        self.Tv.heading(3, text="Workshop Location")
        self.Tv.column(3, minwidth=20, width=150, anchor=CENTER, stretch=NO)
        self.Tv.heading(4, text="Workshop capacity")
        self.Tv.column(4, minwidth=20, width=150, anchor=CENTER, stretch=NO)
        self.Tv.heading(5, text="Workshop Date")
        self.Tv.column(5, minwidth=20, width=150, anchor=CENTER, stretch=NO)
        self.Tv.heading(6, text="Workshop Time")
        self.Tv.column(6, minwidth=20, width=150, anchor=CENTER, stretch=NO)

        # tab2: view my Workshops
        self.Tv2 = ttk.Treeview(self.frame2, columns=(1, 2, 3, 4, 5), show='headings', height=8)

        self.Tv2.heading(1, text="Workshop ID")
        self.Tv2.column(1, minwidth=20, width=100, anchor=CENTER, stretch=NO)
        self.Tv2.heading(2, text="Workshop Name")
        self.Tv2.column(2, minwidth=20, width=150, anchor=CENTER, stretch=NO)
        self.Tv2.heading(3, text="Workshop Location")
        self.Tv2.column(3, minwidth=20, width=150, anchor=CENTER, stretch=NO)
        self.Tv2.heading(4, text="Workshop Date")
        self.Tv2.column(4, minwidth=20, width=150, anchor=CENTER, stretch=NO)
        self.Tv2.heading(5, text="Workshop Time")
        self.Tv2.column(5, minwidth=20, width=150, anchor=CENTER, stretch=NO)
        self.Tv2.pack()

        cursor = conn.execute("SELECT* from Workshop")
        count = 0
        for row in cursor:
            self.Tv.insert(parent='', index=count, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            count += 1
        self.Tv.pack()
        self.SID = uid
        #book Button
        self.bookButton = ttk.Button(self.frame1, text='Book', width=20, command=self.AddbookToDB)
        self.bookButton.pack(side="bottom")
        # logout Button
        self.LogoutButton = ttk.Button(self.frame1, text='Logout', width=20,  command=lambda :[self.main_window.destroy(),self.Signup_window()])
        self.LogoutButton.pack(side="bottom")
        # show Button
        self.showButton = ttk.Button(self.frame2, text='show', width=20, command=self.show_function)
        self.showButton.pack(side="bottom")
        # logout Button2
        self.LogoutButton2 = ttk.Button(self.frame2, text='Logout', width=20,  command=lambda :[self.main_window.destroy(),self.Signup_window()])
        self.LogoutButton2.pack(side="bottom")
        conn.close()
        self.main_window.mainloop()

    def show_function(self):
        try:
            tabNo = str(self.notebook.index(self.notebook.select()))
            if tabNo == "1":
                for item in self.Tv2.get_children():
                    self.Tv2.delete(item)
                conn = sqlite3.connect('KSUWorkshop.db')
                cursor = conn.execute(f"SELECT reservation.WorkshopID, WorkshopName, WorkshopLoc, WorkshopDate, "
                                      f"WorkshopTime FROM student, Workshop, reservation WHERE student.StuID = "
                                      f"reservation.StuID AND Workshop.WorkshopID = reservation.WorkshopID AND "
                                      f"reservation.StuID = '{self.SID}'")
                count = 0
                for row in cursor:
                    self.Tv2.insert(parent='', index=count, text='', values=(row[0], row[1], row[2], row[3], row[4]))
                    count += 1
                self.Tv2.pack()
                conn.close()
            return
        except:
            messagebox.showinfo("Error", "You have no workshops.")

    def AddbookToDB(self):
        try:
            conn = sqlite3.connect('KSUWorkshop.db')
            c = conn.cursor()
            selectedItem = self.Tv.selection()[0]
            WorkshopID = str(self.Tv.item(selectedItem)['values'][0])

            reservID = str(randint(10000, 99999))  # generate random number of 5 digit

            # insert and check if id is existed
            id2 = c.execute(f"SELECT reservation.WorkshopID, WorkshopName, WorkshopLoc, WorkshopDate, WorkshopTime "
                            f"FROM student, Workshop, reservation where student.StuID = reservation.StuID and "
                            f"Workshop.WorkshopID = reservation.WorkshopID and reservation.StuID = {self.SID} "
                            f"and reservation.WorkshopID = '{WorkshopID}'")

            if len(id2.fetchall()) == 0:
                id = c.execute(f"SELECT WorkshopCap from  Workshop where WorkshopID = {WorkshopID} and WorkshopCap != 0")
                if len(id.fetchall()) == 0:
                    messagebox.showinfo("Booking Unsuccessfully", "No more Booking Available for This workshop")
                else:
                    sql = """INSERT INTO reservation VALUES('{}','{}','{}')
                    """.format(reservID, self.SID, WorkshopID)
                    c.execute(sql)
                    c.execute(f"UPDATE Workshop set WorkshopCap = WorkshopCap-1 where  WorkshopID={WorkshopID}")
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Booking successfully", "Your booking has been registered")

            else:
                messagebox.showinfo("Booking Unsuccessfully", "this Workshop already booked")
                conn.close()
        except sqlite3.Error:
               messagebox.showinfo("Database Error", "Error in Database ")

        except:
            messagebox.showinfo("Booking Unsuccessfully", "Booking Was Unsuccessfully, Try Again")

GUI = KSUWorkshop()
