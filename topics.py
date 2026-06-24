#LIST COMPREHENSIONS
#FOR SQUARE OF NUMBERS 0 TO 9

squares=[]
for x in range(10):
    squares.append(x*x)

print(squares)      #traditional way


squares =[x*x for x in range(10)]
print(squares)     #list comprehensions

#simple examples
#cubes
cubes = [x**3 for x in range(1,6)]
print(cubes)

#multiply by 10

numbers=[1,2,3,4]

result=[x*10 for x in numbers]
print(result)

#using strings
name="krishna"
letters = [ch for ch in name]
print(letters)

def letters(name):
    characters=[ch for ch in name]
    return characters

print(letters("krishna"))

#CONDITIONAL LIST COMPREHENSIONS
#for even numbers

evens =[x for x in range(10) if x%2==0]
print(evens)

#strings with length >4

names=["Ram","krishna","aditya","shivam"]
result =[name for name in names if len(name)>4]
print(result)
     
#DICTIONARY COMPREHENSIONS
#SYNATX = {Key:value for item in iterable}

# for squares dicationary

squares={x:x*x for x in range(7)}
print(squares)

#Length of word

words = ["apple","banana","grapes","watermelon"]
result={word:len(words) for word in words}
print(result)

#SET COMPREHENSION

numbers=[1,2,3,4,5,4,4,6,5]
unique={x for x in numbers}
print(unique)

#ADVANCED EXAMPLES

#reverse words

words=["apple","banana","grapes"]
result=[word[::-1] for word in words]
print(result)

#convert strings to integer

numbers=["10","20","30","40"]
result=[int(x) for x in numbers]
print(result)

#remove spaces

sentence="I love you"
result=[char for char in sentence if char!=" "]
print(result)