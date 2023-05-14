a = input("Enter a number between 9 to 5: ")

# try:
#     if a == "quit":
#         print("You have exited the program!")
# except:
#     if (int(a)<5 or int(a)>9):
#         raise ValueError("The value you entered should be between 9 to 5") # The raise keyword here is to help create the user a custom error
if a == "quit":
    print("You have exited the program!")
elif (int(a)<5 or int(a)>9):
    raise ValueError("The value you entered should be between 9 to 5") # The raise keyword here is to help create the user a custom error