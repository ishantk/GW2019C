class Student:
    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

    def studentToCSV(self):
        data = "{},{},{}\n".format(self.roll, self.name, self.age)
        return data


def saveStudent(data):

    # file = open("students.csv",'w')
    # file = open("students.csv", 'a')
    file = open("/Users/ishantkumar/Downloads/students.csv", 'a')
    file.write(data)
    file.close()
    print(">> Data Saved: ",data)

choice = "yes"

while(choice == "yes"):

    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    s = Student(roll=roll, name=name, age=age)
    print(s.studentToCSV())

    saveStudent(s.studentToCSV())

    choice = input("Would you like to add more students (yes/no) ? : ")

# Save Data of Object
# Persistance
# 1. Files
# 2. DataBases
#    2.1 SQL    -> MySQL, Oracle, etc..
#    2.2 NoSQL  -> MongoDB, FirebaseFirestore, Neo4J, etc..