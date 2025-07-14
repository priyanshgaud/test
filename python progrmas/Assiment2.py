#Q1:
# n = int(input("Enter a number: "))
# if n > 0:
#     print("The number is positive.")
# elif n < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

#Q2:
# n = int(input("Enter a number: "))
# if n%2==0:
#     print("even")
# else:
#     print("odd")

#Q3:
# n = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# if n > b:
#     print(n)
# elif n < b:
#     print(b)


#Q4:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a>=b and a>=c:
#     print("The largest number is:",a)
# elif b>=a and b>=c:
#     print("The largest number is:",b)
# else:
#     print("The largest number is :",c)

#Q5:
# ch = input("Enter a character: ").lower()
# if ch in ('a', 'e', 'i', 'o', 'u'):
#     print("Vowel")
# elif ch.isalpha():
#     print("Consonant")
# else:
#     print("Not an alphabet character")

# #Q6:
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

#Q7:
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# elif marks >= 50:
#     print("Grade: E")
# else:
#     print("Grade: F")

#Q8:
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("The number is divisible by both 3 and 5.")
# else:
#     print("The number is not divisible by both 3 and 5.")

#Q9:
# n = int(input("Enter a number: "))
# if n == 0:
#     print("Zero")
# elif n > 0:
#     if n % 2 == 0:
#         print("Positive even")
#     else:
#         print("Positive odd")
# else:
#     if n % 2 == 0:
#         print("Negative even")
#     else:
#         print("Negative odd")

#Q10:
# age = int(input("Enter age: "))
# if age < 13:
#     print("Child")
# elif age >= 13 and age <= 19:
#     print("Teen")
# elif age >= 20 and age <= 59:
#     print("Adult")
# else:
#     print("Senior")

#Q12:
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("Equilateral triangle")
#     elif a == b or b == c or a == c:
#         print("Isosceles triangle")
#     else:
#         print("Scalene triangle")
# else:
#     print("Not a valid triangle")

#Q13:
# day = int(input("Enter a number (1-7): "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid input:")

#Q14:
# signal = input("Enter traffic signal color (red/yellow/green): ")
# if signal == "red":
#     print("Stop")
# elif signal == "yellow":
#     print("Slow")
# elif signal == "green":
#     print("Go")
# else:
#     print("Invalid input")

#Q15:
# year = int(input("Enter a year: "))
# if year % 2 == 0:
#     print("Even year")
# else:
#     print("Odd year")

#Q16:
# n = int(input("Enter a number: "))
# if 1 <= n <= 100:
#     print("Number is in the range 1-100.")
# else:
#     print("Number is not in the range 1-100.")

#Q17:
# balance = float(input("Enter your balance: "))
# amount = float(input("Enter amount to deduct: "))

# if balance >= amount:
#     balance -= amount
#     print("Amount deducted. New balance:", balance)
# else:
#     print("Insufficient Balance")

#Q18:
# temp = float(input("Enter temperature in °C: "))
# if temp < 10:
#     print("Cold")
# elif 10 <= temp <= 25:
#     print("Moderate")
# else:
#     print("Hot")

#Q19:
# password = input("Enter your password: ")
# length = len(password)
# if length < 6:
#     print("Weak")
# elif 6 <= length <= 10:
#     print("Moderate")
# else:
#     print("Strong") 

#Q20:
# amount = float(input("Enter the amount: "))
# if amount > 1000:
#     discount = amount * 0.20
# elif 500 <= amount <= 1000:
#     discount = amount * 0.10
# else:
#     discount = amount * 0.05
# print("Discount:", discount)
# print("Amount after discount:", amount - discount)

#Q21:
# correct_username = "Priyansh"
# correct_password = "1234"
# username = input("Enter username: ")
# password = input("Enter password: ")
# if username == correct_username and password == correct_password:
#     print("Welcome")
# elif username == correct_username:
#     print("Incorrect Password")
# else:
#     print("User not found")

#Q22:
# units = int(input("Enter units consumed: "))
# if units <= 100:
#     bill = units * 1
# elif units <= 200:
#     bill = 100 * 1 + (units - 100) * 1.5
# else:
#     bill = 100 * 1 + 100 * 1.5 + (units - 200) * 2
# print("Total bill: ₹", bill)

#Q23:
# time = int(input("Enter time (0–23): "))
# if 5 <= time <= 11:
#     print("Morning")
# elif 12 <= time <= 17:
#     print("Afternoon")
# elif 18 <= time <= 21:
#     print("Evening")
# elif (22 <= time <= 23) or (0 <= time <= 4):
#     print("Night")
# else:
#     print("Invalid time input")

#Q24:
# day = input("Enter the day: ")
# if day == "saturday" or day == "sunday":
#     print("Weekend")
# else:
#     print("Weekday")

#Q25:
# weight = float(input("Enter weight in kilograms: "))
# height = float(input("Enter height in meters: "))
# bmi = weight / (height ** 2)
# print("BMI:", round(bmi, 2))
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal")
# elif bmi < 30:
#     print("Overweight")
# else:
#     print("Obese")

#Q26:
# age = int(input("Enter your age: "))
# nationality = input("Enter your nationality: ")
# if nationality.lower() == "indian":
#     if age >= 18:
#         print("You are eligible to vote.")
#     else:
#         print("Minimum age is 18.")
# else:
#     print(" You are not eligible to vote")

#Q27:
# cp = "secret123"
# for attempt in range(3):
#     ep = input("Enter password: ")
#     if ep == cp:
#         print("Access Granted")
#     else:
#         print("Incorrect password")
# else:
#     print("Account Locked")

