# def square(x):
#     return x*x # Normal way to define a function\

def avg():
    numOfnums = input("The number of numbers do you want calculate average of: ")
    numadd = 0
    if numOfnums.isalpha():
        text = "You have chosen an alien character now the program will terminate automatically!"
    elif numOfnums == '':
        text = "You have entered nothing! This program will terminate automatically!"
    elif int(numOfnums) <= 10:
        for i in range(int(numOfnums)):
            num = input(f"Enter the number {i+1}: ")
            if num == '':
                num = 0 # Requires only one equal
            elif num.isalpha():
                text = "You have chosen an alien character now the program will terminate automatically!"
                noOut = True
                break
            numadd += int(num)
            average = numadd/int(numOfnums)
        if noOut == True:
            text = "You have chosen an alien character now the program will terminate automatically!"
        else:
            text = f"The average of the {int(numOfnums)} numbers is {average}"
    else:
        text = "You have entered really a big number! This program will terminate automatically!"
    return text

# Below the function is taking a function as an argument and this functions are called higher order function
def appl(fx, value): # here fx is a function inside a function
    return 6 + fx(value)

# Using lamda function to define a function in a minimalistic (short) way
square = lambda x: x*x # Using lambda function define a funtion in just one line which doesn't have any name until we assign it by using equal parameter with a name
cube = lambda x: x*x*x
sum = lambda x, y, z: x+y+z

print(square(5))
print(cube(5))
print(sum(5, 6, 8))
# print(avg())
print(appl(cube, 2))
print(appl(lambda x: x*x, 2))