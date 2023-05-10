setI = {2, 4, 2, 6} # Set is an unordered collection of dat which means the representation of the datas are always in random format
print(setI, "<--This is a set") # Set removes the repeated entries
setII = {"Luffy", 9, 16, True, 9, 5.666} # Can be stored different types of data
print(setII, "<--Here the order of data is not the same as in the code")

testSet = {} # This is actually an empty dictionary
print(type(testSet))
testSetI = set() # To create an empty set you have to do this
print(type(testSetI))
print()

for value in setII:
    print(value)