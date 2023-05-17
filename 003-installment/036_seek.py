with open('003-installment/newtext.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in the file
    f.seek(10)
    # Read the next 5 bytes
    print(f.tell()) # Tells where the seek() is started
    data = f.read(5)
    print(data)

with open('003-installment/truncate.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(5) # Limits the number of characters can be stored in a file. Here only 'Hello' will be wrote in the truncate.txt file

with open('003-installment/truncate.txt', 'r') as f:
    print(f.read())