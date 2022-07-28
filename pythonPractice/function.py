#global variable
x = "awesome"


def myfunc():
    # local variable
    x = "fantastic"
    # global keyword, variable belongs to global scope
    global y
    y = "great"
    print("Python is "+x)


myfunc()

print("Python is " + x)
print("Python is " + y)
