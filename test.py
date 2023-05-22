# l = ["hello", "World!", "How"]
# print(l)
# l[2] = "are"
# l[2] = l[2][::-1]
# print(l)
# l[0] = l[0].replace(l[0][0], "")
# print(l)
# def replc(x):
#     if "!" in x:
#         return x.replace("!", "x")
# a = "Hello!"
# print(replc(a))
# a = "HellofxWorld!fxHowfxarefxyou?"
# a = a.split("fx")
# # print(a[0])
# # print(a[0][:2])
# # print(a[0].replace(a[0][:2], ""))
# print(a)
# newa = ""
# for x in range(len(a)):
#     newa += a[x]
# print(newa)
# char = "Hello World!"
# for a in char:
#     print(a, end="")
# print(newa)
# ran = ""
# for a in range(0, len(newa)):
#     ran += newa[len(newa)-1-a]
# print(ran)
# store = ran[0:3] + "MM" + ran[4:7]
# print(store)
# print(store[-1])
supMat = ['Jugal', 'Kishor', 'Das']
matrix = [0, 1, 2]
for item in matrix:
    print(supMat[item])