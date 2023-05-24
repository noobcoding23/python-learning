def welcome(fx):
    def mfx(*args, **kwargs): # For function with arguments the *args and **kwargs are neccessary
        print("Welcome to Addition program!")
        print()
        fx(*args, **kwargs)
        print()
        print("Ok bye!")
    return mfx

@welcome
def hello():
    print("Hello World!")

hello()

# welcome(hello)() # this can be also used instead of the above block of code
@welcome
def addition(a, b):
    print(f"The addition of {a} and {b} is: {a+b}")
    # print(a+b)

addition(45, 77)

# Best example of decorators

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b