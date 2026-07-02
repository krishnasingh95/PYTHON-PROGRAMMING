#------------------EXCEPTION HANDLING-------------------
#try:
    # risky code
#except:
    # Executes only if an error occurs
#else:
    # executes only if there is no exception
#finally:
     # always executes whether an error happens or not

#EXample 1: without exception handling

num = int(input("Enter number : "))
print(num)     # when input is abc, program crashes

#with exception handling

try:
    num= int(input("Enter number : "))
    print(num)          
                                    #if input is abc, try gets skipped and python jumps onto the except block and except block gets executed
except:
    print("Invalid Input")

#example 2:
try:
    print(100/20)

except:
    print("error")     # here there is no error so, try block gets executed and except block gets skippped
 
#catching specific exceptions:

try:
    print(10/0)

except ZeroDivisionError:
    print("Canot divided by zero")

# multiple exceptions

try:
    num= int(input())
    print(10/num)

except ValueError:
    print("please enter a number")
except ZeroDivisionError:
    print("Cannot be divided by zero")

#else block

#else block runs only if there is no exception

try:
    print(10/2)

except ZeroDivisionError:
    print("cannot divided by zero")

else:
    print("Division Successful")


#finally block  # executes always whether an error happens or not

try:
    print(10/0)

except ZeroDivisionError:
    print("Cannot divided by zero")

finally:
    print("Program Finished")


# example:

try:
    print(10/2)

except ZeroDivisionError:
    print("Cannot divided by zero")

finally:
    print("Program Finished")


#practice question 1:

try:
    num1= int(input("enter first number : "))
    num2= int(input("enter second number : "))
    print(num1/num2)

except ValueError:
    print("please enteer a number")

except ZeroDivisionError:
    print("Cannot be divided by zero")

else:
    print("division successful")

finally:
    print("Thank you for using calculator")

# practice question 2:

numbers= [10,20,30]
try:
    index = int(input("enter the index: "))
    print("Element : ",numbers[index] )

except ValueError:
    print("please select the valid value of index")


except IndexError:
    print("you have selected  the wrong index")

else:
    print("Program successfull")

# practice question 3

student= {"name" : "krishna"}
try:
    key= str(input("enter the key : "))
    print(student[key])

except KeyError:
    print("Please select the valid key")

else:
    print("Program successfull")

#ADVANCED EXCEPTION HANDLING

#The raise keyword

age = int(input("enter your age : "))
if age< 18:
    raise ValueError("Age must be above 18 years")
print("Registration successfull")

#using raise with try-except

try:
    age= int(input("Enter your age : "))

    if age < 18:
        raise ValueError("Age must be 18 or above")
    
    print("Eligible")

except ValueError as e:
    print(e)

#creating a custom exception

class InsufficientBalanceError(Exception):
    pass

try:
    balance= 500
    amount= int(input("Enter the amount : "))

    if amount> balance:
        raise InsufficientBalanceError("Insufficient Balance")
    
    print("Insufficient balance")

except InsufficientBalanceError as e:
    print(e)


# real ATM example

class InsufficientBalanceError(Exception):
    pass

class ATM:
    def __init__(self,balance):
        self.balance= balance

    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        
        self.balance -= amount
        
        print("Withdrawl successful")

atm = ATM(50000)

try:
    atm.withdraw(70000)

except InsufficientBalanceError as e:
    print(e)


# # practicce question 1:

try:
    password= input("Enter password : ")

    if len(password)<8:
        raise ValueError("Password must be of at least 8 charaters")
    
    print("password accepted")
    
except ValueError as e:
    print(e)


# # practice question 2:

class NegativeNumberError(Exception):
    pass

try:
    number= int(input("Enter the number : "))

    if number<0:
        raise NegativeNumberError("Negative numbers are not allowed")
    
except NegativeNumberError as e:
    print(e)

else:
    print("valid number")


# practice question 3:

class AgeTooSmallError(Exception):
    pass

class AGE:

    def __init__(self,age):
        self.age=age

    def eligible(self):
        if self.age <18:
            raise AgeTooSmallError ("Age is too small for vote")
        
        print("Eligible to vote")


agee= AGE(18)

try:
    agee.eligible()

except AgeTooSmallError as e:
    print(e)








