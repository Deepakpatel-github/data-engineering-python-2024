print("Challenge 1:")  # Challenge 1: Working with Quotes and Multiline Strings
famous_quote = ('''\"The magic you are looking for,
                    Is in the you are avoiding\"''')    # triple quotes used for multiline
print(famous_quote)


print("\nChallenge 2:")  # Challenge 2: Concatenation Fun
first_name = 'Deepak'
last_name = 'Patel'
full_name = first_name + ' ' + last_name
print("full name: ", full_name)
greeting = "A very warm welcome to you! " + full_name
print(greeting)


print("\nChallenge 3:")  # Challenge 3: String Length Exploration
name = input("Enter your name: ")
print("Length of your name:", len(name))


print("\nChallenge 4:")  # Challenge 4: Indexing and Slicing

print("First character:", name[0], "Last character:", name[-1])
first_index = int(input("Enter first index:"))
last_index = int(input("Enter last index:"))
print("Substring:", name[first_index:last_index+1])


print("\nChallenge 5:")  # Challenge 5: Case Conversions
sentence = input("Write a sentence: ")

print("In upper case: ", sentence.upper())
print("In lower case: ", sentence.lower())


print("\nChallenge 6:")  # Challenge 6: Stripping Away Whitespace
sentence1 = input("Write a sentence: ")
print("Whitespace removed: ", sentence1.strip())

print("\nChallenge 7:")  # Challenge 7: String Formatting Magic
name1 = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print(f"Hi, this is {name1}, I'm {age} years old, And currently living in [")

