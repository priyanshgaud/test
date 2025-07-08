# A1
# num = int(input("Enter an integer: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# A2
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >= b and a >= c:
#     print("The largest number is:", a)
# elif b >= a and b >= c:
#     print("The largest number is:", b)
# else:
#     print("The largest number is:", c) 


# A3
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")

# A4
# percentage = int(input("Enter your percentage: "))
# if percentage >= 90:
#     print("Grade A")
# elif percentage >= 80:
#     print("Grade B")
# elif percentage >= 70:
#     print("Grade C")
# elif percentage >= 60:
#     print("Grade D")
# else:
#     print("Grade F")

# A5
# letter = input("Enter a letter: ").lower()
# if letter in ('a', 'e', 'i', 'o', 'u'):
#     print(letter, "is a vowel.")
# elif letter.isalpha() and len(letter) == 1:
#     print(letter, "is a consonant.")
# else:
#     print("Invalid input. Please enter a single alphabet letter.")

# A6
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))
# if operator == "+":
#     print("Result:", num1 + num2)
# elif operator == "-":
#     print("Result:", num1 - num2)
# elif operator == "*":
#     print("Result:", num1 * num2)
# elif operator == "/":
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Cannot divide by zero.")
# else:
#     print("Invalid operator. Please use +, -, *, or /.")

# A7
# num = float(input("Enter a number: "))
# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

# A8
# username = input("Enter username: ")
# password = input("Enter password: ")
# if username == "admin" and password == "1234":
#     print("Login Successful")
# else:
#     print("Login Failed")

# A9
# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))
# if (a + b > c) and (b + c > a) and (a + c > b):
#     print("The sides form a valid triangle.")
# else:
#     print("The sides do not form a valid triangle.") 

# A10
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / (height ** 2)
# print("Your BMI is:", round(bmi, 2))
# if bmi < 18.5:
#     print("Underweight")
# elif 18.5 <= bmi < 24.9:
#     print("Normal weight")
# elif 25 <= bmi < 29.9:
#     print("Overweight")

# A11
# price = float(input("Enter the price of the product: "))
# if price > 1000:
#     discount = price * 0.10
# elif 500 <= price <= 1000:
#     discount = price * 0.05
# else:
#     discount = 0
# final_price = price - discount
# print("Final price after discount:", round(final_price, 2)) 

# A12 
# month = input("Enter the name of a month: ").strip().lower()
# if month in ["january", "march", "may", "july", "august", "october", "december"]:
#     print("31 days")
# elif month in ["april", "june", "september", "november"]:
#     print("30 days")
# elif month == "february":
#     year = int(input("Enter the year: "))
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("29 days (leap year)")
#     else:
#         print("28 days")
# else:
#     print("Invalid month name")

# A13
# balance = 1000 
# print("Welcome to the ATM!")
# print("1. Check balance")
# print("2. Deposit money")
# print("3. Withdraw money")
# choice = input("Enter your choice (1/2/3): ")
# if choice == "1":
#     print("Your balance is:", balance)
# elif choice == "2":
#     amount = float(input("Enter amount to deposit: "))
#     balance += amount
#     print("Deposit successful. New balance is:", balance)
# elif choice == "3":
#     amount = float(input("Enter amount to withdraw: "))
#     if amount <= balance:
#         balance -= amount
#         print("Withdrawal successful. New balance is:", balance)
#     else:
#         print("Insufficient balance.")
# else:
#     print("Invalid choice.")

# A14
# age = int(input("Enter your age: "))
# if 0 <= age <= 1:
#     print("Infant")
# elif 2 <= age <= 4:
#     print("Toddler")
# elif 5 <= age <= 12:
#     print("Child")
# elif 13 <= age <= 19:
#     print("Teenager")
# elif 20 <= age <= 59:
#     print("Adult")
# elif age >= 60:
#     print("Senior")
# else:
#     print("Invalid age")

# A15
# day_num = int(input("Enter a number (1-7): "))
# if day_num == 1:
#     print("Monday")
# elif day_num == 2:
#     print("Tuesday")
# elif day_num == 3:
#     print("Wednesday")
# elif day_num == 4:
#     print("Thursday")
# elif day_num == 5:
#     print("Friday")
# elif day_num == 6:
#     print("Saturday")
# elif day_num == 7:
#     print("Sunday")
# else:
#     print("Invalid input. Please enter a number between 1 and 7.")
