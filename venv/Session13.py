# Whatever you are writing in class belongs to class
class Customer:

    # Constructor
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print("======",self.name,"======")
        print("Phone:",self.phone)
        print("Email:", self.email)
        print("=========================")


c1 = Customer("John", "+91 99999 88888", "john@example.com")
c1.showCustomerDetails() # -> Shall be translated to Customer.showCustomerDetails(c1)
Customer.showCustomerDetails(c1)

print()

print(c1.__dict__)
print(Customer.__dict__)




# https://docs.python.org/ -> Python Documentation (Reference)