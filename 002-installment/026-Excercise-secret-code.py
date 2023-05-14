random = 'a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z'
random = random.split(" ")
random.reverse()
# print(random) # For test
print()
print("Welcome to Encrypt&Decript!!!")
print("Here you can encrypt and decrypt your messages")


print("\n\n")
triggerStart = input("So, first select if you want to Encrypt or Decrypt your data (Answer in e, d or q for quit): ")

print("\n\n")

if triggerStart == 'e':
    print("You've chosen Encryption")
    messg = input("Then enter your message here:\n\nEnct>>>")
    messg = messg.split(" ")
    random = random * len(messg)
    # print(random) # for test
    print("\nHere is your Ecrypted message:\nCopy it and paste it wherever you want\n\n\n>>>", end="")
    for i in range(0, len(messg)):
        # print(f"{messg[i]}", end=" ")
        if len(messg[i]) < 3:
            messg[i] = messg[i][::-1] # Reversing the string
            # print(messg)
        else:
            addLast = messg[i][0] # Storing the first letter in a variable
            messg[i] = messg[i].replace(messg[i][0], "") # Replacing the first letter
            messg[i] += addLast # appending the first letter in last
            random1 = random[i:i+3]
            random2 = random[i+3:i+6]
            for x in random1:
                random1[x] += x
            print(random1)
            # messg[i] = random[i][i:i+3] + messg[i] + random[i][i+3:i+6]
            # print(messg[i])
            # print(messg[i], end="fzx") # for test
        # print(messg[i], end="")
        # if messg[i] == messg[-1]:
        #     print("", end="")
        # else:
        #     print(" ", end="")

    print("<<<\n\n")

elif triggerStart == 'd':
    print("You've chosen Decryption")
    messg = input("Then enter your message here:\n\nDect>>>")
    messg = messg.split(" ")
    print("Here is your Decrypted message:\nCopy it and paste it wherever you want\n\n\n>>>", end="")
    # print(messg) # For test
    for i in range(0, len(messg)):
        if len(messg[i]) < 3:
            messg[i] = messg[i][::-1]
            print(messg[i], "\n")
        else:
            messg[i] = messg[i][3:len(messg[i])-3]
            print(messg[i])

        # print(messg[i], end="")
        # if messg[i] == messg[-1]:
        #     print("", end="")
        # else:
        #     print(" ", end="")
    print("<<<\n\n")
elif triggerStart == 'q':
    print("\n\n")
    print("Okay! Good Bye then!")
else:
    print("\n\n")
    print("You've chosen nothing! The program will autumatically exit!")
    print("Exit!")