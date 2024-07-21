# Challenge 1
list1 = [1, 'deepak', 17.5]
print(list1)

list2 = list("Deepak")
print(list2)

list3 = [x**2 for x in range(1, 6)]
print(list3)

# Challenge 2
print(f"\nlist2 = first: {list2[0]}, last: {list2[-1]}")
print("value at index 2:", list2[2])

# Challenge 3
print('\nlist: ', list3)
list3[2] = 00
print("set 0 at index 3: ", list3)
list3[-2] = 99
print("set second last element 99: ", list3)

# Challenge 4
grocery = ['milk', 'bread', 'cream', 'biscuits', 'tomato']
print("Grocery list:", grocery)
grocery.remove('tomato')
print("tomato is removed: ", grocery)
print("remove 3rd element: ", grocery.pop(2))
print("Updated grocery list:", grocery)

# Challenge 5
board = [[" - " for _ in range(3)] for _ in range(3)]
# for row in board:
print(board)

# Challenge 6
color = ['red', 'blue', 'green']
R_Cube = [[[color[z] for x in range(3)] for y in range(3)] for z in range(3)]

print(R_Cube)

# Challenge 7
friends = ['shubham', 'dheeraj', 'lalit', 'mohan', 'bhupen']
for index, name in enumerate(friends, 1):   # begins with 1
    print(f"({index}, {name})")

# Challenge 8
student_info = ['Deepak patel', 23, 'A+']

name, age, grade = student_info
print(f'{name} at age {age}, score {grade} in MBA from IIM Ahmedabad')


