#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#*************************WHILE_LOOP_PRACTICE*******************************#
# QUESTION-1 Write a program that uses a while loop to count from 1 to 10 and print each number.
print("Counting from 1 to 10:")
count = 1
while count <= 10:
    print(count)
    count += 1

# Question-2 Create a while loop to print all even numbers from 1 to 20.
print("\nEven numbers from 1 to 20:")
num = 2
while num <= 20:
    print(num)
    num += 2

#QUESTION-3 Write a program using a while loop to calculate the sum of the first 10 natural numbers.
print("\nSum of first 10 natural numbers")
n = 10  
sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1
print("The sum of the first 10 natural numbers is:", sum_of_numbers)

#QUESTION-4 Write a program that prompts the user to enter numbers. The loop should keep asking for numbers
#until the user enters a negative number. When the loop exits, print the total sum of the numbers entered (excluding the negative number).
print("\nUser Input with Condition")
total_sum = 0
while True:
    number = float(input("Enter a number (enter a negative number to stop): "))
    if number < 0:
        break
    total_sum += number
print("The total sum of the numbers entered is:", total_sum)

#QUESTION-5 Create a guessing game where the user has to guess a number between 1 and 100.
#  Use a while loop to allow the user to keep guessing until they get it right. Provide hints if the guess is too high or too low.
print("\n NUMBER GUESSING GAME")
import random
secret_number = random.randint(1, 100)
guess = None
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

# QUESTION-6 Write a program to calculate the factorial of a given positive integer using a while loop.
print("\n Factorial Calculation")
num = int(input("Enter a positive integer to calculate its factorial: "))
factorial = 1
i = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    while i <= num:
        factorial *= i
        i += 1
    print(f"The factorial of {num} is: {factorial}")

# QUESTION-7 Write a program that uses a while loop to take in a series of numbers from the user.
#  The loop should stop when the user enters "done". Calculate and print the average of the entered numbers.
print("\nAverage Calculator")
total_sum = 0
count = 0
print("Enter numbers to calculate the average. Type 'done' when finished.")
while True:
    user_input = input("Enter a number (or type 'done' to finish): ")
    if user_input.lower() == "done":
        break
    try:
        number = float(user_input)
        total_sum += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a number.")
if count > 0:
    average = total_sum / count
    print("The average of the entered numbers is:", average)
else:
    print("No numbers were entered.")

# QUESTION-8 Print the Fibonacci sequence up to a specified number n (where n is an integer input by the user).
print("\n Fibonacci Sequence")
n = int(input("Enter a positive integer to print the Fibonacci sequence up to: "))
a, b = 0, 1
print("Fibonacci sequence up to", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b 
print()  
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////