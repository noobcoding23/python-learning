marks = [12, 56, 45, 98, 1, 8, 47]
index = 0 # Needs to declare that index is 0
for mark in marks:
    print(mark, end=" ")
    if index == 3:
        print("<--Awsome<<", end=" ")
    index += 1 # adding 1+ to index every time
print("\n")

nMarks = [58, 6, 45, 96, 8, 12, 11]

for index, nMark in enumerate(nMarks, start=1): # Here enumerate function is giving index and value together # There can be added start but not compulsory
    print(nMark, end=" ")
    if index == 4:
        print("<--Awsome<<", end=" ")