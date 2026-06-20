# #This is the basics of python programming language
name = "krishna"
print(name)
age = 25
print(age)
print(name,age)
#Taking input from user
name = input("enter you name: ")
age = input("enter your age: ")
print(name,age)
# #data types in python
name = "krishna"
print(type(name))
print(isinstance(name,str))
print(isinstance(name,int))
age = 25
print(type(age))
print(isinstance(age,int))
print(isinstance(age,str))
#type casting in python
age = 25
print(type(age))
age = str(age)
print(type(age))
#operators in python
#arithmetic operators
a = 10
b = 5
print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division
print(a % b) #modulus
print(a ** b) #exponentiation
print(a // b) #floor division
age = 8
age +=3 # age = age + 3
print(age)
age -=3 # age = age - 3
print(age)
#comparison operators
a = 10
b = 5
print(a > b) #greater than
print(a < b) #less than
print(a == b) #equal to
print(a != b) #not equal to
print(a >= b) #greater than or equal to
print(a <= b) #less than or equal to
#ternary operator
age =19
def check_age(age):
    return "you are an adult" if age >= 18 else "you are a minor"
print(check_age(age))
#logical operators
a = 10
b = 5
print(a > 5 and b < 10) #and operator
print(a > 5 or b < 10) #or operator
print(not(a > 5)) #not operator
#more examples of logical operators
age = 25
gender = "male"
print(age >= 18 and gender == "male") #and operator
print(age >= 18 or gender == "female") #or operator
print(not(age >= 18)) #not operator

#membership operators
name = "krishna"
print("k" in name) #in operator
print("z" in name) #in operator
print("a" not in name) #not in operator
print("s" not in name) #not in operator
 
#more examples of membership operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) #in operator
print("grape" in fruits) #in operator
print("banana" not in fruits) #not in operator

#identity operators
a = 10
b = 10
print(a is b) #is operator
print(a is not b) #is not operator
#more examples of identity operators
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y) #is operator
print(x is not y) #is not operator
#string
"krishna"
"singh"
name = "krishna"
print(name  + "is my name")
print("krishna" + "is my name")
name = "krishna"
name += "is my name"
print(name)
#string formatting
name = "krishna"
age = 25
print("my name is {} and my age is {}".format(name,age))
print(f"my name is {name} and my age is {age}") #f-string
#string methods
name = "krishna"
print(name.upper()) #upper() method
print(name.lower()) #lower() method
print(name.capitalize()) #capitalize() method
print(name.title()) #title() method
print(name.strip()) #strip() method
print(name.replace("k","s")) #replace() method
print(name.split("i")) #split() method
print(name.find("s")) #find() method
#string characters and escape sequences
print("krishna\nsingh") #new line
print("krishna\tsingh") #tab
print("krishna\'s name") #single quote
print("krishna\"s name") #double quote
print("krishna\\singh") #backslash
#string indexing and slicing
name = "krishna"
print(name[0]) #indexing
print(name[1]) #indexing
print(name[-1]) #indexing
print(name[0:3]) #slicing
print(name[3:]) #slicing
print(name[:3]) #slicing
print(name[::2]) #slicing
print(name[::-1]) #slicing
print(name[1:5:2]) #slicing
print(name[5:1:-1]) #slicing
print(name[1:5:-1]) #slicing
print(name[5:1:1]) #slicing
#number data types
num1 = 10
num2 = 3.14
num3 = 2 + 3j
print(type(num1)) #int
print(type(num2)) #float
print(type(num3)) #complex
num1 = 2+4j
num2 = complex(2,3)
print(num1.real) #real part
print(num1.imag) #imaginary part
#built-in functions for numbers
num1 = -10
num2 = 3.14
print(abs(num1)) #absolute value
print(abs(num2)) #absolute value
print(pow(num1,2)) #power
print(pow(num2,2)) #power
print(round(num2)) #round
print(round(num2,1)) #round to 1 decimal place
print(round(num2,2)) #round to 2 decimal places
print(round(num2,3)) #round to 3 decimal places
#enum
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
print(Color.RED) #Color.RED
print(Color.RED.name) #RED
print(Color.RED.value) #1
print(Color.GREEN) #Color.GREEN
print(Color(2))  #Color.GREEN
#user input
name = input("Enter your name: ")
print("Hello, " + name)
#control flow statements
# if statement
age = 18
if age >= 18:
    print("You are an adult")
    print("You can vote")
print("This is always executed")
#more examples of if statement
age = 17
if age >= 18:
    print("You are an adult")
    print("You can vote")

#if-else statement
age = 17
if age >= 18:
    print("You are an adult")
    print("You can vote")
else:
    print("You are a minor")
    print("You cannot vote")
#more examples of if-else statement for an employee
salary = 50000
if salary >= 50000:
    print("You are eligible for a bonus")
else:
    print("You are not eligible for a bonus")

#for even more examples of if-else statement for a student
marks = 75
if marks >= 90:
    print("You got an A grade")
elif marks >= 80:
    print("You got a B grade")
else:
    print("You got a C grade")

#even odd number check using if-else statement
num = 10
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#common example for if else and elif statement
condition = True
name = "krishna"

if condition==True:
    print("The condition " + "is true")
