#Conditional expression - A 1 line shortcut for the if else statement
#     (ternary operator) 
#Print or assign one of two values based on a condition
# return x if condition, else return y

num1 = 5

print("Positive" if num1 > 0 else "Negative")

num2 = 6

result1 = "EVEN" if num2 % 2 == 0 else "ODD"
print(result1)

a = 6
b = 7
max_num = a if a > b else b
print(max_num)

age = 25
min_num = "Adult" if a < b else "Minor"
print(min_num)

temp = 30
weather = "HOT" if temp > 20 else "COLD"
print(weather)

user_role = "admin"
access_level = "Full access" if user_role == "admin" else "Limited Access"
print(access_level)