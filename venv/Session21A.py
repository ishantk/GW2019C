from tkinter import *
import mysql.connector


def clickHandler():

    name = entryName.get()
    phone = entryPhone.get()
    email = entryEmail.get()

    #print(name, phone, email)

    # 1. Write SQL Statement
    sql = "insert into Customer values(null, '{}','{}','{}')".format(name, phone, email)

    # 2. Create Connection with Database
    con = mysql.connector.connect(user="root", password="", host="localhost", database="auridb")

    # 3, Execute SQL Statement
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(name, " Saved in Database")


window = Tk()

lblTitle = Label(window, text="Welcome to CMS")
lblTitle.pack()

lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblEmail = Label(window, text="Enter Customer Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()


btnAddCustomer = Button(window, text="Add Customer", command=clickHandler)
btnAddCustomer.pack()


window.mainloop()