import random
computerSelects = ['s', 'g', 'w'] # List for all the possible computer choices

# Smallcase s means snake
# Smallcase w means water
# Smallcase g means gun
# Caps W means Win
# Caps D means Draw
# Caps L means Lose

winConditions = [
    # User input snake
    ['s', 'w', 'W'],
    ['s', 's', 'D'],
    ['s', 'g', 'L'],
    # User input water
    ['w', 'g', 'W'],
    ['w', 'w', 'D'],
    ['w', 's', 'L'],
    # User input gun
    ['g', 's', 'W'],
    ['g', 'g', 'D'],
    ['g', 'w', 'L']
]

winThree = 0 # A variable to count winning times
drawThree = 0 # A variable to count Draw times

# Function to fetch win, draw or lose result


def winCheckF(x):
    return winConditions[x][-1]

# print(winCheckF(1)) # test


print("Welcome to the game of Snake, Water and Gun!")
print()
for round in range(3):
    computerStrike = random.choice(computerSelects) # To generate random choices of computer before users

    usrStrike = input("Snake, water and gun what do you choose (s, w and g): ")

    print()
    print()

    # Checking the choice of the user
    if usrStrike == 's':
        print("Your choice is \"Snake\"")
        matrixIndex = [0, 1, 2]  # if s first three lists in the list
    elif usrStrike == 'w':
        print("Your choice is \"Water\"")
        matrixIndex = [3, 4, 5]  # if w second three lists in the list
    elif usrStrike == 'g':
        print("Your choice is \"Gun\"")
        matrixIndex = [6, 7, 8]  # if g third three lists in the list

    # Checking the choice of computer
    if computerStrike == 's':
        print("The computer chooses \"Snake\"")
    elif computerStrike == 'w':
        print("The computer chooses \"Water\"")
    elif computerStrike == 'g':
        print("The computer chooses \"Gun\"")

    for index in matrixIndex:
        if computerStrike == winConditions[index][1]:
            # print(index) # for testing
            if winCheckF(index) == 'W':
                winThree += 1
                print("This time your Win!")
            elif winCheckF(index) == 'D':
                drawThree += 1
                print("This time it's Draw!")
            elif winCheckF(index) == 'L':
                print("This time you Lose!")
    print() # For line gap

if winThree > 1:
    print("Congratulations you have won the match!")
elif drawThree == 3:
    print("This match has been Draw!")
else:
    print("You have lost the match!")
