# JSON syntax for storing and interpreting data
# needs to be imported to be used
# to import type, import json
import json

# converting from json to pyhton
# json.loads() : converts to python dictionary
x = '{"name":"Francis", "age": 18}'
# parse x
y = json.loads(x)
print(y)
print(type(y))
print(type(x))

# converting python to json
# json.dumps()
x = {"name":"Francis", "age": 18}
# parse x
y = json.dumps(x)
print(y)
print(type(y))
# converting python objects to JSON strings
print(json.dumps(['apple', 'cherry']))
print(json.dumps(('apple', 'cherry')))
print(json.dumps(32))
print(json.dumps(32.7))
print(json.dumps(True))

# sorting keys
x = {
    'name': "francis",
    'age': 18,
    "married": True,
    'divorced': False,
    'children':('billy'),
    "pets": None,
    'cars': [
        {"model": 'bmw m350i', "mpg": 27.5},
        {"model": 'mercedes c300', "mpg": 24.2}
    ]

}
print(json.dumps(x, indent=4, sort_keys=True))