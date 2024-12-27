# typecasting: Converting a value of one data type to another
# user input is always string

# To find the type of a variable...
name = "Bro"
age = 21
gpa = 3.2
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# Explicit type casting: Manually converting a value or variable into different data type, 
#using one of the cast keywords
age = float(age)
print(type(age))

# Convert gpa into an int
gpa = int(gpa)
print(type(gpa))

# Convert boolean into string (Student stills shows student, but as string)
student = str(student)
print(type(student))

# Convert value into boolean
# when converting number to boolean, if it is anything but 0, empty string, etc.,
# it will show as true
age = bool(age)
print(age)

# Implicit type casting: value or variable is converted into different
# data type automatically 
# Example: 

x = 2
y = 2.0

x = x / y
print(x)

# Above, x becomes a float because of the arithmetic expressions