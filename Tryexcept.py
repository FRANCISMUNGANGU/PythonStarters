# try tests block for error
# except: handling of error
# else: runs without error
# finally: runs regardless of error

# Exception handling:
x = -1
try:
    print(x)
except: 
    print("An error occurred, check if x is defined")
else:
    print(str(x) + " from else")
finally:
    print("Finally block")

# Raise keyword
# works with a condition. if condition is met, raises exception message/ error message
if x < 0:
    raise Exception("sorry x should not be less than zero")
# raise Typeerror("sorry x should not be less than zero") will return same result

