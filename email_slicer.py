#format specifiers = {:flags} format a value
#based on what flags are inserted

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 58769834.9698

# .(number)f = round to that many decimal places (fixed point)
print(f"Price 1 is ${price1:.3f}")
      #outputs $3.141
print(f"Price 2 is ${price2:.2f}")
      #outputs $-987.65
print(f"Price 3 is {price3:.2f}")
      #outputs 12.34

# :number = allocate total number of characters by adding 0s
print(f"Price 1 is ${price1:10} with 10 characters.")
       #outputs$ ___3.14159

# :03 = allocate and zero pad that many spaces
print(f"Price 1 is ${price1:010} with 10 characters.")
       #outputs $0003.14159

# :<  = left justify where, when adding to total number of characters, extra spaces are forced to the right
print(f"Price 1 is ${price1:<10} with 10 characters.")
       #outputs $3.14159___

# :>  = right justify where, when adding to total number of characters, extra spaces are forced to the left (default)
print(f"Price 1 is ${price1:>10} with 10 characters.")
       #outputs $___3.14159

# :^  = center align where, when adding to total number of characters, extra spaces are forced around so the characters are centered
print(f"Price 1 is ${price1:^10} with 10 characters.")
       #outputs $_3.14159__

# :+  = use a plus sign for + to go in front of positive values, and - in front of negative values
print(f"Price 1 is ${price1:+}.")
       #outputs $+3.14159

print(f"Price 1 is ${price1: }.")
       #outputs $+3.14159

# :=  = place sign to leftmost position
print(f"Price 1 with =.2f: ${price1:=.2f}")
        #outputs $____3.14

#  :  = insert a space before positive numbers
print(f"Price 1 with space: ${price1:10}")
        #outputs $______3.14159

# :,  = comma separator
print(f"Price 1 is ${price4:,.2f}.")
       #outputs $58,769,834.96

