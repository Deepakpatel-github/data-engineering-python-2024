# Challenge 1
contact = {"shubham": 97541, "lalit": 12564, "mohan": 56465}
print(contact["lalit"])

mydict = dict([('a', 1), ('b', 2)])
print(mydict)

# Challenge 2
movie_info = {'title': 'DDLJ', 'Director': 'Karan Johar', 'year': 2005}
print(movie_info['title'])
print(movie_info['Director'])
print(movie_info['year'])

for key, values in movie_info.items():
    print(f"{key}: {values}")

# Challenge 3
students_grade = {'Mohan': 'A', 'Shubham': 'A+', 'Deepak': 'C'}

students_grade['lalit'] = 'B+'
students_grade['Deepak'] = 'A'

print(students_grade)

mydict.update(movie_info)
print(mydict)


# Challenge 4
del mydict['year']
print(mydict)

mydict.pop('Director')
print(mydict)

mydict.popitem()
print(mydict)

mydict.clear()
print(mydict)

# Challenge 5
print(movie_info)
key = input("Enter a key to get value:")
if key in movie_info:
    print(f"The key '{key}' exists in dictionary with value:{movie_info[key]}")
else:
    print(f"The key '{key}' does not exist in dictionary with value:{movie_info.get(key, 'Not Available')}")

# Challenge 6

print(students_grade)
for key in students_grade:
    print(f"{key} : {students_grade[key]}")

for key, values in students_grade.items():
    print(key, ' : ', values)

for values in students_grade.values():
    print(values)

for key in students_grade.keys():
    print(key)

# Challenge 7
customer = {'D123': {'name': 'Deepak patel', 'address': {'city': 'Indore', 'state': 'MP'}, 'contact': '9754166812'}}

# print a specific customer's specific detail
print(customer['D123'])
print(customer['D123']['name'])
print(customer['D123']['address']['city'])
print(customer['D123']['address']['state'])
print(customer['D123']['contact'])

# Update any detail
customer['D123']['contact'] = '123456789'
print('Updated contact:', customer['D123']['contact'])
