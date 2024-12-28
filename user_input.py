# To ask for user input: 

name = input("What's your name?")
age = input("Enter your age")

print(f"Hello {name}")
print(f"You are {age} years old.")

# You cannot concatentate ints to strings

# Exercise: Change message with age to be 1 year older

#declare variable new_age, get the string input for age and change it to an int
new_age = int(input("Enter your age"))


# MAD LIBS GAME

adjective1 = input("Enter an adjective.")
noun = input("Enter a noun.")
adjective2 = input("Enter an adjective.")
verb = input("Enter a verb.")
adjective3 = input("Enter an adjective.")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}")

# Calculate the area of a rectangle

length = input("Enter the length in feet of a rectangle.")
width = input("Enter the width in feet of a rectangle.")
area = float(length) * float(width)

print(f"The area of the rectangle is {area} squared feet.")


item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")

# To truncate everything up to 2 decimal places

print(f"Your total is: ${round(total, 2)}")