elif name == "krishna":
    print("The name is krishna")
elif name =="Aditya":
    print("The name is Aditya")
else:
    print("The condition is false and the name is not krishna or Aditya")


#Lists in python
fruits = ["apple", "banana", "cherry"]
print(fruits[0]) #accessing elements
print(fruits[1]) #accessing elements
print(fruits[2]) #accessing elements
print(fruits[-1]) #accessing elements from the end
# List slicing
print(fruits[0:2]) #slicing
print(fruits[1:3]) #slicing
print(fruits[::2]) #slicing
# List methods
fruits.append("orange") #adding an element
print(fruits)
fruits.insert(1,"grape") #inserting an element
print(fruits)
fruits.remove("banana") #removing an element
print(fruits)
fruits.append("Litchi") #adding an element
print(fruits)
fruits.pop() #removing the last element
print(fruits)
fruits.pop(1) #removing an element at a specific index
print(fruits)
fruits.sort() #sorting the list
print(fruits)
fruits.reverse() #reversing the list
print(fruits)
print(len(fruits)) #length of the list
print(fruits.count("apple")) #counting the occurrences of an element
print(fruits.index("cherry")) #finding the index of an element
print(fruits.copy()) #copying the list
print(fruits)

dogs = ["krishna" ,2 , "aditya" , True , 3.14]
dogs[2] = "singh" #modifying an element
print(dogs)

#tuples in python
colors = ("red", "green", "blue")
print(colors[0]) #accessing elements
print(colors[1]) #accessing elements
print(colors[2]) #accessing elements
print(colors[-1]) #accessing elements from the end
#methods of tuples
print(len(colors)) #length of the tuple
print(colors.count("red")) #counting the occurrences of an element
print(colors.index("green")) #finding the index of an element
print(colors) #printing the tuple

#dictionaries in python
student = {"name": "krishna", "age": 20, "grade": "A"}
print(student["name"]) #accessing elements
print(student["age"]) #accessing elements
print(student["grade"]) #accessing elements
#methods of dictionaries
print(len(student)) #length of the dictionary
print(student.keys()) #getting the keys
print(student.values()) #getting the values
print(student.items()) #getting the items
print(student.get("name"))#getting the value of a key
print(student.get("address","Not Found")) #getting the value of a key with default value
student["address"] = "India" #adding a new key-value pair
print(student) #printing the dictionary

#sets in python
fruits = {"apple", "banana", "cherry"}
print(fruits) #printing the set
print(len(fruits)) #length of the set
fruits.add("orange") #adding an element
print(fruits) #printing the set
fruits.remove("banana") #removing an element
print(fruits) #printing the set
print("banana" in fruits) #checking if an element is in the set
print("grape" in fruits) #checking if an element is in the set
print(fruits.union({"grape", "kiwi"})) #union of two sets
print(fruits.intersection({"grape", "kiwi"})) #intersection of two sets
print(fruits.difference({"grape", "kiwi"})) #difference of two sets

#functions in python

def hello(name = "MY FRIEND"): #function definition
    print("Hello" + name)

hello("krishna") #calling the function
hello("aditya") #calling the function
hello() #calling the function with default argument

def hello(name,age):
    print("Hello" + name + "You are" + age + "years old")
hello("krishna","25") #calling the function

def change(value):
    value = 10
    

value = 5
print("Before function call:", value)
value = change(value)
print("After function call:", value)

#more examples of functions

def add(a,b):
    a =10
    b =20
    return a+b

def change():
    a =60
    b =40
    return a,b

def add(a,b):
    return a+b

a,b = change()
value= add(a,b)
print(value)

#more examples of functions
a = 10
b = 20
def add(a,b):
    return a+b
print(add(a,b))

#nested functions
def talk(phrase):
    def say(word):
        print(word)

        
    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to the school')

#objects

age = 20
print(age.real)
print(age.imag)
print(age.bit_length())

#loops in python
#while loop
condition = True
while condition != True:
    print("The condition is True")

count = 0
while count<10:
    print("our condition is true")
    count = count + 1
print("after the loop")

#more examples of while loop
employee = ["krishna","aditya","singh"]
while employee:
    print(employee.pop())
    print(employee)

#for loop
items = [1,2,3,4]
for item in items:
    print(item)

for item in range(15):
    print(item)

#more examples of for loop
items = [1,2,3,4,5]
for index,item in enumerate(items):
    print(index,item)

#break and continue statements
items=[1,2,3,4,5]
for item in items:
    if item == 2:
        continue
    print(item)

items = [1,2,3,4,5]
for item in items:
    if item == 2:
        break
    print(item)

#classes

class Animal:
    def walk(self):
        print("walking...")
class dog(Animal):
    def __init__(self,name,age):
        self.name = "krishna"
        self.age = 21
    def bark(self):
        print("woof!")

krishna = dog("krishna",21)

print(krishna.name)
print(krishna.age)
krishna.bark()
krishna.walk()

#modules
import math

print(math.sqrt(4))

# it can also be wriiten as

from math import sqrt
print(sqrt(4))

#RECURSION

def factorial(n):
    if n ==1:
        return 1
    else:
        return n *factorial(n-1)

result = factorial(5)
print(result)


















