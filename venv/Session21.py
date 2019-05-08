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

"""

# Object which is holding data of a Customer is created in RAM
# Object is temporary
# We should save data of Object permanently
# 1. Files -> csv
# 2. Database -> Table -> Data Save

name = input("Enter Customer Name:")
phone = input("Enter Customer Phone:")
email = input("Enter Customer Email:")

c1 = Customer(None, name, phone, email)
print(c1.__dict__)

save = input("Do you wish to save customer in database (yes/no) ?")

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