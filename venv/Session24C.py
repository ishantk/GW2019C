import json # Java Script Object Notation

# Dictionary
employee = {"eid":101, "name":"John", "salary":20000}
print(employee)
print(type(employee))

print()

# We are converting dictionary of python into JSON Data
# JSON is a String

# dumps will convert dictionary of python into string json data
jsonData = json.dumps(employee)
print(jsonData)
print(type(jsonData))

print()

# loads will convert string json data into dictionary of python
emp = json.loads(jsonData)
print(emp)
print(type(emp))