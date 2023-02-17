# This is a technic in python programming that will allow is to repeat tasks based of the condition
# we have two primitive loops: while loop and the for loop

# WHILE LOOP: allows us to execute a set of logic as long as a condition is true
# to print 1 to 6 using a while loop
# it needs a condition which is written using operators
# it needs a start point known as initialization counter
# incrementors increase initial value, decrementor decreases value
# incrementor stops loop, decrementor create infinite loop(might crush program) depends on condition
# start = 1
# while start < 7:
#     print(start)
#     start += 1

# to stop a loop
# SPECIAL STATEMENTS IN WHILE LOOPS
# BREAK: allows up to stop a loop even if the statement is true
start = 1
while start < 7:
    print(start)
    # here we can place the break after the logic runs
    if start == 3:
        break
    start += 1

# CONTINUE : stops current loop and continue with the next
# to exclude 3 from loop print out
start = 0
while start < 7:
    start += 1
    if start == 3:
        continue
    print(start)

# ELSE statement
# we can run block of code once when condition is no longer true
start = 1
while start < 7:
    print(start)
    start += 1
else:
    print("start is no longer less than 7")

# FOR LOOP: popular for looping over sequences/collections(iterables and strings)
# allows execution of a set of statements on each item in collection
fruits = ["apple", "banana", "cherry"]
tupleFruits = ("apple", "banana", "cherry")
for x in fruits:
    if x == "apple":
        print("I have reached apple")
    else:
        print(x)

for x in tupleFruits:
    print(x)
# loop in string
for x in "Francis":
    print(x)
# the range function
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)
# range with increment
for x in range(2, 10, 3):
    print("Last loop " + str(x))

# ELSE IN, in FOR LOOPS:specifies block of code to execute when loop is done
for x in range(5):
    print(x)
else:
    print("Loop is finished")
# NESTED LOOP
loopOne = ["red", "mango", "Francis"]
loopTwo = ["a", "b", "c"]
for x in loopOne:
    for y in loopTwo:
        print(x, y)

# PASS STATEMENT: avoid errors when loop body is empty
emptyVariable = ""
for x in [1, 2, 3]:
    pass
