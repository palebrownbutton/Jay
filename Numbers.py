import random
import math

def get_random(num1, num2):
    print("Here is a random number between", num1, "and", str(num2) + ":", random.randint(num1, num2))

def multiply(num1, num2):
    print(num1, "times", num2, "is", num1 * num2)

def divide(num1, num2):
    print(num1, "divided by", num2, "is", num1 / num2)

def add(num1, num2):
    print(num1, "plus", num2, "is", num1 + num2)

def subtract(num1, num2):
    print(num1, "minus", num2, "is", num1 - num2)

def power(num1, num2):
    print(num1, "to the power of", num2, "is", num1 ** num2)

def square_root(num):
    print("The square root of", num, "is", round(math.sqrt(num), 2))

def factorial(num):
    print("The factorial of", num, "is", math.factorial(num))