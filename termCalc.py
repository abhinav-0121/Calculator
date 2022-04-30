import time

print("\nHello! Welcome to the calculator by OmegaX.")
time.sleep(2)

operation = input("\nWhat would you like to use your calculator for? (Addition, Substraction, Multiplication, Division) : ")
time.sleep(1.5)

if operation == "Addition":
    number1 = int(input("\nWhat is your first number? : "))
    number2 = int(input("What is your second number? : "))
    answer = number1 + number2
    time.sleep(1)
    print(f"\nThe sum of {number1} and {number2} is {answer}.")

if operation == "Substraction":
    number1 = int(input("\nWhat is your first number? : "))
    number2 = int(input("What is your second number? : "))
    answer = number1 - number2
    time.sleep(1)
    print(f"\nThe difference of {number1} and {number2} is {answer}.")

if operation == "Multiplication":
    number1 = int(input("\nWhat is your first number? : "))
    number2 = int(input("What is your second number? : "))
    answer = number1 * number2
    time.sleep(1)
    print(f"\nThe product of {number1} and {number2} is {answer}.")

if operation == "Division":
    number1 = int(input("\nWhat is your first number? : "))
    number2 = int(input("What is your second number? : "))
    answer = number1 / number2
    time.sleep(1)
    print(f"\nThe quotient of {number1} and {number2} is {answer}")

time.sleep(4)
exit()