import os

path = os.getcwd()
print("CWD: ",path) # venv

os.chdir("/Users/ishantkumar/Downloads")

path = os.getcwd()
print("CWD Now is: ",path)

# os.mkdir("/Users/ishantkumar/Downloads/GW2019C")
# print("Directory Created")

# os.rmdir("/Users/ishantkumar/Downloads/GW2019C")
# print("Directory Removed")

print("OS Name:",os.name)
print("User:",os.getlogin())
print("Parent Process ID:",os.getppid())

path = os.path.join("/Users/ishantkumar/Downloads","CPP2018Batch")
print(path)

newPath = os.path.split(path)

# os.chdir(path)

print(newPath)

path = "/Users/ishantkumar/Downloads"
path = os.path.join(path,"CPP2018Batch")

print("Is this path existing? ",os.path.exists(path))
# os.path.isdir(path)
# os.path.isfile(path)
allFiles = os.walk(path)
files = list(allFiles)

for file in files:
    print(file)

# Assignment:
# Count different type of files in any specific path