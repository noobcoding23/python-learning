# READING A FILE
# f = open('myfile.txt', 'r')

# # print(f)
# text = f.read()
# print(text)
# f.close()


# WRITING TO A FILE
# f = open('myfile.txt', 'w')
# f.write("Hello World! How are you?") # This will replace everything inside the file with the new text. For adding new stuff without replacing anything you have to use append() function
# f.close()

# APPENDING TO A FILE
# f = open('myfile.txt', 'a') # a for append
# f.write("Hello World! How are you?") # Everytime you run this file it will add this line to file
# f.close()

# WITH STATEMENT
# f = open('myfile.txt', 'a') 
# with open('myfile.txt', 'a'):
with open('myfile.txt', 'a') as f:
    f.write("New textline")

'''
Modes in file

There are various modes in which we can open files.

    read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

    write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

    append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

    create (x): This mode creates a file and gives an error if the file already exists.

    text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

    binary (b): used to handle binary files (images, pdfs, etc).
'''