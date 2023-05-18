a = [1, 2, 3]
b = [1, 2, 3]
c = 2
d = 2
e = None
# Pythond stores same constant value in same memory place and point the variable name to the same location
# That's why when its checked with is keyword it returns true
# This can be true with datatypes which are immutable (unchangable)
# Such as tuple, constants

print(a is b) # Checks exact location of object in memory
print(a == b) # Checks value only
print(c is d)
print(e is None)

