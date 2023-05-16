import os
# print(dir(os))

if (not os.path.exists("data")): # Checking if the data folder exists or not, if not then create one
    os.mkdir("data")

# for i in range(0,100): # Creating 100 folders automatically in python
#     os.mkdir(f"data/Day{i +1}")

# for i in range(0,100): # Renaming 100 folders using forloop
#     os.rename(f"data/Day{i+1}", f"data/Tutorial {i+1}")

folders = os.listdir("data")
# print(folders) # Prins all folder's name in list format

# for folderName in folders: # Using for loop to print all the directories
#     print(folderName)
#     print(os.listdir(f"data/{folderName}"))

# os.chdir("/data") # Changes a working directory
print(os.getcwd())
