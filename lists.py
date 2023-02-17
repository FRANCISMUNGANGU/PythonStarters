# Lists store multiple items in a single variable
# Items can be stored in : tuples, sets, dictionaries and sets
shoppingBasket = ["kales", "flour", "sugar", "kales", "flour", "sugar"]
# Features of lists items
# 1:They are ordered changeable and allow duplicate values
# 2:They are indexed: start counting from 0
# 3:They can be accessed, added, removed and changed

# Accessing list items.
# List items are accessed by referring to their index numbers
print(shoppingBasket[0])
# Negative indexing: start from the end
print(shoppingBasket[-1])
# range if indexes/indices: ranges are specified by  having start and end position
print(shoppingBasket[2:5])  # ranges use the positional flow only removing the elements in the start
print(shoppingBasket[:4])  # if I give end element,it returns the first n elements : n is the integer given
print(shoppingBasket[2:])  # if I give start element,it removes the first n elements
print(shoppingBasket[-4:-2])  # specify negative indices if you want to start the access from the end of the list

# Checking for items im a list
# We use keyword in

x = input("Check basket for this item : ")
if x in shoppingBasket:
    print("yes, " + x + " in basket")
else:
    print("no " + x + " in basket")

# Changing list items
# Done by referring to the index and replace the value by assigning a new one
shoppingBasket[3] = "soap"
shoppingBasket[4] = "bread"
shoppingBasket[5] = "cooking oil"
print(shoppingBasket)

# Change a range of item values
# Define a list with new values and refer to the index number where you want inserted
shoppingBasket[1:4] = ["apples", "oranges", "juice"]
print(shoppingBasket)
# How to add/ insert
# To insert new item use : insert() method and refer to index and new value of item
shoppingBasket.insert(0, "spinach")
print(shoppingBasket)
# append
shoppingBasket.append("cereals")  # adds item to end of list
# extend: in python it joins two lists together
toolShopping = ["hammers", "screws", "screwdrivers"]
shoppingBasket.extend(toolShopping)
print(shoppingBasket)

# you can also add other iterables : tuples, sets, lists, dictionaries
# example of a tuple
tupleExample = ("kiwi", "gel")
shoppingBasket.extend(tupleExample)
print(shoppingBasket)
# remove items in lists
# use remove to remove known items
shoppingBasket.remove("bread")
print(shoppingBasket)
# pop method together with index position.
shoppingBasket.pop(1)
#  If index is not specified it removes last item
shoppingBasket.pop()
print(shoppingBasket)

# delete using del keyword
del shoppingBasket[2]
print(shoppingBasket)
# to empty/remove everything from a list use clear method
shoppingBasket.clear()
print(shoppingBasket)


