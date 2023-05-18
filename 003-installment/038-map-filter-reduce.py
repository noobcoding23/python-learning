from functools import reduce
# To use reduce function importing is necessary

#MAP
def square(x):
    return x*x

print(square(2))

l = [1, 2, 4, 6, 7, 9]
# newL = []
# for item in l:
#     newL.append(square(item)) # Normal way to do square value of a list

# Here map is an higher order function which is a function taking a function
# map(function, iterable)
newL1 = map(square, l) # This returns the type of newL
newL2 = list(map(square, l)) # This returns the same result in the loop above

print(newL1)
print(newL2) # Maped list

#FILTER
def filter_function(a):
    return a>4

# filter(function, iterable)
nwL1 = filter(filter_function, l)
# Here the function inside filter function should be giving True or False as return
nwL2 = list(filter(filter_function, l))

print(nwL1)
print(nwL2) # Filtered list if the list item is greater than 4

#REDUCE

#List of numbers
numbers = [1, 2, 3, 4, 5]
# Now what the reduce function is doing is very simple
# sum = [3, 3, 4, 5] 1+2 = 3
# sum = [6, 4, 5] 3+3 = 6
# sum = [10, 5] 6+4 = 10
# sum = 15 # The output of the below function

# calculating the sum of numbers using reduce function
def mysum(x,y):
    return x+y

# reduce(function, iterable)
sum = reduce(mysum, numbers)
print()
print()
print(sum)
print()