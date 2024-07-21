# Challenge 1
num = int(input("Enter a number:"))

if num % 2 == 0:
    print("The number is even")
elif num % 2 != 0:
    print("The number is odd")

# Challenge 2
grade = input("Enter a grade between A to F:")
if grade in ['A', 'B', 'C']:
    print('Passing grade')
else:
    print('Failing grade')

# Challenge 3
day = input('Enter a dat of week:')
if day in ['saturday', 'sunday']:
    print('Weekend')
elif day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print('Weekday')
else:
    print('Invalid entry!!, Please try again.')





