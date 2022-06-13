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
text = str(input("Enter a sentence or phrase: "))

print("You entered:", text)

def output_without_whitespace(text):
    return "".join(text.split())

print("String with no whitespace:", output_without_whitespace(text))

# This code turns user inputted string into an acronym
phrase = str(input("Enter a phrase to generate an acronym: "))

def acronym(words):
    return "".join(word[0] for word in words).upper()

def main():
    words = phrase.split()
    print("The acronym is:", acronym(words))

if __name__ == "__main__":
    main()

'''
Output:
Enter a sentence or phrase: The only thing we have to fear is fear itself.
You entered: The only thing we have to fear is fear itself.
String with no whitespace: Theonlythingwehavetofearisfearitself.
Enter a phrase to generate an acronym: random access memory
The acronym is: RAM
'''

# Name: Gabriel Policarpio
# Lab 3 - Task 3
# This program takes a user inputted zip code and turns it into a bar code
zip = int(input("Enter a zip code (in ZIP+4 format): "))

import turtle

t = turtle
t.pensize(2)
t.hideturtle()
t.left(90)
t.speed('fastest')

def print_zero():
    long()
    long()
    short()
    short()
    short()
    return

def print_one():
     short()
     short()
     short()
     long()
     long()

def print_two() :
    short()
    short()
    long()
    short()
    long()

def print_three() :
    short()
    short()
    long()
    long()
    short()

def print_four() :
    short()
    long()
    short()
    short()
    long()

def print_five() :
    short()
    long()
    short()
    long()
    short()

def print_six() :
    short()
    long()
    long()
    short()
    short()

def print_seven() :
    long()
    short()
    short()
    short()
    long()

def print_eight() :
    long()
    short()
    short()
    long()
    short()

def print_nine() :
    long()
    short()
    long()
    short()
    short()

def long():
    t.fd(14)
    t.up()
    t.bk(14)
    t.right(90)
    t.fd(6)
    t.down()

def short():
    t.fd(6)
    t.up()
    t.bk(6)
    t.right(90)
    t.fd(6)
    t.left(90)
    t.down()

t.up()
t.goto(0, -50)
t.down()

if digit == '0':
    print(print_zero)

elif digit == '1':
    print(print_one)

elif digit == '2':
    print(print_two)

elif digit == '3':
    print(print_three)

elif digit == '4':
    print(print_four)

elif digit == '5':
    print(print_five)

elif digit == '6':
    print(print_six)

elif digit == '7':
    print(print_seven)

elif digit == '8':
    print(print_eight)

elif digit == '9':
    print(print_nine)

else:
    print('Please print a valid zipcode.')
