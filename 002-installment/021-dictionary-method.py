ep1 = {1001: "Harry", 1002: "Jugal", 1003: "Nayan", 1004: "Bishal"}
ep2 = {1005: "Sangita", 1006: "Mayuri", 1007: "Bijay", 1008: "Ajay"}

ep1.update(ep2)
print(ep1)
ep1.pop(1004)
print(ep1, "<-- For removing 1004 for the area ")
ep1.clear()
print(ep1, "<--Cleared with the clear() method")
empt = {} # Creating empty dictionary
print(ep2)
ep2.popitem() # popitem() method removes the last data
print(ep2)
del ep2[1006] # del removes the data which key data is provided
print(ep2)