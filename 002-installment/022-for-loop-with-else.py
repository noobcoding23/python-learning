for x in range(5):
    print(x, end=" ")
else:
    print()
    print("The loop has ended") # When the loop is completed then the else statement is executed

for x in range(7):
    print(x, end=" ")
    if x == 5:
        break
else:
    print()
    print("The loop execution is finished") # This state is not going to be printed because the loop was not finished its execution rather it was stopped using if and brak statement

print()
# Whith for loop

y = 0
while y<5:
    print(y, end=" ")
    y += 1
else:
    print()
    print("The execution of the loop is finished successfully") # This is an example with while loop