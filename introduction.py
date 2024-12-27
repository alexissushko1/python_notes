# In python, the runtime environment is python's interpreter
# You interact with your python interpreter by running python script.py


# To create a virtual environment on python: 
# -In folder you want, create a file with a .py extension.
# To print: print("Hello World")
# Press run button
# Open command palette on VSCode
# Python: Create Environment
# Choose venv environment type
# Choose latest interpreter
# This should create your project

# When printing, you can use single or double quotes
# To write a comment, use the pound sign (#)

# Variable: container for a value, acts as if it were the value
# snake_case for variables, functions, and methods: words written in lower case and spaces replaced with underscores

# Print "Hello World"

print("Hello World")

# Assign variable first name with string Alexis and print it

first_name = "Alexis"
print(first_name)

# Use f string to add variable with some text
print(f"Hello {first_name}")

#f stands for format
# You can add multiple variables while printing

#Print a 7.57 price in USD

price = 7.57
print(f"The price is ${price}")

# Boolean values are capitalized

# Write an if else statement to check whether you are a student or not

is_student = True
if is_student:
  print("You are a student.")
else:
  print("You are not a student.")