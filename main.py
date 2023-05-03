# Hey this is a comment
# print("Hello World \nHow are you?")
# print("Hello world\n"*25)
# for x in range(1,11):
#     # print(x)
#     for y in range(1,11):
#         print(x, "x", y, "=", x*y)
#     print("_______________________")
#     print()
# x = 1
# while(x<11):
#     y = 1
#     while(y<11):
#         print(x, "x", y, "=", x*y)
#         y += 1 
#     x += 1 
#     print("__________________________")
#     print()

# print("This thing is called \"Stone Mask\" Jojo")
# print("Hello", "World!", "How", "are", "you?", sep="____", end="007")
# print("New line")
# a = "Hello"
# b = 44
# c = 45.6
# d = True
# e = None
# f = complex(7, -5)
# print("The type of a is", type(a))
# print("The type of b is", type(a))
# print("The type of c is", type(a))
# print("The type of d is", type(a))
# print("The type of e is", type(a))
# print("The type of f is", type(f))
# print(f)
# print(45/2)
# print(45//2)
# print(45%2)
# print(5**2)

# Excersise
# a = 5
# b = 6
# print()
# print("The first number is:", a)
# print()
# print("The second number is:", b)
# print()
# print("The addition of the two numbers are", a, "+", b, "=", a+b)
# print()
# print("The subtraction of the two numbers are", a, "+", b, "=", a-b)
# print()
# print("The multiplication of the two numbers are", a, "+", b, "=", a*b)
# print()
# print("The division of the two numbers are", a, "+", b, "=", a/b)
# print()
# Explicit type casting (Changing the datatype by user)
# a = '1'
# b = '2'
# print(a + b) # Returns 12
# print(int(a) + int(b)) #Returns 3

# # Implicit type casting (Done by the python automatically)
# c = 1.9
# d = 8 # is an int
# print(c + d)  # Float plus Int Returns a float datatype changed automatically by python

# n = input("Enter your name\n")
# print("The namae is ",n)
# print('''Hello World!
# How are you?
# What?
# ''') # Multiple line string
# a = "B
'''
a = "Hello World!"
print(a[0:6]) # Returns Hello # Including 0 but not 6
print(a[:6]) # Returns Hello # Including 0 but not 6
print(a[1:6]) # Returns ellow # Including 1 but not 6
print(len(a)) # Returns 12
print(a[0:-3]) # Returns Hello Wor
print(a[0:len(a)-3]) # Also Returns Hello Wor
print(a[-1:len(a)-3]) # Returns blank
# means a[11:9] which doesn't makes any sense
#[-3:-1] means len(a)-3 = 12 - 3 = 9
# len(a)-1 = 12 -1 = 11
print(a[-3:-1])

for i in a:
    print(i) # The i is a new variable

'''
'''
nm = "Harry"
print(nm[-4:-2])
'''
