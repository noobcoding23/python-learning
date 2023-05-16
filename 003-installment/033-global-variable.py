x = 99
print(x)

def hello():
    # global x # Using global keyword we can modify a global variable inside a function. However it is not a good practice to do that. So it is a good practice to avoide it
    x = 66 # This a local variable cannot be accessed outside a function
    global y
    y = 9966 # This is a global variable assigned inside a function
    print(f"The local variable is {x}")
    print("Hello World!")

print(f"The global variable is {x}")
hello()
print(f"The global variable is {x}")
print(f"{y}<--This is global variable assigned inside a function")