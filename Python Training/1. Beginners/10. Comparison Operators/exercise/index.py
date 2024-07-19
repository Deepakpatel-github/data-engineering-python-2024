# challenge 1
if 10 < 5: print(True)
else: print(False)

# challenge 2
num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))
if num1 > num2:
    print(f"The first number ({num1}) is greater than the second number ({num2}).")
elif num1 < num2:
    print(f"The first number ({num1}) is less than the second number ({num2}).")
else:
    print(f"The first number ({num1}) is equal to the second number ({num2}).")

# challenge 3
str1 = input("Enter first string:")
str2 = input("Enter second string:")
str1_len = len(str1)
str2_len = len(str2)
if str1_len < str2_len:
    print('length of string2 is greater than string1')
elif str1_len > str2_len:
    print('length of string1 is greater than string2')
else:
    print('length of string1 is equal to string2')




