def average1(a, b=1):
    print("The average is", (a+b)/2)
def average(a=9, b=1):
    print("The average is", (a+b)/2)
average() # Returns 5 according to the valuew of a and b inside the functions
average(5, 15) # Returns 10 cause the value assigned her will replace the mentioned above values of  a, b
average(1) # Here a=1 and the value of b is the default value which is mentioned above
average(b=1) # Here value of b is changed and the value of a is the default value
average(b=5, a=5) # Here the order of a and b is changed thogh still its working
average1(a=9) # Here it is compulsory to give value to a cause there is no value is assigned to a when this function was defined

def averageMulti(*number): # Here is number is a tuple which saves multiple numbers
        sum = 0
        for i in number:
             sum += i # This block of code helps in addition of the numbers
        return sum/len(number) # Using return so that the result can be stored in a variable
        return 7 # This return is being ignored by the function cause the first one is the one with the priority
c = averageMulti(5,6,7) # Here averageMulti is calling funtion
print("The average of the numbers is ",c)