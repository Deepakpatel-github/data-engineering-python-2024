# Challenge 1
hobbies = {'cooking', 'reading books', 'editing videos',  'editing videos'}
print(hobbies)
# duplicates removed

my_list = [1, 1, 2, 3, 6, 5, 6, 5, 4, 4]
unique_num = set(my_list)
print(unique_num)

# Challenge 2
specific_num = 7
if specific_num in unique_num:
    print(f"{specific_num} is present in above set")
else:
    print(f"Oops!!, {specific_num} is not present in above set")

# Adding duplicate element
unique_num.add(1)
print(unique_num)

# Challenge 3
set1 = {'a', 'b', 'c', 'd', 1, 2, 3}
set2 = {1, 4, 5, 'c', 'a'}

union_set = set1.union(set2)
print(union_set)

intersect_sets = set1.intersection(set2)
print(intersect_sets)   # only duplicated are there

difference_set = set1.difference(set2)
print(difference_set)  # values from set1 which is not present in set2

# set1.update(set2)
# print(set1)

# set1.intersection_update(set2)
# print(set1)

# set1.difference_update(set2)
# print(set1)

set3 = set1.symmetric_difference(set2)
print(set3)

print('\nChallenge 4')
fruits = {'mango', 'banana', 'cherry', 'guava'}
fruits.add('sitafal')
print(fruits)

fruits.remove('sitafal')
print(fruits)

# fruits.remove('sitafal')  # KeyError: 'sitafal'
fruits.discard('sitafal')

fruits.clear()
print(fruits)
