print()
print("_"*7, "^"*7, "===Program Start===", "^"*7, "_"*7 )
print()
print()
print()
# Start of functions
def calculateGmean(a, b): # A function is created for calculating Geometrical Mean
    mean = (a*b)/(a+b)
    print(mean)

a = 8
b = 9
# gmean1 = (a*b)/(a+b) # Functions helps you to keep your code blocks DRY (Donot Repeat Yourself)
# print(gmean1)
calculateGmean(a, b) # The function is being used for the above values for 'a' and 'b'

c = 7
d = 6
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c, d) # The variables can be changed or replace depending on your needs

def isGreater(a, b):
    pass # Pass is used for leaving a function body to be completed in later