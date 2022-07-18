#!/usr/bin/python3
def fizzbuzz():
    while i <= 100:
        if (i % 5 == 0) and (i % 3 == 0):
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
