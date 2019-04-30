class Student:
    #Property of Class
    whiteBoardContent = "NA"

    def __init__(self, data):
        self.notebook = data # Property of Object
        Student.whiteBoardContent = "Be Exceptional !!"

    def show(self):
        print("NoteBook Data is:",self.notebook,"and WhiteBoard data is:",Student.whiteBoardContent)

s1 = Student("I am Learning Python")
s2 = Student("I have Learnt Python")
s3 = Student("I am done with Python")

Student.whiteBoardContent = "Search the Candle, rather than cursing the Darkness"

s4 = Student("Thank You for Session")

s1.show()
s2.show()
s3.show()
s4.show()