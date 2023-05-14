a = "!!!Jugal!!! is a good boy" # Strings are immutable (Unchangable)
print()
print()
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Jugal", "Harry"))
print(a.split(" "), "<--")
sentence = "there is something fishy"
print(sentence.capitalize())
print(sentence.center(50))
print(a.count("Jugal"))
print(a.endswith("boy"))
print(a.endswith("Jugal", 3, 8)) #Checking if the string "Jugal" comes between the index 3, 8

testString = "Hi there, how are you?"
print(testString.find("are"))
print(testString.find("are")) # Returns -1 cause there is no string in there
print(testString.index("are")) # Similar to find() method but returns error when an absent string is put as an argument
str1 = "WelcomeToTheConsole99"
print(str1.isalnum())
# Returns true cause there is no space and other special characters
str1 = "WelcomeToTheConsole"
print(str1.isalpha())
# Returns true cause there is no space and other special characters and no numerics
print(str1.islower())
# Returs flase cause there are Upper Case letters
str1 = "\"Hello World!\"\nHow are you?"
print(str1.isprintable())
# Returns false cause there is an unprintable character which is "\n". Which cannot be printed
str1 = "    "
print(str1.isspace())
# Returns true when there is only white spaces or tabs but if there is an alphanumeric value than it returns false
str1 = "Hello World!"
print(str1.istitle())
# Retuns true cause each word is capitalize
str2 = "How are you?"
print(str2.istitle())
# Returns flase cause not every word is capitalize
print(str2.startswith("How"))
# Returns true cause str2 starts with "How"
print(str2.swapcase())
# Swapes the case of the texts
print(str2.title())
# Swapes the case of the texts to title case means capitalize each word