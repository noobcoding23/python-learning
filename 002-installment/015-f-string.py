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

txt = "My percentage in exam is {price:.2f}"
print(txt.format(price = 88.999999997))