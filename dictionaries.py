# It's an iterable used to store values in key and value pairs
# They are ordered from python 3.7 onwards
# They are changeable but do not allow duplicates
# syntax of a simple dictionary
# shoppingDictionary = {
#     key:value
# }
# dictionary values can be of different datatypes
# shoppingDictionary = {
#     "item1": "wine",
#     "item2": 1,
#     "item3": True,
# }

shoppingDictionary = {
    "item1": "bread",
    "item2": "milk",
    "item3": "flour",
}
# to get length use len()
print(len(shoppingDictionary))

# accessing a dictionary
# done by referencing key name inside square bracket
print(shoppingDictionary["item2"])
# using inbuilt method called get
x = shoppingDictionary.get("item3")
print(x)

# to get keys in ours dictionaries we use the keys() method
x = shoppingDictionary.keys()
print(x)

# if you want all values use values() method
print(shoppingDictionary.values())

# items() method returns all items in a dictionary as tuples in a list
print(shoppingDictionary.items())

# to check if keys exist in a dictionary:
check = "item1"
if check in shoppingDictionary:
    print("Yes, the item in dictionary")
else:
    print("No, item not found")

# updating a dictionary
# changing values, adding values, removing values
# changing values if specific item
# reference the key and assign a new value
shoppingDictionary["item3"] = "salt"
print(shoppingDictionary["item3"])
# we can also use update method
shoppingDictionary.update({"item2": "flour"})
print(shoppingDictionary["item2"])
# adding, reference key and assign new value
shoppingDictionary["item4"] = "sugar"
# update also used to add
shoppingDictionary.update({"item5": "eggs"})
print(shoppingDictionary.values())

# removing things: use the pop method which requires a key in the dictionary
shoppingDictionary.pop("item5")
print(shoppingDictionary.values())

# popitem() removes a random item in version 3.7 onwards
shoppingDictionary.popitem()
print(shoppingDictionary.values())

# del keyword removes item with a specified name
# del shoppingDictionary["item1"]
# print(shoppingDictionary.values())
# # clear empties the dictionary
# shoppingDictionary.clear()
# print(shoppingDictionary.values())

# coping a dictionary
# use copy inbuilt method
copyDictionary = shoppingDictionary.copy()
# dict() will allow you to do the same
dictDictionary = dict(shoppingDictionary)
print(copyDictionary)
print(dictDictionary)

# NESTED dictionaries
myFamily = {
    "child1": {
        "name": "Francis",
        "age": "36"
    },

    "child2": {
        "name": "Mary",
        "age": "24"
    },
    "child3": {
        "name": {
         "firstname": "James",
         "lastname": "Badman"
               },
         "age": "23"
    },
}
# access to nested dictionaries
# say we wanted name info on child two
# reference child 2 using the key and then get the details you want using the key
print(myFamily["child2"]["name"])
print(myFamily["child3"]["name"]["firstname"])
