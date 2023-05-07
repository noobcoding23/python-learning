tup = (1, 5, 7, "Green", True) # Different types of data can be stored in tuple
print(type(tup), tup)
tup = (1)
print(type(tup), tup, "<- this becomes an integer why???")
tup = (1,)
print(type(tup), tup, "<- this becomes a tuple") # To tell python that you are creating a one data tuple you have to use one comma after the data
print()
print("#"*50)
print("<--Tuples are unchangeble/immutable in nature. So there is no method to change data in a tuple-->")
print("#"*50)
print()
tupL = (56, 77, 89)
print(tupL[0], end=" || ") # Tuple index printing
print(tupL[1], end=" || ")
print(tupL[2])
print()
print("#"*50)
print("<--Indexing in the tuple is same as in the list-->")
print("#"*50)
print()

if 56 in tupL:
    print("Yes 56 is present in tupL")

tupL2 = tupL[1:2] # Tuple slicing is possible but the original one doesn't change but it creates a new one
print(tupL2, "<-- This is a sliced tuple")