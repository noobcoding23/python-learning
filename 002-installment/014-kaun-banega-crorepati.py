opAlpha = ['[A]', '[B]', '[C]', '[D]']
questions = ["What is the name of the Indian scientist who won the Nobel Prize in Physics in 1930 for his work on scattering of light?", "Which Indian state has the highest population density?", "Who is the current Chief Justice of India?", "Which Indian city is known as the 'Manchester of India'?", "Which Indian musician was posthumously awarded the Bharat Ratna, India's highest civilian award, in 2001?", "Which Indian state has the longest coastline?", "Who is the only Indian woman to have won an Olympic gold medal in individual sports?", "Which Indian freedom fighter was known as the 'Iron Man of India'?", "Which Indian state has the largest forest cover?", "Who was the first Indian woman to be elected as the President of the United Nations General Assembly?", "Which Indian state is the largest producer of coffee?", "Who is the first Indian woman to win a silver medal at the Olympics?"]

rightAnswers = ["C.V. Raman", "Bihar", "N.V. Ramana", "Ahmedabad", "Bismillah Khan", "Gujarat", "Abhinav Bindra", "Sardar Vallabhbhai Patel", "Madhya Pradesh", "Vijaya Lakshmi Pandit", "Karnataka", "P.V. Sindhu"]

# for i in range (0, 12):
#     print(questions[i], end="\n\n")
mcqOpt = [[
    "Vijay P. Bhatkar", # Computer scientist and architect of India's first supercomputer
    "Raj Reddy",
     "C.V. Raman", # Artificial intelligence and robotics researcher
    "Sabeer Bhatia", # Co-founder of Hotmail, a popular email service
], ['Assam', 'Madhyapradesh', 'Uttarpradesh', "Bihar"], ["N.V. Ramana",
    "Justice H.J. Kania", # First Chief Justice of India
    "Justice M. Patanjali Sastri", # Second Chief Justice of India
    "Justice Y.V. Chandrachud", # Fourteenth Chief Justice of India
], ['Kolkata', 'Banglore', 'Guwahati', "Ahmedabad"], [
    "A.R. Rahman", # Composer and music director known for his work in Bollywood and Hollywood
    "Lata Mangeshkar", # Playback singer who has recorded songs in over 36 Indian languages
    "Bismillah Khan",
    "Ustad Zakir Hussain", # Tabla virtuoso and composer who has collaborated with several Western musicians
], ['Gujarat', 'West Bengal', 'Kerala', 'Madhyapradesh'], [
    "PV Sindhu", # Badminton player and Olympic medalist
    "Abhinav Bindra",
    "Mithali Raj", # Cricketer and former captain of the Indian women's cricket team
    "Mary Kom", # Boxer and Olympic medalist
], ['Netaji Subhash Chandra Bose', "Sardar Vallabhbhai Patel", 'Bhagat Sigh', 'Bal Gangadhar Tilak'], ['Uttarpradesh', 'Tamilnadu', 'Bihar', "Madhya Pradesh"], [
    "Mamata Banerjee", # Chief Minister of West Bengal and leader of the Trinamool Congress party
    "Nirmala Sitharaman", # Minister of Finance and Corporate Affairs in the Government of India
    "Smriti Irani", # Minister of Women and Child Development and Minister of Textiles in the Government of India
    "Vijaya Lakshmi Pandit"
], ['Tamilnadu', "Karnataka", 'Kerala', 'Assam'], [
    "Mithali Raj", # Cricketer and former captain of the Indian women's cricket team
    "Dipa Karmakar", # Artistic gymnast and the first Indian female gymnast to qualify for the Olympics
    "P.V. Sindhu",
    "Saina Nehwal", # Badminton player and former World No. 1
]
]
# mcqOpt[0].append(rightAnswers[0])
# print(mcqOpt[0][3])
# for opt in range(0,12):
#     mcqOpt[opt].append(rightAnswers[opt])
# print(mcqOpt)

# Define a function for question and answer

