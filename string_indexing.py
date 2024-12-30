#indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_num = "1234-567-9043-3456"

#Get character at certain index
print(credit_num[4])

#Get characters between 2 indexes
print(credit_num[0 : 4])

#Easier way to get characters between 2 indexes when starting at index 0
print(credit_num[: 4])

#Easier way to get characters between 2 indexes when starting at given index and go to end of string
print(credit_num[4: ])

#Get last character of a string
print(credit_num[-1])

#Get every second character of a string
print(credit_num[::2])

#Get last 4 digits of a string
print(credit_num[-4 :])

#Reverse the characters in a string
reversed_card = credit_num[::-1]
print(reversed_card)

#Get every second character of a string from index 1 - 4
print(credit_num[1:4:2])