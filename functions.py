# Function is a simple block of organised and reusable code that performs a single or return function
# how to define functions in python
# define using (def) followed by function name, then parentheses then colon
# To call use function name then a set of parentheses
# functions called in order of execution




def greeting ():
# write logic
# to end function wrire RETURN
    message = print("Hello from greeting")
    return message
greeting() #call to a function
# Functions in python can have parameters:information that a code needs in its execution
message = "Hello from user"
def greeting_from_user(greeting):
    print(greeting)
    return
greeting_from_user(message)
# multiple parameters
def simple_add(num1,num2):
    print(int(num1) + int(num2))
    return
simple_add(1,1)
# default arguments: initialises parameters within a default value
def default_arguments(num1,num2 = 1):
    print(int(num1) / int(num2))
    return
default_arguments(20/10)
# SCOPE OF VARIABLE IN A FUNCTION
# global variables found outside function and accessible to all functions
# Local variables found inside function and accessible to the function it is found in
#
result = 0 # global variable
def sum(num1,num2):
    message_local = "The result is " # local variable
    result = num1 + num2
    print(message_local + str(result))
    return
def divison(num1,num2):
    result = num1 / num2
    print(str(result))
    return
sum(10,10)
divison(10,10)
#
# # ANONYMOUS FUNCTIONS:not declared by def
# # created using lambda keyword
# # take a number of arguments but can print one result in form of a expression
# # we can use print method directly when writing lambda
# # can only access global variables and written parameters
# # to work with them well store lambda inside a variable
#
#
#
#
#
sum = lambda num1,num2: num1 + num2
print("value of", sum(10,10))


