dic = {
   "John": "Human Being", 
   "book": "Object",
   567: "John Doe",
   77: "Neha"
}

print(dic["John"])
print(dic[77])

info = {"Name": "Jack Frost", "Age": 22, "Qualification": "BSc"}
print(info, "<--This is a dictionary")
print(info["Name"])
# print(info["Name2"]) # This will throw an error cause there is no "Name2" in the first place
print(info.get("Name"))
print(info.get("Name2"), "<--Doesn't throw any but prints None")
print(info.keys()) # Prints the dictionary keys
print(info.values()) # Prints the dictionary values
print(info.items()) # Prints the dictionary items in pair

print()
for k in info.keys():
    print(f"The value corresponding to key \"{k}\" is {info[k]}")

print()
for k, v in info.items():
    print(f"The value corresponding to the key \"{k}\" is {v}")