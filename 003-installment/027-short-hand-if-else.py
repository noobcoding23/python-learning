a = 4400
b = 5500
print("A") if a>b else print("=") if a==b else print("B")

print("B>") if b>a else "" # here quotation after else is compulsory

c = 9 if a>b else 0 # can be used when assigning a value

print(c)