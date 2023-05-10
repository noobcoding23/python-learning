text = "Hey there! My name is {} and I am from {}"
text1 = "Hey there! My name is {1} and I am from {0}"
name = "Jugal"
country = "India"
print(text)
print(text.format(name, country)) # Replacing the {} to a variable
print(text.format(country, country)) # Replacing the {} to a variable
print(text.format(country, name)) # Replacing the {} to a variable
print(text1.format(country, name)) # Replacing the {0}, {1} to a variable <-- Here we have done the indexing
print(f"Hello my name is {name}") # Replacing with variables and f-string
print(f"Hello my name is {{name}}") # When use double curly braces it doesn't replaces the {name} rather print it like it is

txt = "My percentage in exam is {price:.2f}"
print(txt.format(price = 88.999999997))

price = 88.09999
txt = f"My percentage in exam is {price:.2f}"
print(txt)
print("30*2")
print(type(f"{30*2}"),f"{30*2}") # Calculations can be done with f string