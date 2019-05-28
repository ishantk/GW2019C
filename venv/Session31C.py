import pandas as pd

numList1 = [10, 20, 30, 40, 50]
numList2 = [11, 22, 33, 44, 55]

employee1 = {"eid":101, "name":"John", "email":"john@example.com"}
employee2 = {"eid":201, "name":"Fionna", "email":"fionna@example.com"}

employees = [
    {"eid":101, "name":"John", "email":"john@example.com"},
    {"eid": 201, "name": "Fionna", "email": "fionna@example.com"},
    {"eid":301, "name":"Kia", "email":"kia@example.com"}
]

# print(numList1)
# print(employee1)
# print(employees)

# Create a DataFrame instead of Series
df1 = pd.DataFrame([numList1, numList2])
df2 = pd.DataFrame([employee1, employee2])
df3 = pd.DataFrame(employees)

print(df1)
print()
print(df2)
print()
print(df3)

print()
print(df3["eid"])
print()
print(df3["eid"][1])