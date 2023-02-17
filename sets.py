# Sets allow us to store multiple items in a single variable
# they are unordered unchangeable and un-indexed
# use {} to define
# cannot be duplicated
# True and 1 are considered the same
# allow different data types :shoppingSet = {"bread", "sugar", "salt", True, 1} mixed
# shoppingSet = {"bread", "sugar", "salt"} same datetype
shoppingSet = {"bread", "sugar", "salt"}
print(shoppingSet)
# length of set
# use len()
print(len(shoppingSet))

# accessing items: we use a loop:repetitive task
# for in
for x in shoppingSet:
    print(x)
# to check if item exists in set
check = "bread"
print(check in shoppingSet)

# updating a set : adding and removing
# adding
# you cannot change items, but you can add new items add()
shoppingSet.add("flour")
print(shoppingSet)
# adding items from another set to a current set
juiceFlavors = {"mango", "apple", "passion"}
shoppingSet.update(juiceFlavors)  # adds to the end
print(shoppingSet)
# add other iterables
simpleList = ["oranges", "soap", "beer"]
simpleTuple = ("forks", "spades")
set2 = {"item2", "item3"}
shoppingSet.update(simpleList)
shoppingSet.update(simpleTuple)
shoppingSet.update(set2)
print(shoppingSet)
# removing
shoppingSet.remove("spades")
shoppingSet.discard("forks")
print(shoppingSet)

# x = shoppingSet.pop()  # removes random element
# print(x)
# shoppingSet.clear()  # empties set
# print(shoppingSet)
# del shoppingSet
# print(shoppingSet)

# https://www.w3schools.com/python/python_sets_methods.asp

# joining tuples, update, union:creates new set
set3 = {"item4", "item5", 5}
set4 = shoppingSet.union(set3)
print(set4)
# intersection_update: only keeps items in both sets
x = {"apple", "banana"}
y = {"microsoft", "apple"}
x.intersection_update(y)
print(x)
# intersection:creates new set
x = {"apple", "banana"}
y = {"microsoft", "apple"}
z = x.intersection(y)
print(z)
# symmetric_difference_update: elements not present in both sets
x = {"apple", "banana"}
y = {"microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
# symmetric_difference:creates new set
x = {"apple", "banana"}
y = {"microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
# True and 1 are same, False and 0 are same
x = {"apple", "banana", True, False}
y = {"microsoft", 1, 2, "apple", 0}
z = x.symmetric_difference(y)
print(z)
