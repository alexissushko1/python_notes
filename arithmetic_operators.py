#Import math for functions, starting line 60
import math

friends = 0

# Addition operator
friends = friends + 1
# OR
friends += 1
print(friends)

#Subtraction operator
friends = friends - 2
# OR
friends -= 2

# Multiplication operator
friends = friends * 2
# OR
friends *= 2

#Division operator
friends = friends / 2
# OR
friends /= 2

#Exponents operator
friends = friends ** 2
# OR
friends **= 2

#Modulus operator
remainder = friends % 2
print(remainder)

x = 3.14
y = -4
z = 5

#Find the rounded value
round_result = round(x)
print(round_result)

#Find the absolute value
abs_value_result = abs(y)
print(abs_value_result)

#Find y to the power of x
pow_result = pow(y, x)
print(pow_result)

#Find the max of x, y, and z
max_result = max(x, y, z)
print(max_result)

#Find the min of x, y, and z
min_result = min(x, y, z)
print(min_result)

#Print value of pi
print(math.pi)

#Print value of e
print(math.e)

#Print square root of x
sqrt_result = math.sqrt(x)
print(sqrt_result)

#Always round up
round_up = math.ceil(x)
print(round_up)

#Always round down
round_down = math.floor(x)
print(round_down)

#Calculate the circumference of a circle with 2 decimal places

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")

#Calculate the area of a circle with 2 decimal places
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)} cm^2")

#Calculate the hypotenuse of a right triangle
a = float(input("Enter the width in feet of side a"))
b = float(input("Enter the width in feet of side b"))
hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The lenth of the hypotenuse is: {hypotenuse} ft^2. ")