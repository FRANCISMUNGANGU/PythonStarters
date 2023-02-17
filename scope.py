# a variable only available inside the region it is created
# LOCAL SCOPE: variables created inside functions
# GLOBAL SCPE: variables created outside functions\
x = 200  # global variable
# global keyword makes variables global
# example of a local scope


def sample_method():
    global y
    x = 100
    y = 200
    return x + y


print(sample_method())

# what of functions inside functions


def sample_function():
    def inner_function():
        print(y)
    return inner_function()


sample_function()

