# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline() # Readlines for reading line by line of a file
#     if not line:
#         break
#     print(line)

# f = open('003-installment/newfile.txt', 'r')
# i = 0
# while True:
#     i += 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"The mark of student {i} in Maths is: {m1}")
#     print(f"The mark of student {i} in Maths is: {m2}")
#     print(f"The mark of student {i} in Maths is: {m3}")
#     print( line)

f = open('003-installment/newfile.txt', 'w') # for writing a file
lines = ['line1\n', 'line2\n', 'line3\n'] # Here this lines are added on the newfile.txt and also is replaced the old content of the file
f.writelines(lines)
f.close()
