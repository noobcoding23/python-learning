# ----------List Methods in python------------

l = [1, 77, 12, 99, 17, 2]
print(l)
l.reverse()
print(l, "<- The list in reverse order")
l.append(7) # This method just adds a new data to a list
print(l, "<- Appended list")
l.sort()
print(l, "<- Sorted list low->high")
print(l.index(99)) # Gives the index number of position of 99 according to the above list
l.sort(reverse=True)
print(l, "<- Sorted list reverse order")

listNum2 = [23, 77, 67, 88, 77, 67]
print(listNum2.count(77), "<- Here 77 is repeated two times")
print(listNum2)
m = listNum2
m[0] = 69
print(listNum2) # When m list replaces a data the listNum2 also changes with m
m = listNum2.copy()
m[0] = 23
print(listNum2) # Using copy method, now it doesn't changes the listNum2 while replacing a number in the m list
listNum2.insert(1, 99) # Here 99 is inserted in the index 1
print(listNum2)

l.extend(listNum2) # Using this the listNum2 list dataset is added to l list
print(l)
newL = [55, 66, 77]
k = newL + listNum2 # Two lists are merged together in the new list called k
print(k)