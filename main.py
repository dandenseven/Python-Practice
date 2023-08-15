from enum import Enum
from dog import bark
import sys
from functools import reduce


def is_adult(age):
    if age > 18:
        return True
    else:
        return False
    
# example 2
def is_adult2(age):
    return True if age > 18 else False

# enums
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

# print(State['ACTIVATE'].value)


# age = input("What is your age? ")
# print("Your age is?")

#dictionaries

dog = {"name": "Roger", "age": 8, "color": "green"}

#changing value

dog["name"] = "Syd"

print(dog)
print(dog.get("color", "brown"))

print(dog.pop("name"))
# print(dog.popitem())
print("color" in dog)
print(dog.keys())
print(dog.items())
print(dog.values())
print(list(dog.keys()))

dog["favorite food"] = "Meat"
# delete
del dog['color']

#copy a dictionary
dogCopy = dog.copy()

print(dog)
print(dogCopy)

#Sets
set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2
print(intersect)

set1 = {"Roger", "Syd"}
set2 = {"Luna"}

mod = set1 | set2
print(mod)

#creating a list from set

print(list(set1))

#Functions

def hello(name):
    print('Hello! ' + name)

hello("Beau")

def hello(name = "my friend"):
    print('Hello! ' + name)


hello("Beau")

def hello(name, age):
    print('Hello! ' + name + " my age is " + str(age))


hello("Beau", 14)

#Nested Functions
def talk(phrase):
    def say(word):
        print(word)
    
    words = phrase.split(' ')
    for word in words:
        say(word)

talk("I am going to buy the milk")

def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()

#objets

age = 8

print(age.real)
print(age.imag)
print(age.bit_length())

items = [1,2]
items.append(3)
items.pop()
print(id(items))

#Loops
#This is a while loop
condition = True
while condition == True:
    print("The condition is True")
#keeps running because condition is true/ false stops the while loop from running
    condition = False

count = 0
while count < 10:
    print("The condition is True")
    count = count + 1

print("After the loop")

#this is a foor loop

items = [1, 2, 3, 4]
for item in items:
    print(item)

for item in range(15):
    print(item)


items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)



items = [1, 2, 3, 4]
for item in items:
    if items == 2:
        continue
    print(item)


items = [1, 2, 3, 4]
for item in items:
    if items == 2:
        break
    print(item)

#classes
class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)

print(roger.name)
print(roger.age)

roger.bark()
roger.walk()

#Modules

bark()

#Accepting Arguments

print("hello")

# name = sys.argv[1]

# print("Hello " + name)

# Lambda Functions

lambda num : num * 2

multipy = lambda a, b : a * b

print(multipy(2, 4))

#map

numbers = [1,2,3]
def double(a):
    return a * 2

result = map(double, numbers)

print(list(result))

# usng map as a lambda function

numbers = [1,2,3]

double = lambda a : a * 2

result = map(double, numbers)

print(list(result))

# simplified map lambda function

numbers = [1,2,3]

result = map(lambda a : a * 2, numbers)

print(list(result))

#Filter

numbers = [1,2,3,4,5,6]

def isEven(n):
    return n % 2 == 0

result = filter(isEven, numbers)

print(list(result))

#Filter lambda function

numbers = [1,2,3,4,5,6]

result = filter(lambda n : n % 2 ==0, numbers)

print(list(result))

# Reduce - to use reduce you to import functools

expenses = [
    ("Dinner", 80),
    ("Car repair", 120)
]

sum = 0
for expense in expenses:
    sum += expense[1]

print(sum)


# Using reduce with lambda 

expenses = [
    ("Dinner", 80),
    ("Car repair", 120)
]

sum = reduce(lambda a,b,: a[1] + b[1], expenses)

print(sum)

#Recursion

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

# Decorators 

def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("hello")

hello() 

#Exceptions

#List Compressions

numbers = [1, 2, 3, 4, 5,]
#simpler to use list compression vs loop
numbers_power_2 = [n ** 2 for n in numbers]

print(numbers_power_2)

#loop
numbers_power_2 = []
for n in numbers_power_2:
    numbers_power_2.append(n**2)
# same otcome but more complex using map
numbers_power_2 = list(map(lambda n : n**2, numbers))


#Polymorphism

class Dog:
    def eat(self):
        print("Eating dog food")

class Cat:
    def eat(self):
        print('Eating cat food')

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

#Operator Overloading

class Dog:

    def __init__(self, name, age) :
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
    
roger = Dog("Rpger", 8)
syd = Dog("Syd", 9)

print(roger > syd)

