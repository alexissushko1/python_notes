# Logical operators = use on conditional statements

#   and = checks if 2 or more conditions are true
# or = checks if at least 1 condition is true
# not = true if condition is false, and false if condition is true

temp1 = 25

# and

if temp1 > 0 and temp1 < 30:
  print("The temperature is good")
else:
  print("The temperature is bad.")

# or

temp2 = 2

if temp2 <= 0 or temp2 >= 30:
  print("The temperature is good")
else:
  print("The temperature is bad.")

# not

sunny = True
if not sunny:
  print("Stay inside")
else:
  print("Go outside")