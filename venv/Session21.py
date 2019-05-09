import mysql.connector

class Customer:

    def __init__(self, cid, name, phone, email):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("===",self.cid,self.name,"==")



"""

create table Customer(
	cid int primary key auto_increment,
	name varchar(256),
	phone varchar(20),    
    email varchar(256)
)

insert into Customer values(null, 'John', '+91 99999 88888', 'john@example.com')
update Customer set name = 'John Watson', email = 'john.watson@example.com' where cid = 1
delete from Customer where cid = 1

"""

# Object which is holding data of a Customer is created in RAM
# Object is temporary
# We should save data of Object permanently
# 1. Files -> csv
# 2. Database -> Table -> Data Save

id = int(input("Enter Customer ID:"))
name = input("Enter Customer Name:")
phone = input("Enter Customer Phone:")
email = input("Enter Customer Email:")

c1 = Customer(None, name, phone, email)
print(c1.__dict__)

save = input("Do you wish to save customer in database (yes/no) ?")
update = input("Do you wish to update customer in database (yes/no) ?")
delete = input("Do you wish to delete customer in database (yes/no) ?")
show = input("Do you wish to view all customers in database (yes/no) ?")

if save == "yes":
    # 1. Write SQL Statement
    sql = "insert into Customer values(null, '{}','{}','{}')".format(c1.name, c1.phone, c1.email)

    # 2. Create Connection with Database
    con = mysql.connector.connect(user="root", password="", host="localhost", database="auridb")

    # 3, Execute SQL Statement
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(c1.name," Saved in Database")

if update == "yes":
    # 1. Write SQL Statement
    sql = "update Customer set name = '{}', phone='{}', email='{}' where cid = {}".format(name, phone, email, id)

    # 2. Create Connection with Database
    con = mysql.connector.connect(user="root", password="", host="localhost", database="auridb")

    # 3, Execute SQL Statement
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(name, " Updated in Database")

if delete == "yes":
    # 1. Write SQL Statement
    sql = "delete from Customer where cid = {}".format(id)

    # 2. Create Connection with Database
    con = mysql.connector.connect(user="root", password="", host="localhost", database="auridb")

    # 3, Execute SQL Statement
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(id, " Deleted from Database")

if show == "yes":
    # 1. Write SQL Statement
    sql = "select * from Customer"

    # 2. Create Connection with Database
    con = mysql.connector.connect(user="root", password="", host="localhost", database="auridb")

    # 3, Execute SQL Statement
    cursor = con.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    # print(data)

    for row in data:
        print(row)