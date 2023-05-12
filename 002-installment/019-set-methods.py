s1 = {1, 2, 4, 6, 7}
s2 = { 6, 11, 2, 9, 3}
print(s1)
print(s2)
print(s1.union(s2), "<--Union of the above two sets")
s1.update(s2)
print(s1, "<- updated s1", s2)
cities = {"Guwahati", "Kolkata", "Delhi"}
cities2 = {"Mumbai", "Guwahati", "Banglore", "Kolkata"}
print(cities, "<--Cities")
print(cities2, "<--cities2")
cities3 = cities.intersection(cities2)
print(cities3, "<--Intersection")
# print(cities, "<--This is")
cities.intersection_update(cities2)
print(cities, "<--Intersection Update")
cities3 = cities.symmetric_difference(cities2)
print(cities3, "<--Symmetric Difference")
print(cities.isdisjoint(cities2), "<--There is something common in both sets") # Tells if two sets have any common object or not. Returns true when there is no common object
print(cities.issuperset(cities2), "<--Not a superset of") # Tells if a set is a superset of a set or not. Returns false it isn't
print(cities.issubset(cities2), "<--is a subset of") # Tells if a set is a subset of a set or not. Returns false it isn't

print(cities)
cities.add("Delhi")
print(cities, "<--Delhi is added")
cities.remove("Kolkata") # Throws an error if ther is no Kolkata
print(cities, "<--Kolkata is removed")
cities.discard("Tokyo") # Doesn't throws an error if there is no Tokyo
print(cities)

fruits = {"Mango", "Apple", "Tomato", "Pineapple"}
fruitRem = fruits.pop()
print(fruits)
print(fruitRem)

if "Mango" in fruits:
    print("Yes! There is Mango")
else:
    print("No! There is no Mango")

fruits.clear()
print(fruits) # Which removes the whole set datas

del cities # Removes a set entirely throws error when tried to print