# Define a function for question and answer
# fetchQnA(1)
print()
print()
start = input("Do you want to be a crorepati? (answer in 'y' or 'n'):")
win = 0
if start=='y':
    for x in range(0,12):
        print()
        print()
        print("Here's your Question No", "[", x+1, "]")
        print()
        print(questions[x])
        print()
        print("Here are your options:")
        print()
        for opt in range(0,4):
            print(opAlpha[opt], mcqOpt[x][opt])
        print()
        print()
        ans = input("Answer the question in (a, b, c or d): ")
        if ans == 'a':
            if mcqOpt[x][0] == rightAnswers[x]:
                if x == 11:
                    print("Wow you have won the final round and 60000000, \"Kya kijiyega itne paiso ka?\"")
                else:
                    win += 1
                    print("Correct Answer! You've won", win*5000000, "Rupees")
                    print()
                    print("#"*20)
                    print()
                    secondaryConti = input("Do you want to continue? (Answer in 'y' or 'n'): ")
                    if secondaryConti == 'n':
                        print("Okay bye than!")
                        break
            else:
                if x == 0:
                    print()
                    print()
                    print("Worng answer! You've lost all the money! Wait you didn't get even any money!")
                    break
                elif x == 11:
                    print("Well it's sad that you have to return empty handed in this point!")
                else:
                    print()
                    print()
                    print("Worng answer! You've lost all the money")
                    break
        elif ans == 'b':
            if mcqOpt[x][1] == rightAnswers[x]:
                if x == 11:
                    print("Wow you have won the final round and 60000000, \"Kya kijiyega itne paiso ka?\"")
                else:
                    win += 1
                    print("Correct Answer! You've won", win*5000000, "Rupees")
                    print()
                    print("#"*20)
                    print()
                    secondaryConti = input("Do you want to continue? (Answer in 'y' or 'n'): ")
                    if secondaryConti == 'n':
                        print("Okay bye than!")
                        break
            else:
                if x == 0:
                    print()
                    print()
                    print("Worng answer! You've lost all the money! Wait you didn't get even any money!")
                    break
                elif x == 11:
                    print("Well it's sad that you have to return empty handed in this point!")
                else:
                    print()
                    print()
                    print("Worng answer! You've lost all the money")
                    break
        elif ans == 'c':
            if mcqOpt[x][2] == rightAnswers[x]:
                if x == 11:
                    print("Wow you have won the final round and 60000000, \"Kya kijiyega itne paiso ka?\"")
                else:
                    win += 1
                    print("Correct Answer! You've won", win*5000000, "Rupees")
                    print()
                    print("#"*20)
                    print()
                    secondaryConti = input("Do you want to continue? (Answer in 'y' or 'n'): ")
                    if secondaryConti == 'n':
                        print("Okay bye than!")
                        break
            else:
                if x == 0:
                    print()
                    print()
                    print("Worng answer! You've lost all the money! Wait you didn't get even any money!")
                    break
                elif x == 11:
                    print("Well it's sad that you have to return empty handed in this point!")
                else:
                    print()
                    print()
                    print("Worng answer! You've lost all the money")
                    break
        elif ans == 'd':
            if mcqOpt[x][3] == rightAnswers[x]:
                if x == 11:
                    print("Wow you have won the final round and 60000000, \"Kya kijiyega itne paiso ka?\"")
                else:
                    win += 1
                    print("Correct Answer! You've won", win*5000000, "Rupees")
                    print()
                    print("#"*20)
                    print()
                    secondaryConti = input("Do you want to continue? (Answer in 'y' or 'n'): ")
                    if secondaryConti == 'n':
                        print("Okay bye than!")
                        break
            else:
                if x == 0:
                    print()
                    print()
                    print("Worng answer! You've lost all the money! Wait you didn't get even any money!")
                    break
                elif x == 11:
                    print("Well it's sad that you have to return empty handed in this point!")
                else:
                    print()
                    print()
                    print("Worng answer! You've lost all the money")
                    break
        else:
            print()
            print()
            print("Worng answer! You've lost all the money")
            break
        
else:
    print("OK! Bye then!")
    print()
    print()
