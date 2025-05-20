#This code have support for the at time history works on Python
#Uses command terminal for output
#Devam Shah wrote this code 
#---!!!---
import time

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Error: Division by zero!" if y == 0 else x / y

def show_menu(): #menu option 
    print("\n" + "="*40)
    print("      🔢 WELCOME TO PY CALCULATOR")
    print("="*40)
    print(" Select an operation:")
    print("  1 ➕  Addition")
    print("  2 ➖  Subtraction")
    print("  3 ✖️  Multiplication")
    print("  4 ➗  Division")
    print("  5 📜  View History")
    print("  0 ❌  Exit")
    print("="*40)

history = []

while True:
    show_menu()
    choice = input("Enter your choice (0-5): ").strip()

    if choice == '0':
        print("\n👋 Thank you for using the calculator. Goodbye!\n")
        break

    elif choice == '5':
        print("\n📜 Calculation History:") #The history will only work for the at time entries only
        if not history:
            print("   No calculations yet.")
        else:
            for i, entry in enumerate(history, start=1):
                print(f"  {i}. {entry}")
        time.sleep(1)

    elif choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input(" Enter first number: "))
            num2 = float(input(" Enter second number: "))
        except ValueError:
            print(" ⚠️ Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            symbol = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            symbol = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            symbol = '*'
        elif choice == '4':
            result = divide(num1, num2)
            symbol = '/'

        formatted = f"{num1} {symbol} {num2} = {result}"
        print(f" ✅ Result: {formatted}")
        history.append(formatted)
        time.sleep(1)
    else:
        print(" ❗ Invalid choice. Please select from the menu.") 
