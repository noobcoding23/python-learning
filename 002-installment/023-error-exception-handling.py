a = input("Enter a number: ")
print(f"The multiplication table of {a} is: ")
print()
try:
    for i in range(1,6):
        print(f"{a} x {i} = {int(a)*i}")
# except Exception as e: # Exception as e is used to show what's wrong with the lines of code
#     print(e)
except: # If you don't want to show what is wrong with the program but rather want to show a custom message
    print("Invalid input")
print()
print("This program is finished Have a nice day!")

# Multiple error exception handling
try:
    x = int(input("Enter an integer: "))
    num = [6, 3, 2]
    print(num[x])
except ValueError: # Checks if the value is invalid
    print("The value you entered is no an integer")
except IndexError:
    print("Index Error in the list print")
# Multiple error exception handling