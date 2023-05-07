marks = [46, 38, 44, "John Doe", True, 48] # Can be added different types of datatype
print()
print(marks)
print(type(marks)) # Printing the datatype of marks
print(marks[0], end=" - ") # Using index to print only one data inside the list
print(marks[1], end=" - ")
print(marks[3], end=" - ")
print(marks[2], end=" - ")
print(marks[4])

print(marks[-3], end=" - ") # Negative indexing
print(marks[len(marks)-3], end=" - ") # Positive indexing but the result will be the same
print(marks[2])

if 50 in marks:
    print(True)
else:
    print(False)

if "38" in marks: # There is no string 38 in Marks but number 38
    print(True)
else:
    print(False)

if "Doe" in "John Doe": # Same this is also apply for a string
    print(True)
else:
    print(False)

print(marks) # Printing marks list full
print(marks[:]) # Printing marks list full
print(marks[1:-1]) # Index printing start and end negative index
print(marks[1:6]) # Index printing start and end positive index
print(marks[0:5:2]) # Using JumpIndex in list which skips the data inside list

# List comprehension
lst = [i for i in range(10)] # Generating List
print(lst)
lst = [i*i for i in range(10)] # Adding extra parameters in list
print(lst)
lst = [i*i for i in range(10) if i%2==0] # Adding conditions in list
print(lst)

# ----------List Methods in python------------

