# Ma'am I tried to do the homework task but I couldn't figure out how to make it work,sorry.

import dropbox
import time
import random

def multiplication():
    # Automation of the looping of multiples from 1 to 10
    number = int(input("Enter a number from 1-10 to get 10 multiples of it: "))

    if (number == 2):
        print(2)
        while number<=19:
            number = number + 2
            print(number)

    if (number == 3):
        print(3)
        while number<=29:
            number = number + 3
            print(number)

    if (number == 4):
        print(4)
        while number<=39:
            number = number + 4
            print(number)

    if (number == 5):
        print(5)
        while number<=49:
            number = number + 5
            print(number)

    if (number == 6):
        print(6)
        while number<=59:
            number = number + 6
            print(number)

    if (number == 7):
        print(7)
        while number<=69:
            number = number + 7
            print(number)

    if (number == 8):
        print(8)
        while number<=79:
            number = number + 8
            print(number)

    if (number == 9):
        print(9)
        while number<=89:
            number = number + 9
            print(number)

    if (number == 10):
        print(10)
        while number<=99:
            number = number + 10
            print(number)

    if (number == 1):
        print(1)
        while number<=9:
            number = number + 1
            print(number)

    if(number > 10):
        print("Invalid number")

multiplication()