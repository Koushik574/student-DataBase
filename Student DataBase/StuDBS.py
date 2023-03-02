from tkinter import *
import mysql.connector as a
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.title("Student Database")
win.iconbitmap(r'C:\Users\Sai Koushik\OneDrive\Pictures\SQL Logo.ico')
canvas = Canvas(win, width=300, height=400)
canvas.pack()
loginimage = PhotoImage(file=r"C:\Users\Sai Koushik\OneDrive\Pictures\Login Photo1.png")
canvas.create_image(20, 40, anchor=NW, image=loginimage)
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d+0+0" % (width, height))
databse_label = Label(win, text="Database name", font=("calibre", 20))
databse_label.pack(pady=5)
database = Entry(win, width=50)
database.pack(pady=5)
password_label = Label(win, text="Password", font=("calibre", 20))
password_label.pack(pady=5)
password = Entry(win, width=50, show="*")
password.pack(pady=10)


def entry():
    global db
    global win2
    global isclicked
    dbase = database.get()
    pword = password.get()
    try:
        db = a.connect(host="localhost", user="root", database=dbase,  passwd=pword)
        cursor = db.cursor()
        win2 = Tk()
        win2.geometry("350x1200")
        win2.title("Student Datbase-Main Menu")
        # win2.iconbitmap("icon.ico")

        def view():
            win3 = Tk()
            win3.title("View Tables")
            # win3.geometry("%dx%d+0+0"%(width,height))
            # win3.iconbitmap("icon.ico")
            tv1 = ttk.Treeview(win3, columns=(1), show="headings", height="30")
            tv1.grid(row=0, column=0, rowspan=30)
            tv1.heading(1, text="Tabels")
            cursor.execute("show tables")
            all_table = cursor.fetchall()

            def create_new_table():
                warning_message = messagebox.showwarning("Student Database", '''*NAME OF THE EXSISTING TABLE SHOULD NOT BE ENTERED*
                                                Got It?''', parent=win3)
                # win4=Tk()
                # win4.geometry("%dx%d+0+0"%(width,height))
                new_table_label = Label(win3, text="New Table Name", font=("calibre", 20))
                new_table_label.grid(row=2, column=1)
                new_table_entry = Entry(win3, width=60)
                new_table_entry.grid(row=3, column=1)

                def create_table():
                    new_table_entry_var = str(new_table_entry.get())
                    try:
                        cursor.execute("create table " + str(
                            new_table_entry_var) + " (Admi_No int primary key,Roll_no int,Name varchar(30),Class_Section varchar(50),Address varchar(300),Father_Name varchar(30),Mother_name varchar(30))")
                        db.commit()
                    except:
                        messagebox.showerror("Table Name Error", "Table Already Exsists", parent=win3)

                create_table = Button(win3, text="Create Table", command=create_table).grid(row=4, column=1)
                # win4.mainloop()

            for a in all_table:
                tv1.insert('', 'end', values=a)
            warning = Label(win3, text="*NAME OF THE EXSISTING TABLE SHOULD NOT BE ENTERED*",
                            font=("calibre", 10)).grid(row=0, column=1)
            create_new_table = Button(win3, text="Create New Table", command=create_new_table,
                                      font=("calibre", 20)).grid(row=1, column=1)
            win3.mainloop()

        def insert():
            win4 = Tk()
            win4.title("Insert Data")
            # win5.geometry("%dx%d+0+0"%(width,height))
            win4.iconbitmap("icon.ico")
            table_name_label = Label(win4, text="Enter the table name", font=("calibre", 20))
            table_name_label.grid(row=0, column=0, columnspan=2)
            global table_name
            table_name = Entry(win4, width=50)
            table_name.grid(row=1, column=0, columnspan=2)

            def enter_table():
                b = (table_name.get(),)
                cursor.execute("show tables")
                all_table = cursor.fetchall()
                l1 = []
                for c in all_table:
                    l1.append(c)
                if b in l1:
                    # win6=Tk()
                    # win6.resizable(False ,False)
                    insert_values = Label(win4, text="Insert Values", font=("calibre", 30)).grid(row=4, columnspan=2)
                    admin_no_label = Label(win4, text="Admission Number").grid(row=5, column=0)
                    admin_no_entry = Entry(win4, width=100)
                    admin_no_entry.grid(row=5, column=1)
                    roll_no_label = Label(win4, text="Roll Number").grid(row=6, column=0)
                    roll_no_entry = Entry(win4, width=100)
                    roll_no_entry.grid(row=6, column=1)
                    name_label = Label(win4, text="Name").grid(row=7, column=0)
                    name_entry = Entry(win4, width=100)
                    name_entry.grid(row=7, column=1)
                    class_sec_label = Label(win4, text="Class & Section").grid(row=8, column=0)
                    class_sec_entry = Entry(win4, width=100)
                    class_sec_entry.grid(row=8, column=1)
                    address_label = Label(win4, text="Address").grid(row=9, column=0)
                    address_entry = Entry(win4, width=100)
                    address_entry.grid(row=9, column=1)
                    f_name_label = Label(win4, text="Father's Name").grid(row=10, column=0)
                    f_name_entry = Entry(win4, width=100)
                    f_name_entry.grid(row=10, column=1)
                    m_name_label = Label(win4, text="Mother's Name").grid(row=11, column=0)
                    m_name_entry = Entry(win4, width=100)
                    m_name_entry.grid(row=11, column=1)

                    def insert_data():
                        try:
                            cursor.execute("insert into " + table_name.get() + " values(%s,%s,%s,%s,%s,%s,%s)", (
                            int(admin_no_entry.get()), int(roll_no_entry.get()), name_entry.get(),
                            class_sec_entry.get(), address_entry.get(), f_name_entry.get(), m_name_entry.get()))
                            db.commit()
                            messagebox.showinfo("Done", "Data inserted", parent=win4)
                        except:
                            messagebox.showerror("Error", "Data already exsits", parent=win4)

                    insert_data_but = Button(win4, text="Insert Data", font=("calibre", 20), command=insert_data)
                    insert_data_but.grid(row=12, columnspan=2)
                    # win6.mainloop()
                else:
                    messagebox.showerror("Table Name Error", "Incorrect table name entered", parent=win4)

            enter_button = Button(win4, text="Enter", font=("calibre", 20), command=enter_table).grid(row=3, column=0,
                                                                                                      columnspan=2)
            win4.mainloop()

        def view_data():
            win5 = Tk()
            win5.title("View Data")
            # win7.geometry("%dx%d+0+0"%(width,height))
            win5.iconbitmap("icon.ico")
            table_label = Label(win5, text="Table Name", font=("calibre", 20)).pack()
            table_entry = Entry(win5, width=50)
            table_entry.pack()

            def view_table_data():
                d = (table_entry.get(),)
                cursor.execute("show tables")
                all_table = cursor.fetchall()
                l2 = []
                for c in all_table:
                    l2.append(c)
                if d in l2:
                    # win=Tk()
                    # win8.geometry("%dx%d+0+0"%(width,height))
                    tv2 = ttk.Treeview(win5, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="30")
                    tv2.pack()
                    tv2.heading(1, text="Admin Number")
                    tv2.heading(2, text="Roll Number")
                    tv2.heading(3, text="Name")
                    tv2.heading(4, text="Class & Section")
                    tv2.heading(5, text="Address")
                    tv2.heading(6, text="Father's Name")
                    tv2.heading(7, text="Mother's Name")
                    cursor.execute("select * from " + table_entry.get())
                    all_data = cursor.fetchall()
                    for e in all_data:
                        tv2.insert('', 'end', values=e)
                    # win8.mainloop()
                else:
                    messagebox.showerror("Table Name Error", "Incorrect table name entered", parent=win5)

            view_table_data_but = Button(win5, text="Enter", font=("calibre", 20), command=view_table_data).pack()
            win5.mainloop()

        def drop_table():
            win6 = Tk()
            win6.title("Delete Table")
            win6.iconbitmap("icon.ico")
            # win3.geometry("%dx%d+0+0"%(width,height))
            tv3 = ttk.Treeview(win6, columns=(1), show="headings", height="30")
            tv3.grid(row=0, column=0, rowspan=30)
            tv3.heading(1, text="Tabels")
            cursor.execute("show tables")
            all_table = cursor.fetchall()
            for a in all_table:
                tv3.insert('', 'end', values=a)
            # warning = Label(win6,text="*NAME OF THE EXSISTING TABLE SHOULD NOT BE ENTERED*",font=("calibre",10)).grid(row=0,column=1)
            # create_new_table = Button(win6,text="Create New Table",command=create_new_table,font=("calibre",20)).grid(row=1,column=1)

            # win9=Tk()
            # win9.geometry("%dx%d+0+0"%(width,height))
            enter_table_del_label = Label(win6, text="Enter Table Name", font=("calibre", 20)).grid(row=0, column=1)
            delete_entry = Entry(win6, width=50)
            delete_entry.grid(row=1, column=1)

            def delete():
                w = (delete_entry.get(),)
                cursor.execute("show tables")
                all_table = cursor.fetchall()
                l3 = []
                for v in all_table:
                    l3.append(v)
                if w in l3:
                    messagebox.askyesno("Confirmation", "Are you sure?", parent=win6)
                    cursor.execute("drop table " + delete_entry.get())
                    messagebox.showinfo("Done!!", "Table Deleted", parent=win6)
                    db.commit()
                else:
                    messagebox.showwarning("Table Name Error", "Incorrect table name entered", parent=win6)

            delete_button = Button(win6, text="Delete", command=delete, font=("calibre", 20)).grid(row=2, column=1)

        def update():
            win7 = Tk()
            win7.title("Update Table")
            win7.iconbitmap("icon.ico")
            global table_update_name_entry
            table_update_name_label = Label(win7, text="Table Name", font=("calibre", 20)).grid(row=0, column=0)
            table_update_name_entry = Entry(win7, width=50)
            table_update_name_entry.grid(row=0, column=1)

            def update_enter():
                e = (table_update_name_entry.get(),)
                cursor.execute("show tables")
                table_all = cursor.fetchall()
                l = []
                for r in table_all:
                    l.append(r)
                if e in l:
                    # win11=Tk()
                    global admin_no_update_entry
                    admin_no_update_label = Label(win7, text="Admission Number", font=("calibre", 20)).grid(row=1,
                                                                                                            column=0)
                    admin_no_update_entry = Entry(win7, width=50)
                    admin_no_update_entry.grid(row=1, column=1)

                    def enter_admin_no():
                        cursor.execute(
                            "select * from " + table_update_name_entry.get() + " where Admi_no= " + admin_no_update_entry.get())
                        y = cursor.fetchall()
                        if y == []:
                            messagebox.showerror("Error", "Admission Number Not Found", parent=win7)
                        else:
                            update_label = Label(win7, text="Edit", font=("calibre", 20)).grid(row=2, columnspan=3)
                            updat_message = Label(win7, text="Enter Here", font=("calibre", 10)).grid(row=3, column=0)
                            global update_entry
                            update_entry = Entry(win7, width=100)
                            update_entry.grid(row=3, column=1)
                            global clicked
                            clicked = StringVar(win7)
                            clicked.set("Enter Here")
                            drop = OptionMenu(win7, clicked, "Roll No", "Name", "Class Section", "Address",
                                              "Father name", "Mother Name")
                            drop.grid(row=3, column=2)

                            def edit_enter():
                                try:
                                    a = clicked.get()
                                    if a == "Enter Here":
                                        messagebox.showinfo("Input Error", "No Input Entered", parent=win7)
                                    if a == "Roll No":
                                        cursor.execute(
                                            "update " + table_update_name_entry.get() + " set Roll_no= " + update_entry.get() + " where Admi_no= " + admin_no_update_entry.get())
                                        # cursor.commit()
                                    if a == "Name":
                                        cursor.execute(
                                            "update " + table_update_name_entry.get() + " set Name= " + "\'" + str(
                                                update_entry.get()) + "\'" + " where Admi_no= " + admin_no_update_entry.get())
                                        # cursor.commit()
                                    if a == "Class Section":
                                        cursor.execute(
                                            "update " + table_update_name_entry.get() + " set Class_Section= " + "\'" + str(
                                                update_entry.get()) + "\'" + " where Admi_no= " + admin_no_update_entry.get())
                                        # cursor.commit()
                                    if a == "Address":
                                        cursor.execute(
                                            "update " + table_update_name_entry.get() + " set Address= " + "\'" + str(
                                                update_entry.get()) + "\'" + " where Admi_no= " + admin_no_update_entry.get())
                                        # cursor.commit()
                                    if a == "Father Name":
                                        cursor.execute(
                                            "update " + table_update_name_entry.get() + "\'" + " set Father_Name= " + str(
                                                update_entry.get()) + "\'" + " where Admi_no= " + admin_no_update_entry.get())
                                        # cursor.commit()
                                    if a == "Mother Name":
                                        cursor.execute(
                                            "update " + table_update_name_entry.get() + "\'" + " set Mother_name= " + str(
                                                update_entry.get()) + "\'" + " where Admi_no= " + admin_no_update_entry.get())
                                        # cursor.commit()
                                    messagebox.showinfo("Updated!!", "Updated successfully!!", parent=win7)
                                except:
                                    messagebox.showerror("Error", "An error occured", parent=win7)

                            update_enter = Button(win7, text="Edit", font=("calibe", 10), command=edit_enter).grid(
                                row=4, columnspan=3)

                    admin_no_update_button = Button(win7, text="Enter", font=("calibre", 20),
                                                    command=enter_admin_no).grid(row=1, column=2)
                else:
                    messagebox.showerror("Table Name Error", "Incorrect table name entered", parent=win7)

            table_update_name_button = Button(win7, text="Enter", font=("calibre", 20), command=update_enter).grid(
                row=0, column=2)

        def clear_data():
            win8 = Tk()
            win8.title("Delete Data")
            win8.iconbitmap("icon.ico")
            table_name_label1 = Label(win8, text="Enter the table name:", font=("calibre", 20))
            table_name_label1.pack()
            global table_name1
            table_name1 = Entry(win8, width=50)
            table_name1.pack()

            def enter_table1():
                messagebox.showwarning("Warning", "ARE YOU SURE??", parent=win8)
                b = (table_name1.get(),)
                cursor.execute("show tables")
                all_table = cursor.fetchall()
                l1 = []
                for c in all_table:
                    l1.append(c)
                if b in l1:
                    cursor.execute("delete from " + str(table_name1.get()))
                    messagebox.showinfo("Done!", "Deleted!!!", parent=win8)
                else:
                    messagebox.showerror("Error!!", "Table Doesn\'t Exsists", parent=win8)

            Enter = Button(win8, text="Clear", command=enter_table1, font=("calibre", 20)).pack()

        view_table_button = Button(win2, text="View Table", command=view, font=("calibre", 20), pady=10).pack(pady=30)
        insert_button = Button(win2, text="Insert Data", command=insert, font=("calibre", 20), pady=10).pack(pady=30)
        view_data_button = Button(win2, text="View Data", command=view_data, font=("calibre", 20), pady=10).pack(
            pady=30)
        clear_table = Button(win2, text="Delete Data", command=clear_data, font=("calibre", 20), pady=10).pack(pady=30)
        update_table_button = Button(win2, text="Edit Table", font=("calibre", 20), pady=10, command=update).pack(
            pady=30)
        drop_table_button = Button(win2, text="Delete Table", font=("calibre", 20), pady=10, command=drop_table).pack(
            pady=30)
        win2.mainloop()
    except:
        messagebox.showerror("Error", "Incorrect Password or Incorrect Datbase Name")


entrybutton = Button(win, text="Enter", font=("calibre", 20), command=entry)
entrybutton.pack()
win.mainloop()