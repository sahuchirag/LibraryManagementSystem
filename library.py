from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime
import tkinter
# from mysql.connector import(connection)

class libraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1400x700+0+0")

        # Variable
        self.member_var = StringVar()
        self.roll_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateissued_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()


        lbltitle = Label(self.root, text = "LIBRARY MANAGEMENT SYSTEM", bg = "powder blue", fg = "green", bd = 20, relief = RIDGE, font = ("times new roman", 50, "bold"), padx = 2, pady = 6)
        lbltitle.pack(side = TOP, fill = X)

        frame = Frame(self.root, bd = 12, relief = RIDGE, padx = 20, bg = "powder blue")
        frame.place(x = 0, y = 130, width = 1270, height = 350)

        # Data Frame Left
        DataFrameLeft = LabelFrame(frame, text = "Library Membership Information", bg = "powder blue", fg = "green", bd = 12, relief = RIDGE, font = ("times new roman", 14, "bold"), padx = 2, pady = 6)
        DataFrameLeft.place(x = 0, y = 5, width = 600, height = 320)

        lblMember = Label(DataFrameLeft, bg = "powder blue", text = "Member Type", font = ("times new roman", 10, "bold"), padx = 2, pady = 6)
        lblMember.grid(row = 0, column = 0, sticky = W)

        comMember = ttk.Combobox(DataFrameLeft, textvariable = self.member_var, font = ("times new roman", 10, "bold"), width = 20, state = "readonly")
        comMember["value"] = ["Admin", "Faculty", "Student"]
        comMember.grid(row = 0, column = 1)

        lblRollNo = Label(DataFrameLeft, bg="powder blue", text="Roll No.", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblRollNo.grid(row = 1, column = 0, sticky=W)
        txtRollNo = Entry(DataFrameLeft, textvariable = self.roll_var, font=("times new roman", 10, "bold"), width = 22)
        txtRollNo.grid(row = 1, column = 1)

        lblIDNo = Label(DataFrameLeft, bg="powder blue", text="ID No.", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblIDNo.grid(row=2, column=0, sticky=W)
        txtIDNo = Entry(DataFrameLeft, textvariable = self.id_var, font=("times new roman", 10, "bold"), width=22)
        txtIDNo.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="First Name", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, textvariable = self.firstname_var, font=("times new roman", 10, "bold"), width=22)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, textvariable = self.lastname_var, font=("times new roman", 10, "bold"), width=22)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address 1", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, textvariable = self.address1_var, font=("times new roman", 10, "bold"), width=22)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Address 2", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, textvariable = self.address2_var, font=("times new roman", 10, "bold"), width=22)
        txtAddress2.grid(row=6, column=1)

        lblPC = Label(DataFrameLeft, bg="powder blue", text="Postal Code", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblPC.grid(row=7, column=0, sticky=W)
        txtPC = Entry(DataFrameLeft, textvariable = self.postcode_var, font=("times new roman", 10, "bold"), width=22)
        txtPC.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile Number", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, textvariable = self.mobile_var, font=("times new roman", 10, "bold"), width=22)
        txtMobile.grid(row=8, column=1)

        lblBookID = Label(DataFrameLeft, bg="powder blue", text="Book ID", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID = Entry(DataFrameLeft, textvariable = self.bookid_var, font=("times new roman", 10, "bold"), width=22)
        txtBookID.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, textvariable = self.booktitle_var, font=("times new roman", 10, "bold"), width=22)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, bg="powder blue", text="Author", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, textvariable = self.author_var, font=("times new roman", 10, "bold"), width=22)
        txtAuthor.grid(row=2, column=3)

        lblDateIssued = Label(DataFrameLeft, bg="powder blue", text="Date Issued", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblDateIssued.grid(row=3, column=2, sticky=W)
        txtDateIssued = Entry(DataFrameLeft, textvariable = self.dateissued_var, font=("times new roman", 10, "bold"), width=22)
        txtDateIssued.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, textvariable = self.datedue_var, font=("times new roman", 10, "bold"), width=22)
        txtDateDue.grid(row=4, column=3)

        lblDaysOn = Label(DataFrameLeft, bg="powder blue", text="Days On", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblDaysOn.grid(row=5, column=2, sticky=W)
        txtDaysOn = Entry(DataFrameLeft, textvariable = self.daysonbook_var, font=("times new roman", 10, "bold"), width=22)
        txtDaysOn.grid(row=5, column=3)

        lblLate = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblLate.grid(row=6, column=2, sticky=W)
        txtLate = Entry(DataFrameLeft, textvariable = self.latereturnfine_var, font=("times new roman", 10, "bold"), width=22)
        txtLate.grid(row=6, column=3)

        lblDateOverDue = Label(DataFrameLeft, bg="powder blue", text="Date Over Due", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft, textvariable = self.dateoverdue_var, font=("times new roman", 10, "bold"), width=22)
        txtDateOverDue.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, textvariable = self.finalprice_var, font=("times new roman", 10, "bold"), width=22)
        txtActualPrice.grid(row=8, column=3)

        #Data Frame Right
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=12, relief=RIDGE, font=("times new roman", 14, "bold"), padx=2, pady=6)
        DataFrameRight.place(x = 630, y = 5, width=470, height=320)

        self.txtBox = Text(DataFrameRight, font=("times new roman", 14, "bold"), width = 32, height = 14, padx= 2, pady = 6)
        self.txtBox.grid(row = 0, column = 2)

        listScrollBar = Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky=NS)

        listBooks = ["Inside the Machine", "Structure and Interpretation of Computer Programs", "Design Patterns: Elements of Reusable Object-Oriented Software"]

        def SelectBooks(event = ""):
            value = str(listBox.get(listBox.curselection()))
            x = value

            if(x == "Inside the Machine"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Berry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateissued_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")


        listBox = Listbox(DataFrameRight, font=("times new roman", 14, "bold"), width = 20, height = 14)
        listBox.bind("<<ListboxSelect>>", SelectBooks)
        listBox.grid(row = 0, column = 0, padx = 4)
        listScrollBar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # Buttons Frame
        frameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frameButton.place(x=0, y=480, width=1270, height=70)

        btnAddData = Button(frameButton, command = self.adda_data, text = "Add Data", font=("times new roman", 14, "bold"), width = 15, bg = "blue", fg = "white")
        btnAddData.grid(row = 0, column = 0)

        btnShowData = Button(frameButton, command = self.showData, text="Show Data", font=("times new roman", 14, "bold"), width=15, bg="blue", fg="white")
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(frameButton, command = self.update,text="Update", font=("times new roman", 14, "bold"), width=15, bg="blue", fg="white")
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(frameButton, command = self.delete, text="Delete", font=("times new roman", 14, "bold"), width=15, bg="blue", fg="white")
        btnDelete.grid(row=0, column=3)

        btnReset = Button(frameButton, command = self.reset, text="Reset", font=("times new roman", 14, "bold"), width=15, bg="blue", fg="white")
        btnReset.grid(row=0, column=4)

        btnExit = Button(frameButton, command = self.iExit, text="Exit", font=("times new roman", 14, "bold"), width=15, bg="blue", fg="white")
        btnExit.grid(row=0, column=5)

        # Information Frame
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=550, width=1270, height=190)

        Table_frame = Frame(FrameDetails, bd=12, relief=RIDGE,  bg="powder blue")
        Table_frame.place(x=0, y=2, width=1210, height=170)

        xscroll = ttk.Scrollbar(Table_frame, orient = HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, column = ("Member Type", "Roll No", "ID No", "First Name", "Last Name", "Address 1", "Address 2", "PC", "Mobile", "BookID", "BookTitle", "Author", "Date Issued", "Date Due", "Days", "Late Fine", "Date Over Due", "Final Price"), xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

        xscroll.pack(side = TOP, fill = X)
        yscroll.pack(side = RIGHT, fill = Y)

        xscroll.config(command = self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("Member Type", text = "Member Type")
        self.library_table.heading("Roll No", text="Roll Number")
        self.library_table.heading("ID No", text="ID Number")
        self.library_table.heading("First Name", text="First Name")
        self.library_table.heading("Last Name", text="Last Name")
        self.library_table.heading("Address 1", text="Address 1")
        self.library_table.heading("Address 2", text="Address 2")
        self.library_table.heading("PC", text="Postal Code")
        self.library_table.heading("Mobile", text="Mobile Number")
        self.library_table.heading("BookID", text="Book ID")
        self.library_table.heading("BookTitle", text="Book Title")
        self.library_table.heading("Author", text="Author")
        self.library_table.heading("Date Issued", text="Date Issued")
        self.library_table.heading("Date Due", text="Date Due")
        self.library_table.heading("Days", text="Days")
        self.library_table.heading("Late Fine", text="Late Fine")
        self.library_table.heading("Date Over Due", text="Date Over Due")
        self.library_table.heading("Final Price", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill = BOTH, expand =1)

        self.library_table.column("Member Type", width = 100)
        self.library_table.column("Roll No", width=100)
        self.library_table.column("ID No", width=100)
        self.library_table.column("First Name", width=100)
        self.library_table.column("Last Name", width=100)
        self.library_table.column("Address 1", width=100)
        self.library_table.column("Address 2", width=100)
        self.library_table.column("PC", width=100)
        self.library_table.column("Mobile", width=100)
        self.library_table.column("BookID", width=100)
        self.library_table.column("BookTitle", width=100)
        self.library_table.column("Author", width=100)
        self.library_table.column("Date Issued", width=100)
        self.library_table.column("Date Due", width=100)
        self.library_table.column("Days", width=100)
        self.library_table.column("Late Fine", width=100)
        self.library_table.column("Final Price", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def adda_data(self):
        conn = mysql.connector.connect(username = "root", password = "Chirag@2001", host = "localhost", database = "sys")
        # config = {
        #     'user': 'root',
        #     'password': 'Chirag@2001',
        #     'host': 'localhost',
        #     'database': 'sys',
        #     # 'raise_on_warnings': True
        # } connection.MySQLConnection

        # conn = mysql.connector.connect(**config)
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
            self.member_var.get(), self.roll_var.get(), self.id_var.get(), self.firstname_var.get(), self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(),
            self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(), self.author_var.get(), self.dateissued_var.get(), self.datedue_var.get(), self.daysonbook_var.get(), self.latereturnfine_var.get(),
            self.dateoverdue_var.get(), self.finalprice_var.get()) )
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Details have been added successfully!")

    def update(self):
        conn = mysql.connector.connect(username="root", password="Chirag@2001", host="localhost", database="sys")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member = %s, ID = %s, FirstName= %s, LastName = %s, Address1 = %s, Address2 = %s, PostCode = %s, Mobile = %s, BookID = %s, BookTitle = %s, Author = %s, DateIssued= %s, DateDue = %s, DaysOnBook = %s, LateReturnFine= %s, DateOverDue = %s, FinalPrice = %s where RollNumber = %s",
                          (self.member_var.get(), self.id_var.get(), self.firstname_var.get(), self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(),
                           self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(), self.author_var.get(), self.dateissued_var.get(), self.datedue_var.get(), self.daysonbook_var.get(), self.latereturnfine_var.get(),
                           self.dateoverdue_var.get(), self.finalprice_var.get(), self.roll_var.get()))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Details Updated!")

    def fetch_data(self):
        conn = mysql.connector.connect(username="root", password="Chirag@2001", host="localhost", database="sys")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0 :
            self.library_table.delete(*self.library_table.get_children())

            for i in rows:
                self.library_table.insert("", END, values = i)
            conn.commit()
        conn.close()

    def get_cursor(self, event = ""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0])
        self.roll_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateissued_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END, "Member Type:\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END, "Roll Number:\t" + self.roll_var.get() + "\n")
        self.txtBox.insert(END, "ID Number:\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "Mobile:\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Author:\t" + self.author_var.get() + "\n")
        self.txtBox.insert(END, "Date Issued:\t" + self.dateissued_var.get() + "\n")
        self.txtBox.insert(END, "Late Return Fine:\t" + self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END, "Final Price:\t" + self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.roll_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateissued_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.latereturnfine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")
        self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit?")

        if(iExit > 0):
            self .root.destroy()
            return

    def delete(self):
        if(self.roll_var.get() == "" or self.id_var.get() == ""):
            messagebox.showerror("Error", "Select the details!")
        else:
            conn = mysql.connector.connect(username="root", password="Chirag@2001", host="localhost", database="sys")
            my_cursor = conn.cursor()
            query = "delete from library where RollNumber = %s"
            value = (self.roll_var.get(),)
            my_cursor.execute(query, value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Successfully deleted data.")

if __name__ == "__main__":
    root = Tk()
    obj = libraryManagementSystem(root)
    root.mainloop()