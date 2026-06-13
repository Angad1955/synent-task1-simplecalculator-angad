# Task 1: Simple Calculator (CLI)
print("Simple Calculator:")
num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Cannot divide by zero!")

