# factorial(5) = 5*4*3*2*1

#  factorial(n) = n * factorial(n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
# How does the above mentioned function works?
# The is here...
# factorial(5) =
# 5 * factorial(4)
# 4 * factorial(3)
# 3 * factorial(2)
# 2 * factorial(1) <-- factorial(1) is actually 1 according to above mentioned function so..
# 2 * 1

print(factorial(5))

# Testing how does Fibbonacci
def fibboNacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibboNacchi(n-1) + fibboNacchi(n-2)

print(fibboNacchi(11)) # Returns 89