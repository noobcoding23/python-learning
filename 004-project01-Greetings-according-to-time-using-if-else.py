import time
timeStamp = int(time.strftime("%H"))
# timeStamp = 22 # Testing if is it working or not
# print(timeStamp + 1) # Testing if int() is working!
goodMor = "Hey there! Good Morning!"
goodAft = "Hey there! Good Afternoon"
goodEve = "Hey there! Good Evening!"
goodNig = "Hey there! Good Night!"
realTime = time.strftime("%I:%M %P")
print()
print()
print()
print("#######  The current time is ", realTime, "  #######")

if (timeStamp >= 5): # if the time is 5 AM or later
    if (timeStamp < 12): # but not later than 12 PM
        print("________________________________________________")
        print()
        print("#"*12, goodMor, "#"*12) # it's morning
    else:
        if(timeStamp < 17): # if the time is 12 PM or later but not later than 5 PM
            print("________________________________________________")
            print()
            print("#"*12, goodAft, "#"*12) # it's afternoon
        elif (timeStamp < 21): # 5 PM or later but not later than 9 PM
            print("________________________________________________")
            print()
            print("#"*12, goodEve, "#"*12) # it's evening
        else: # after that it falls under night
            print("________________________________________________")
            print()
            print("#"*12, goodNig, "#"*12) # it's night
else: # before 5 AM its falls under night
    print("________________________________________________")
    print()
    print("#"*12, goodNig, "#"*12) # it's night
