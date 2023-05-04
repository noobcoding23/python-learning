# Conditional Operators:
# "<", ">", "<=", ">=", "==", "!="
# a = int(input("Enter your age: "))
# # print(a>18)
# # print(a<=18)
# # print(a==18)
# # print(a!=18)
# # print(a<18)

# if (a>=18):
#     print("You can drive!")
# else:
#     print("You cannot drive!")

num = int(input("Enter a number: "))
if (num < 0):
    print("The number is negative")
elif (num == 0):
    print("The number is zero")
elif (num == 999):
    print("the number is special")
else:
    print("The number is positive")
    if (num <= 10):
        print("The number is between 1-10")
