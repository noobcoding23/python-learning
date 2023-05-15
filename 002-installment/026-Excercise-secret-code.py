print()
print("Welcome to Encrypt&Decript!!!")
print("Here you can encrypt and decrypt your messages")


print("\n\n")
triggerStart = input("So, first select if you want to Encrypt or Decrypt your data (Answer in e, d or q for quit): ")

print("\n\n")

# Encryption start form here
if triggerStart == 'e':
    print("You've chosen Encryption")
    messg = input("Then enter your message here:\n\nEnct>>>")

    # for creating 3 random character for first and last part
    messgRan = messg.replace(" ", "")
    newMessgRan = ""
    for spl in range(0, len(messgRan)):
        newMessgRan += messgRan[len(messgRan)-1-spl]
    # print(newMessgRan) # for test
    # for creating 3 random character for first and last part

    messg = messg.split(" ")
    print("\nHere is your Ecrypted message:\nCopy it and paste it wherever you want\n\n\n>>>", end="")
    for i in range(0, len(messg)):
        # print(f"{messg[i]}", end=" ")
        if len(messg[i]) < 3:
            messg[i] = messg[i][::-1] # Reversing the string
            # print(messg[i], end=" ") # for test
        else:
            addLast = messg[i][0] # Storing the first letter in a variable
            messg[i] = messg[i].replace(messg[i][0], "") # Replacing the first letter
            messg[i] += addLast # appending the first letter in last
            messg[i] = newMessgRan[0:3] + messg[i] + newMessgRan[4:7]
            # print(messg[i], end=" ") for test
        print(messg[i], end="")
        if messg[i] == messg[-1]: # This conditions were written for the last space removal
            print("", end="")
        else:
            print(" ", end="")

    print("<<<\n\n")

elif triggerStart == 'd':
    print("You've chosen Decryption")
    messg = input("Then enter your message here:\n\nDect>>>")
    messg = messg.split(" ")
    print("\nHere is your Decrypted message:\nCopy it and paste it wherever you want\n\n\n>>>", end="")
    # print(messg) # For test
    for i in range(0, len(messg)):
        if len(messg[i]) < 3:
            messg[i] = messg[i][::-1]
            # print(messg[i], "\n") # for test
        else:
            messg[i] = messg[i][3:len(messg[i])-3]
            messg[i] = messg[i][-1] + messg[i][:-1]
            # print(messg[i]) # for test

        print(messg[i], end="")
        if messg[i] == messg[-1]:  # This conditions were written for the last space removal
            print("", end="")
        else:
            print(" ", end="")
    print("<<<\n\n")
elif triggerStart == 'q':
    print("\n\n")
    print("Okay! Good Bye then!")
else:
    print("\n\n")
    print("You've chosen nothing! The program will autumatically exit!")
    print("Exit!")