l = ["hello", "World!", "How"]
print(l)
l[2] = "are"
l[2] = l[2][::-1]
print(l)
l[0] = l[0].replace(l[0][0], "")
print(l)
def replc(x):
    if "!" in x:
        return x.replace("!", "x")
a = "Hello!"
print(replc(a))
a = "HellofxWorld!fxHowfxarefxyou?"
a.split("fx")
# print(a[0])
# print(a[0][:2])
# print(a[0].replace(a[0][:2], ""))
print(a)
for x in a:
    a += x
print(a)