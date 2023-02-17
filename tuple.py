# Tuples store multiple items in a single variable.
# They are ordered but unchangeable
# defined by : define with round brackets
shoppingTuple = ("Bread", "sugar", "salt", "Bread", "sugar")
print(shoppingTuple)
# lists() converting tuple to list
# They are indexed : start is at 0
# they also allow duplicates
# to get the length of a tuple use len ()method
print(len(shoppingTuple))
# tuple with one item: define by placing a comma
tupleOne = ("bread",)
# tuples can have same or different datatypes
tuple1 = (1, 2, 3)
tuple2 = ("string", 1, True, False, "another string")
type(tuple1)
# Access to a tuple
# done by referencing the index number
print(shoppingTuple[0])
# negative indexing
print(shoppingTuple[-1])
# range
print(shoppingTuple[2:5])
# search first indexing range
print(shoppingTuple[2:])
# search last index
print(shoppingTuple[:5])
# search negative indices
print(shoppingTuple[-4:-1])  # searches from end of then tuple

# checking if item exists in a tuple
search = "Milk"
if search in shoppingTuple:
    print("yes " + search + " is in tuple")
else:
    print("no " + search + " in tuple")

# Updating a tuple
# if you want to add remove or change items in a tuple use this hack around
# convert tuple to list then use list method to modify items then convert list to a tuple

# adding items
tempList = list(shoppingTuple)
tempList[0] = "Milk"
# convert back
shoppingTuple = tuple(tempList)
print(shoppingTuple)
# adding new items
tempList.append("Flour")
shoppingTuple = tuple(tempList)
print(shoppingTuple)
# adding tuple to a tuple
tuple3 = "oranges",
shoppingTuple += tuple3
print(shoppingTuple)
tempList = list(shoppingTuple)
# remove items
# convert to list then use remove, pop
tempList.remove("oranges")
del tempList[0]
shoppingTuple = tuple(tempList)
print(shoppingTuple)

# delete a tuple completely
# del shoppingTuple

# Unpacking a tuple : making an item in a tuple act as an independent variable
(sugar, salt, bread, sugar, flour) = shoppingTuple
print(sugar)
print(salt)
print(bread)
print(sugar)
print(flour)
(sugar, salt, *bread) = shoppingTuple  # if variables are less than number if items in a tuple use an * to package the remaining values as a list
print(bread)
(*sugar, salt, bread) = shoppingTuple
print(sugar)

# replicate values in a tuple
duplicateTuple = shoppingTuple * 2
print(duplicateTuple)

fruits = ("apple", "bananas", "cherry", "kiwi", "avocado", "mango")
x = fruits.count("apple")  # shows number of times a value appears in a tuple
y = fruits.index("cherry")  # searches for the first occurrence in a tuple value
print(x)
print(y)
