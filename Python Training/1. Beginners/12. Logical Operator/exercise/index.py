# Challenge 1
age = int(input("Enter your age: "))
grade = float(input("Enter your grade: "))
if age >= 18 and grade >= 60:
    print("Eligible for scholarship!")
else:
    if age < 18:
        print("Not old enough.")
    if grade < 60:
        print("Grade not high enough.")

#challenge 2
original_price = 2800
print(f"Orignal price is {original_price}")
has_membership = input("Do you have a membership? (yes/no): ").strip().lower()
has_coupon = input("Do you have a valid coupon? (valid/invalid): ").strip().lower()

if has_membership == 'yes' or has_coupon == 'valid':
    final_price = original_price * ( 1 - 1/10)
    print(f"Discount applied! The final price is: {final_price:.2f}")
else:
    print(f"No discount applied. The final price is: {original_price:.2f}")

# Challenge 3
day = input("Enter a day of the week: ")
weekend_days = ["saturday", "sunday"]
if day not in weekend_days:
    print("It's a weekday!")
else:
    print("It's the weekend!")

# Challenge 4
correct_username = "admin"
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password != "":
    print("Login successful!")
else:
    if username != correct_username:
        print("Incorrect username")
    if password == "":
        print("Empty password")








