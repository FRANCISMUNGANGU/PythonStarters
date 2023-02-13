# We use operators to manipulate the value of operands (Values/Variables)
# Types of operators
# 1. Arithmetic operators (+,-,/,*,%,**,//)
# 2. Comparison operators (>,<,<=,>=,!=,==)
# 3. Assignment Operators (=,+=,-=,*=,%=,**=,//=)
# 4. Logical Operators (and,or,not)
# # week 2
# others , membership operators / bitwise / identity operators

# Comparison operators
# equal 4 == 5 false
# less than 4 < 5 true
# greater than4 > 5 false
# not equal 4 != 5 true
# less or equal4 <= 5 true
# greater or equal4 >= 5 false

a = 4
b = 5
print("a == b : ", a == b)

print("a != b : ", a != b)

print("a < b : ", a < b)

print("a > b : ", a > b)

print("a <= b : ", a <= b)

print("a >= b : ", a >= b)


# ASSIGNMENT OPERATORS
# a = 10
#  addition a += 10, a = a + 10
# subtraction a -= 10, a = a - 10
#  multiplication a *= 10, a = a * 10
# division a /= 10, a = a / 10
# exponent a **= 10, a = a ** 10
# floor a //= 10, a = a // 10
# reminder/modulus a %= 10, a = a % 10

a = 10
a += 5
print("a += 5 : ", a)

a -= 5
print("a -= 5 : ", a)

a *= 5
print("a *= 5 : ", a)

a /= 5
print("a /= 5 : ", a)

a **= 3
print("a **= 3 : ", a)

a %= 2
print("a %= 2 : ", a)

a //= 3
print("a //= 3 : ", a)

# Logical operators
# and if both operands are true then the condition becomes true (a and b)is true. &
# or if one operand is non-zero then condition becomes true ( a or b)is true. |
# not reverses logical state of its operand !

# conditionals or control flow statements are used together with logical operators. (DECISION MAKING PROCESS)
variableCompare = 5
secondVariable = 10
# simple if
if variableCompare == 10:
    print("simple if")
else:
     print("condition not met.")
# multi condition
if variableCompare == 10:
    print("from multi condition")
elif variableCompare == 7:
    print("form the multi condition")
elif variableCompare == 6:
    print("form the multi condition")
else:
    print("no met condition")
# with logical
if variableCompare == 10 or secondVariable == 6:
    print("from or")
elif variableCompare == 5 and secondVariable == 10:
    print("from and")
else:
    print("No condition met.")

