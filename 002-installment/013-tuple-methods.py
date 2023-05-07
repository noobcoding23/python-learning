# <--My example-->
# 
# 
nameOfPeople = ("Rohan", "Ravi", "Jugal", "Nayan")
print(nameOfPeople)
tempList = list(nameOfPeople) # Converting to list using list method
# print(tempList)
tempList.append("Vijay") # Adding a data
# print(tempList)
tempList.pop(3) # Removing a data using pop method with index number 3
# print(tempList)
tempList[1] = "Raju"
# print(tempList)
nameOfPeople = tuple(tempList) # Converting again to tuple using tuple method
print(nameOfPeople)
# 
# 
# <--My example-->

# <--Internet Example-->
#
# 
# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)
# 
# 
# <--Internet Example-->

tp1 = (1, 2, 3, 4, 5)
tp2 = (6, 7, 8, 9, 10)
tpMerge = tp1 + tp2
print(tpMerge) # Merging two tuples in a new tuple
testTp = (1, 2, 2, 3, 4, 2, 70)
print(testTp.count(2), "<-- Number of time 2 is repeated in the tuple")
print(testTp.index(2), "<-- Returns the index of 2 in the first occurence")
print(testTp.index(2, 3, 6), "<-- Returns the index of 2 in between the start and end index")# index(ELEMENT, START, END) <-Syntax
