"""
CHAPTER 3-3 STACK
LIFO: LAST-IN-FIRST-OUT
FILO: FIRST-IN-LAST-OUT
"""

""" Stack Example """

def greet(name):
    print("hello, ", name, "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, ", name, "?")

def bye():
    print("ok bye")

greet("maggie")


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(3)

