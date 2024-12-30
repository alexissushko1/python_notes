#len is a function  to get length of string, including spaces

name = input("Enter your full name")

result = len(name)
print(result)

#Find method returns first (position) occurrence of a given character
find_result = name.find("o")
print(find_result)

#Find method returns last (position) occurrence of a given character
find_rresult = name.rfind("o")
print(find_rresult)

#Capitalize first letter in a string
capital_result = name.capitalize()
print(capital_result)

#Make all characters in a string upper case
upper_result = name.upper()
print(upper_result)

#Make all characters in a string lower case
lower_result = name.lower()
print(lower_result)

#Return true or false if string contains only digits
digit = name.isdigit()
print(digit)

#Return true or false if string contains only alphabetical characters
alpha = name.isalpha()
print(alpha)

#Count how many of a certain characters in a string
phone_number = input("Enter your phone number: ")
phone_result = phone_number.count("-")
print(phone_result)

#Replace any occurrence of 1 character with another
replace_phone = phone_number.replace("-", "")
print(replace_phone)

#Get a list of all string methods
print(help(str))

#Validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
  print("Your username cannot be more than 12 characters.")
elif not username.find(" ") == -1:
  print(f"Your username cannot contain spaces")
elif not username.isalpha():
  print(f"Your username cannot contain numbers.")
else:
  print(f"Welcome {username}")