import os

fixedPath = '004-installment/'
thePath = f'{fixedPath}PNG files'

# Here exists() method is used for checking the path
if os.path.exists(thePath): # The os.path for path related methods
    print('Folder already exits!')
else:
    os.mkdir(thePath) # mkdir - make directory
    print('The folder has been created!')

print()
fileNamesList = []
fileList = []
files = os.listdir(thePath)
# print(f'The number of files is {numOfFiles}') # Test
for file in files:
    # print(os.path.splitext(file)) # The splittext() method is used for separating the file name and extension in a tuple
    fileNames, fileExtensions = os.path.splitext(file) # assigning values to two variables together
    # print(fileExtensions) # For checking the if the file extensions are there # Simply prints all the file extensions
    if fileExtensions == '.png':
        fileNamesList.append(fileNames)
        # fileList.append()
        # print(fileNames, fileExtensions, sep='') # prints only png extensions
        # print(newName, fileExtensions, sep='')
        
# print(fileNamesList)

for newName, fileNames in enumerate(fileNamesList):
    # print(f'{fileNames} --> {newName}.png')
    os.rename(f'{thePath}/{fileNames}.png', f'{thePath}/{newName+1}.png')