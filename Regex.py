# means regular expressions: sequence of characters that form a pattern
import re
# using Regex to see if strings contain a pattern

text = "It is sunny today"
# search regex method: returns match object of there is match in the string
# in regex ^ means start with
# in regex $ means end with
# * indicates zero or more occurrences
# . indicates any
x = re.search("^It.*$", text)
print(x)
# find all
# returns a list with all possible matches
x = re.findall("raining", text)
print(x)
# split: returns list where strings are split at each match
x = re.split("\t", text)
print(x)
x = re.split("\s", text)
print(x)
# sub: replaces search term with term of choice
x = re.sub("\s", "4", text)
print(x)
# match: equivalent to search