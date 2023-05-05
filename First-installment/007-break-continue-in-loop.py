# Break statement starts here
for x in range(1, 8):
    # if (x == 5): # forcefully stops the loop from continuing prints up to 5 x 9 = 45 cause the loop stops before it reaches to the print statement below
    #     break
    print("5 x", x, "=", 5*x) # loop for printing multiplication table of five
    if (x == 5):
        break # forcefully stops the loop from continuing prints up to 5 x 5 = 25 cause the loop print the mentioned statement before it reaches the break statement
# Break statement ends here

print()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print()

# Continue statement starts here
for y in range(1, 8):
    if (y == 5):
        print("") # Skips the iteration ( the part 5 x 5 = 25) in continue statement and prints the rest which is left after that
        continue
    print("5 x", y, "=", 5*y)
    # if (y == 5):
    #     continue # Doesn't have any effect on the loop cause it is placed after the print statement
# Continue statement ends here

print()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print()

# Emulating do while loop in python

i = 0
while True: # When while loop is true it creates infinite loop
    print(i, end=" ^_^ ")
    i += 1
    if (i % 100 == 0):
        break