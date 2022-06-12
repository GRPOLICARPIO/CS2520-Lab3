# Name: Gabriel Policarpio
# Lab 3 - Task 1
# This program determines whether a number is negative, positive, or zero and displays 1, -1, or 0

def posNegZero(x) :
    if x > 0 :
        return "1"
    elif x < 0 :
        return "-1"
    else :
        return "0"

# Makes a call to these three specific values, as stated in the instructions
print(posNegZero(-5))
'''
Output:
-1
'''
print(posNegZero(0))
'''
Output:
0
'''
print(posNegZero(6.5))
'''
Output:
1
'''

# User input
x = float(input("Enter a number: "))
print(posNegZero(x))

# This program contains a function that calculates both the square and cube of numbers
def sqrCube(n, m) :
    n = n ** 2
    m = m ** 3
    return n, m

print(sqrCube(5, 3))

# Makes a call to these five specific set of values, as stated in the insructions
print(sqrCube())
'''
Output:
TypeError: sqrCube() missing 2 required positional arguments: 'n' and 'm'
'''
print(sqrCube(4))
'''
Output:
TypeError: sqrCube() missing 1 required positional argument: 'm'
'''
print(sqrCube(3, 5))
'''
Output:
(9, 125)
'''
print(sqrCube(n=4, m=2))
'''
Output:
(16, 8)
'''
print(sqrCube(n=4, 2))
'''
Output:
    print(sqrCube(n=4, 2))
                        ^
SyntaxError: positional argument follows keyword argument
'''

# Name: Gabriel Policarpio
# Lab 3 - Task 2
# This program takes a string as a parameter and outputs the string's characters except for whitespace
