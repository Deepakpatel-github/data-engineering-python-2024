name = input("Enter your fullname: ")

# Challenge 1
print("UpperCase: ", name.upper())
print("LowerCase: ", name.lower())
print("Capitalize: ", name.capitalize())
print("Title case: ", name.title())

# Challenge 2
print("leading and trailing spaces removed:", name.strip())

# Challenge 3
str = input("Enter a string: ")
chr = input("Enter a character: ")

print(f"Is string starts with this char \'{chr}\'? ", str.startswith(chr))
print(f"Is string ends with this char \'{chr}\'? ", str.endswith(chr))

# Challenge 4
str1 = input("Enter a string: ")
word1 = input("To find: ")
word2 = input("Replace with: ")
print("Result:", str1.replace(word1, word2))

# Challenge 5
sentence = input("Write a sectence: ")
word3 = input("word to find: ")

find_position = sentence.find(word3)
print(find_position)
# if found return index, if not return -1

try:
    index_position = sentence.index(word3)
except ValueError:
    index_position = None

    # if found returns index, if not returns value error
    # to handle value error we use try except

# Challenge 6
sentence1 = 'the magic you are looking for is in work you are avoiding!!'
words_list = sentence1.split(' ')
print(words_list)

join_words = '_'.join(words_list)
print(join_words)

# Challenge 7
sentence2 = 'a b c d g g t f k k k l o l k f s s k p j'
print(sentence2.count('k')) #5


