print("Challenge 1:")
# Initialize a secret number
secret_num = 5
# Create a variable to count number rof guesses
num_guesses = 0

while True:
    # Prompt the user to enter a guess number
    user_guess = int(input('Guess a number:'))

    # Increment the number of guess
    num_guesses += 1

    if secret_num < user_guess:
        print("Too high! Try again.")
    elif secret_num > user_guess:
        print("Too low! Try again.")
    else:
        print(f"Congratulation!!, You guessed the secret number in {num_guesses} guesses")
        break

print("\nChallenge 2:")
num1, num2, result = 0,0,0

while True:
    print('   Menu')
    print('1. Add')
    print('2. Subtract')
    print('3. Exit')

    choice = int(input('Enter your choice:'))
    if choice == 1:
        num1 = float(input('Enter first number:'))
        num2 = float(input('Enter second number:'))

        print(f'Result: {num1} + {num2} = {num1+num2}\n')
    elif choice == 2:
        num1 = float(input('Enter first number:'))
        num2 = float(input('Enter second number:'))

        print(f'Result: {num1} - {num2} = {num1 - num2}\n')
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")

import time

print("\nChallenge 2:")
start_time = int(input("Enter time in seconds:"))

counter = start_time

while counter >= 0:
    print(f"Time remaining: {counter} seconds", end='\r')

    counter -= 1
    time.sleep(1)
print("\nTime's up!")



