#FUNCTIONS IN PYTHON
def greet():
    print("Hello krishna")
greet()

def welcome():
    print("welcome to Python Programming krishna")
    print("Now we are learning functions")

welcome()

def greet(name):
    print(f"Hello {name}")
    print("Hello",name)

greet("krishna")

def square(number):
    print(number*number)

square(5)
square(10)


def add(a,b):
    print(a+b)

add(10,20)

def student(name,age):
    print("Name:" , name)
    print("Age" , age)

student("krishna:",20)


#Dfference between print() and return()
#using print()

def add(a,b):
    print(a+b)

result = add(23,46)
print(result)      # line 65, 66 and 68 are same there has been just the different ways to print statements.can also applied on return() 

print(add(23,46))

# using return()

def add(a,b):
    return a+b    

print(add(23,47))  


def multiply(a,b):
    return a*b

result = multiply(4,6)
print(result)

#Returning multiple values

def calculate(a,b):
    return a*b, a+b , a-b

result = calculate(90,56)
print(result)


#Default parameters

def greet(name="Guest"):
    print("hello",name)

greet()
greet("krishna")

def power(base=3,exponent=3):
    return base**exponent

print(power())

def power(base,exponent=3):
    return base**exponent

print(power(4))
print(power(3,4))
    

#Keyword Arguments

def student(name,age):
    print(name)
    print(age)
                                    #here order doesn't matter at all
student(age=21,name="krishna")

#Positional arguments

def subtract(a,b):
    print(a-b)
                   #Here order matters
subtract(20,5)       
subtract(b=5,a=20)

#Arbitrary arguments(*args)

def add(*args):
    print(args)

add(2,3,4,5)

def total(*numbers):
    print(sum(numbers))

total(3,56,89,45)

def largest(*numbers):
    print(max(numbers))

largest(34,67,23,98)

#Arbitrary keyword arguments (**kwargs)

def person(**kwargs):
    print(kwargs)

person(name = "krishna",age=21)


def details(**data):
    for key,value in data.items():
        print(key,value)

details(name = "krishna" , age=20, city = "azamgarh")

#  Global and Local variables

def test():
    x=100
    print(x)

test()  # 100

x = 50
def test():
    print(x)

test()

count = 0
def increase():
    global count
    count +=8

increase()
print(count)

#Nested Function

def outer():
    print("outer")

    def inner():
        print("inner")

    inner()

outer()

#Rescuesive function
 
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(6))

#FIBONACCI

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(7))

#lambda Function

def square(x):
    return x*x
                   #normal function
print(square(4))

square = lambda x:x*x
                     #labda function
print(square(4))


multiply = lambda a,b:a*b

print(multiply(3,4))

#map()             #map() applies a function to every element of an iterable(list,tuple) and returns a map object
  
#synatax :  map(function,iterable)

#example 1: squaring numbers

numbers = [1,2,3,4]

result=[]

for num in numbers:
    result.append(num**2)

print(result)     # without map() 


numbers = [1,2,3,4]

def square(x):
    return x**2

result= map(square,numbers)
print(list(result))     # with map()

numbers =[1,2,3,4]

square = list(map(lambda x:x**2,numbers))
print(square)           # with lambda()

#example 2 : convert strings to uppercase

names = ["krishna","aditya","prasoon"]

result = list(map(str.upper,names))

print(result)

# example 3 :convert string numbers into integers

numbers =["10","20","30"]

result = list(map(int,numbers))
print(result)

#example 4: adding two list

a = [1,2,3]
b = [5,6,7]

result= list(map(lambda x,y:x+y,a,b))
print(result)

#filter()       selects elements based on a condition
#syntax :  filter(function,iterable)

#example 1: even numbers
numbers =[1,2,3,4,5,6]
evens=[]

for num in numbers:
    if num%2==0:
        evens.append(num)

print(evens)   #without filter

numbers=[1,2,3,4,5,6,7,8]

def even(x):
    return x % 2==0

result =filter(even,numbers)   #using filter()

numbers=[1,2,3,4,5,6,7,8]

result = list(filter(lambda x:x%2==0,numbers))
print(result)   #using lambda

# example 2: filter strings

names =["krishna","","aditya"]
result = list(filter(bool,names))
print(result)

#combining map() and filter()
#example 1: suppose we want to select even numbers and square them

numbers=[1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x:x % 2==0,numbers))
squares = list(map(lambda x : x**2,evens))
print(list(squares))

#example 2 

ages=[24,36,12,3,8,45,23,21]

adults=list(filter(lambda x:x>=18,ages))
print(adults)

labels = list(map(lambda age:f"age: {age}",adults))
print(labels)

#PRACTICE OF FUNCTIONS IN  PYTHON

#maximum of three numbees

def maximum(a,b,c):
    return max(a,b,c)
print(maximum(10,45,56))


#check whether a number is prime 

def is_prime(n):
    if n< 2:
        return False
    for i in range(2,n):
        if n % i==0:
            return False
    return True
    

        
print(is_prime(6))

#find factorial
def factorial(n):
    if n<=1:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))

# Reverse a string

def reverse_string(s):
    return s[::-1]

print(reverse_string("krishna"))

#count a vowel

def count_vowels(s):
    count = 0

    for char in s.lower():
        if char in "aeiou":
            count += 1

    return count

print(count_vowels("Educationalist"))

#average of a list

def average(lst):
    return sum(lst)/len(lst)

numbers = [10,20,30,40]
print(average(numbers))

# remove duplicates from list

def remove_duplicates(lst):
    return list(set(lst))

numbers = [1,2,3,4,4,5,5,6,6,8,8,9]
print(remove_duplicates(numbers))

# calculate simple interest

def simple_interest(principal,rate,time):
    return(principal*rate*time)/100
print(simple_interest(10000,6,4))

#check palindrome

def palindrome(s):
    return s==s[::-1]

print(palindrome("madam"))
print(palindrome("python"))
print(palindrome("mam"))
    


