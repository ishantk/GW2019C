# Creating a Single Value Container
# And Writing Data 10 in it
age = 10
# age is a reference variable which will have HashCode for data 10
print("age is:",age)
print("HashCode of age is:",id(age))

# Update Operation
age = 20

# Read Operation
print("age is:",age)
print("HashCode of age is:",id(age))

# Reference Copy
johnsAge = age
print("johnsAge is:",age)
print("HashCode of johnsAge is:",id(age))

# Delete Operation
del age
# print("age is:",age) -> error


"""
    
        Class Notes:
        Orange Juice in Making !!

	Oranges			Source

	Juicer

	Liquid Juice 	Result

	Pack It

	Glass \_/		End Result


	===============
	Programming Language

	C++
	MyApp.cpp		Source Code	| High Level Language

	Compiler

	MyApp.obj 		Object Code | Low Level Language

	Pak It

W:	MyApp.exe 		Executable Code | Conatiner which contains .obj
M:  myApp.dmg
L:  myApp.sh


	Java
	MyApp.java

	Compiler

	MyApp.class

	Thats It !!

	Python
	MyApp.py

	Thats It !!


	Software Development
	MODEL
		Data Storage
	VIEW
		UI
	CONTROLLER
		Logic


	MODEL
		Data Storage Container / Box	
		1. Single Value Container
		2. Multi Value Container
			2.1 Hetrogeneous
			2.2 Homogeneous


		Instagram
			Profile Pic -> SVC
			Album -> MVC
					 Pics -> Homo
					 Pics + Videos -> Hetro

		Decimal System:			 
		12
		10*1 + 2

		112
		100*1 + 10*1 + 2

		Binary System:
		64	32	16  8	4  2  1
		0	0	0	1 	1  0  0 -> 12
		0   1   0   0   1  0  1 -> 37

		Explore as HW:
		Hexadecimal System
		0-9 | A to F

		Octal System
		0 - 7
		



						 	


"""