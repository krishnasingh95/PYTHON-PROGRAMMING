#Python object-oriented programming

#example 1:
class Student:             #creating class
    name="krishna"

s1=Student()              #creating object(instance)
print(s1.name)


class Car:
    color="blue"
    brand="Mercedes"

car1=Car()
print(car1.color)
print(car1.brand)


#example   #giving attributes

class Student:
    pass

student1= Student()
student1.name = "krishna"
student1.age = 21

print(student1.name)
print(student1.age)

# example   #assignment question

class Laptop:
    pass

laptop1 = Laptop()
laptop2 = Laptop()

laptop1.Brand = "DELL"
laptop1.RAM = "16GB"
laptop2.Brand = "HP"
laptop2.RAM = "8GB"

print(laptop1.Brand)
print(laptop1.RAM)
print(laptop2.Brand)
print(laptop2.RAM)

#constructor   __init__ Function
class Student:
    def __init__(self,name,age,branch):
        self.name= name
        self.age= age
        self.branch = branch

s1= Student("krishna ",21,"AIML")
print(s1.name , s1.age, s1.branch)

# example
class Car:
    def __init__(self,Brand,Model,Price):
        self.Brand=Brand
        self.Model=Model
        self.Price=Price

car1 = Car("Toyota","Land cruiser",4500000)
car2 = Car("Honda","city",1200000)
print("Brand:",car1.Brand , "Model:" , car1.Model , "Price:" , car1.Price)
print("Brand:",car2.Brand , "Model:" , car2.Model , "Price:" , car2.Price)

# example

class Book:
    def __init__(self,title,author,price):
        self.title= title
        self.author= author
        self.price = price

book= Book("Life Thoughts","RUSKIN BOND",420)
print("Title: " ,book.title, "AUthor: ",book.author ,"Price: " ,book.price)


class Student:
    #default constructors
    def __init__(self):
         pass

    #parameterized constructors
    def __init__(self,name,marks):
        self.name= name
        self.marks= marks
        

s1= Student("krishna",90)
print(s1.name,s1.marks)

s2= Student("karan",98)
print(s2.name,s2.marks)

# Instance Methods    are the function that belongs to objects
# Accessing attributes insides methods

class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks= marks

    def welcome(self):
        print("welcome to the world of python students",self.name)

    def get_marks(self):
        return self.marks


s1= Student("krishna",90)
s1.welcome()
print(s1.get_marks())



#Methods can accept parameters

class calculator:
    def add(self,a,b):
        return a+b
calc = calculator()
print(calc.add(10,29))
        
# example: Rectangle

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
    
r= Rectangle(10,20)
print(r.area())

# example: Bank account

class Bankaccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance -=amount

        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:" , self.balance)

account=Bankaccount("Krishna Singh",45000)
account.check_balance()
account.deposit(5000)
account.check_balance()
account.withdraw(12000)
account.check_balance()

# practice question 1

class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)

    def start(self):
        print(f"{self.brand},{self.model} has started")
    def stop(self):
        print(f"{self.brand},{self.model} has stopped")

car= Car("Maruti Suzuki","Ciaz", 1800000)
car.display()
car.start()
car.stop()

# practice question 2

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def increase_salary(self,amount):
        self.salary +=amount
        
    def display(self):
        print("name: ",self.name)
        print("Salary: ",self.salary)

employee= Employee("krishna singh",42000)
employee.display()
employee.increase_salary(10000)
employee.display()


# practice question 3
#Here we use the concept of transfer() , it is a very important concept.
class BankAccount:
    def __init__(self,account_holder,account_number,balance,pin):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
        self.pin=pin
        self.transaction_history=[]
    #deposit money
    def deposit(self,amount):
        if amount >0:
            self.balance +=amount
            print(f"RS.{amount} deposited succesfully")

        else:
            print("invalid amount")

    #withdrawn money
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"withdrawn Rs. {amount}")
            self.transaction_history.append(f"Deposited Rs. {amount}")
            print(f"Rs.{amount} debited sucessfully")

        else:
            print("Insufficient balance")

    #transfer money
    def transfer_money(self,other_account,amount):
        if amount <= self.balance:
            other_account.balance += amount
            self.transaction_history.append(f"Transfeered Rs. {amount} to the {other_account.account_holder} Rs. {amount}")
            other_account.transaction_history.append(f"Recieved  Rs. {amount} from the {self.account_holder} Rs. {amount}")
            print(f"Rs.{amount} has been succsfully transferred from {self.account_holder} to {other_account.account_holder}")
        else:
            print("Insufficient balance")

    #check balance
    def check_balance(self):
        print(f"{self.account_holder}'s balance : Rs {self.balance}")


    #change PIN

    def change_pin(self,old_pin,new_pin):
        if old_pin == self.pin:
            self.pin= new_pin
            print("PIN chnaged succesfully")

        else:
            print("Incorrect old PIN")

    # Apply interset
    def apply_interest(self,rate):
        interest=self.balance*rate/100
        self.balance += interest

        self.transaction_history.append(f"Interest added Rs.{interest:.2f}")
        print(f"Interest of Rs.{interest:.2f} added")


    # check minimum balance

    def check_minimum_balance(self):
        if self.balance>=1000:
            print("minimum balance maintained")

        else:
            print("warning! balance below 1000")

    #display account details

    def display(self):
        print("---------------Account details----------")
        print(f"Account Holder : {self.account_holder}")
        print(f"Account number: {self.account_number}")
        print(f" Account Balance : {self.balance}")
        print("-------------------------------------------------")
     

    #show transaction history

    def show_history(self):
        print("\n Transaction history")
        
        if len(self.transaction_history) ==0:
            print("No transaction done till now")

        else:
            for transaction in self.transaction_history:
                print(transaction)

acc1= BankAccount("Krishna singh",240567890,450000,2459)
acc2= BankAccount("Aditya Singh",24625867890,550000,3589)

acc1.display()
acc2.display()

acc1.deposit(21000)
acc1.withdraw(12000)

acc1.transfer_money(acc2,3000)

acc1.check_balance()
acc2.check_balance()

acc1.change_pin(2459,9090)
acc2.change_pin(3589,0000)

acc1.apply_interest(7)
acc2.apply_interest(9)

acc1.check_minimum_balance()
acc2.check_minimum_balance()

acc1.show_history()
acc2.show_history()


#Counting objects

class Student:

    count = 0

    def __init__(self,name):
        self.name=name
        Student.count +=1

s1= Student("krishna")
s1= Student("Aditya")
s1= Student("Pooja")

print(Student.count)

#INSTANCE CLASS AND CLASS VARIABLES

class University:

    #class variables
    university_name="BIET"
    city="LUCKNOW"
    total_students=0

    def __init__(self,student_name,branch,semester):
        
        #instance variables
        self.student=student_name
        self.branch= branch
        self.sem= semester

        University.total_students +=1
    
    #displaying the student details
    def display_student(self):
        print(f"Student's name is {self.student}")
        print(f"Student's branch is {self.branch}")
        print(f"Student's current semester is {self.sem}")


    #displaying the university details
    def display_university(self):
        print(f"The University name is {University.university_name}")
        print(f"The University is in  {University.city}")
        print(f"The Total students in the university is {University.total_students}")


student1=University("Krishna Singh","AIML","4th")
student2=University("Aditya Singh","AIML","5th")

student1.display_student()
student2.display_student()

student1.display_university()

#CLASS METHOD AND STATIC METHOD
# example 1:
class Student:
    university= "AKTU"
    
    @classmethod
    def display_university(cls):
        print(cls.university)

Student.display_university()

#example 2:
class Student:

    university = "Galgotias"

    @classmethod
    def change_university(cls, new_name):

        cls.university = new_name


print(Student.university)
Student.change_university("IIT DELHI")
print(Student.university)

# example 3: static methods

class Calculator:

    @staticmethod
    def add(a,b):
        return a+b
    
print(Calculator.add(10,30))

#example 4:
class Bank:

    @staticmethod

    def validate_ifsc(ifsc):

        return len(ifsc)==11
    
print(Bank.validate_ifsc("UNIB9807065"))

# # example 5: mixed example

class Student:

    university = "Galgotias"
    count = 0

    def __init__(self,name):
        self.name=name
        Student.count +=1

    def display(self):
        print(self.name)

    @classmethod

    def display_count(cls):
        print(cls.count)

    @classmethod
    def change_university(cls,new_name):
        cls.university=new_name

    @staticmethod
    def is_adult(age):
        return age>=18
    
s1=Student("krishna singh")
s1.display()

Student.display_count()
Student.change_university("AKTU")
print(Student.university)

print(Student.is_adult(20))
print(Student.is_adult(17))

# practice question 1:

class BankClass:
    #class variables
    bank_name="Union Bank of India"
    interest_rate= 7

    #instance variables
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance +=amount
        print(f"Rs.{amount} has been deposited succesfully")

    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance -=amount
            print(f"Rs.{amount} has been withdrawn from your account succesfully")

        else:
            print("insufficient balance")

    def display(self):
        print("-------------ACCOUNT DETAIL--------------")
        print(f"Account holder's name is {self.account_holder}")
        print(f"Account current balance is {self.balance}")
        print(f"This account is exists in {BankClass.bank_name}")
        print(f"Interest Rate : {BankClass.interest_rate}%")
        print("---------------------------------------")

    @classmethod
    def change_interest(cls,new_interest_rate):
        cls.interest_rate=new_interest_rate

    @staticmethod
    def validate_amount(amount):
        if amount >0:
            return True
        return False


bank1=BankClass("Krishna Singh",20000)
bank2=BankClass("Aditya Singh",30000)

bank1.deposit(20000)
bank2.deposit(50000)

bank1.withdraw(10000)
bank2.withdraw(10000)


BankClass.change_interest(8)
print(BankClass.interest_rate)

bank1.display()
bank2.display()

print(BankClass.validate_amount(20000))

# practice question 2
class Library:
    library_name="Krishna study Point"
    total_books=0
    

    def __init__(self,title,author,book_id):
        self.title=title
        self.author=author
        self.book_id= book_id
        self.is_issued=False

        Library.total_books +=1

    def issue_book(self):
        if self.is_issued==False:
            self.is_issued=True
            print(f"{self.title} issued succesfully")
            print(f"Issued : {self.is_issued}")

        else:
            print("Book  already issued")

    def return_book(self):
        if self.is_issued==True:
            self.is_issued=False
            print(f"{self.title} returned succesfully")
            print(f"Issued : {self.is_issued}")
        else:
            print("Book already returned")


    def display(self):
        print("--------------BOOK DETAILS-----------------")
        print(f"Library name : {Library.library_name}")
        print(f"Total books in the library is: {Library.total_books}")
        print(f"The title of the book is : {self.title}")
        print(f"The author of the book is: {self.author}")
        print(f"The ID of the book is : {self.book_id}")
        status="Issued" if self.is_issued else "Available"
        print(f"The status of book is : {status}")
        print("----------------------------------------------")

    @classmethod
    def change_library_name(cls,new_name):
        cls.library_name=new_name

    @classmethod
    def display_total_books(cls):
        print(cls.total_books)

    @staticmethod
    def is_valid_book_id(book_id):
        return len(book_id)==6 and book_id.isdigit()
    

book1= Library("Prem","Munshi Premchand","234566")
book2= Library("The last day","Anne Frank","234456")

book1.issue_book()
book2.issue_book()

book1.return_book()
book2.return_book()

book1.display()
book2.display()

Library.change_library_name("Aditya Study Point")
print(Library.library_name)
print("Library name changed")

Library.display_total_books()

print(Library.is_valid_book_id("234356"))
# example 5
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
     

    def average(self):
       sum=0
       for value in self.marks:
           sum += value
       print("hello" , self.name , "Your avg score is:" , sum/3)
    

s1=Student("krishna singh",[90,95,98])
s1.average()


#ENCAPSULATION (Bundling data and methods toeghter inside a class and controlling how the data is accessed or modified)
# Python gives three access level (public,protected,private)
# public members

class Student:
    def __init__(self):
        self.name="krishna"

s=Student()
print(s.name)
s.name="Aditya"
print(s.name)

#Protected members

class Bank:
    def __init__(self):
        self._balance=5000

bank=Bank()
print(bank._balance)

#private members:

class Bank:
    def __init__(self):
        self.__balance=5000

bank=Bank()
#print(bank.__balance)   # This gives attribute error
print(bank._Bank__balance)

#GETTERS AND SETTERS

class Bank:

    def __init__(self):
        self.__balance= 5000

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        if amount >= 0:
            self.__balance=amount

        else:
            print("Invalid Balance")

bank= Bank()
print(bank.get_balance())   #5000
bank.set_balance(8000)
print(bank.get_balance())   #8000
bank.set_balance(-500)   

# example:

class Student:

    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks

    def get_marks(self) :
        return self.__marks
    
    def set_marks(self,marks):
        if  0 <= marks <= 100:
            self.__marks=marks

        else:
            print("Invalid Marks")

s= Student("Krishna Singh",94)
print(s.get_marks())
s.set_marks(95)
print(s.get_marks())
s.set_marks(150)

# practice question 1:

class BankAccount:

    def __init__(self,balance,pin):
        self.__balance=balance
        self.__pin=pin

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid Amount")

    def withdraw(self,amount,pin):
        if pin !=self.__pin:
            print("Incorrect PIN")
            return
        if amount<=self.__balance:
            self.__balance -=amount
            print(f"Rs. {amount} withdrawn successfully")

        else:
            print("Insufficeint balance")

    def get_balance(self,pin):
        if pin ==self.__pin:
            return self.__balance
        
        print("Incorrect PIN")
    
    def change_pin(self,old_pin,new_pin):

        if old_pin==self.__pin:
            self.__pin = new_pin
            print("PIN changed successfully")

        else:
            print("Invalid PIN")

bank1= BankAccount(20000,4356)

bank1.deposit(3000)
print(bank1.get_balance(2345))

bank1.withdraw(9000,4356)
print(bank1.get_balance(2345))

bank1.change_pin(3456,8970)

# practice question 2:
class ATM:

    def __init__(self,balance,pin):
        self.__balance=balance
        self.__pin=pin

    def deposit(self,amount,pin):
        if pin==self.__pin:
            if amount>0:
                self.__balance +=amount
                print(f"Rs.{amount} deposited succesfully")

            else:
                print("Invalid Amount")

        else:
            print("Incorrect PIN")

    def withdrawl(self,pin,amount):
        if pin!= self.__pin:
            print("Incorrect PIN")
            return

        if amount<= self.__balance:
                self.__balance -= amount
                print(f"Rs.{amount} withdrawn succesfully")

        else:
            print("Insufficient Balance")

    def change_pin(self,old_pin,new_pin):
        
        if old_pin ==self.__pin:
            self.__pin=new_pin
            print("PIN changed successfully")
        else:
            print("Invalid PIN")

    
    def get_balance(self,pin):
        if pin== self.__pin:
            return self.__balance

        else:
            print("Incorrect PIN")
        
    def display(self,pin):
        if pin==self.__pin:
            print("-----------------------ATM DETAILS")
            print(f"The balance in the account is : {self.__balance}")
            print("-----------------------------------------------")
        else:
            print("Incorrect PIN")

bank = ATM(300000,3476)
bank.deposit(2345,3476)
print(bank.get_balance(3476))
bank.withdrawl(3476,9876)
print(bank.get_balance(3476))

bank.change_pin(3476,9800)
bank.display(9800)

 #INHERITANCE (Inheritance is an OOP feature where the child class acquires the properties and methods of parent class.)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"My name is {self.name}")

class Student(Person):
   pass

s1= Student("Krishna Singh",21)

s1.introduce()

# example 2: using super()

class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"My name is {self.name}")

class Student(Person):

    def __init__(self,name,age,roll,branch):

        super().__init__(name,age)

        self.roll=roll
        self.branch=branch

    def display(self):
        print(self.name)
        print(self.age)
        print(self.roll)
        print(self.branch)

s1 = Student("Krishna Singh",21,35,"AIML")

s1.display()
s1.introduce()

#METHOD OVERRIDING

class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

dog= Dog()
dog.sound()   # Python always prefers a child's version. This process is method overriding

# Practice question 1

class Animal:

    def __init__(self,name):
        self.name=name

    def sound(self):
        print("Some Animal Sound")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        
        self.breed=breed

    def sound(self):
        print("Bark")


    def display(self):
        print(f"The name of the animal is : {self.name}")
        print(f"The breed  of the animal is : {self.breed}")

dog = Dog("Rocky", "German Sephard")
dog.sound()
dog.display()

# Practice question 2

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):

    def __init__(self,name,age,salary,department):
        super().__init__(name,age)
        self.salary=salary
        self.department=department

    def display(self):
        print("------------EMPLOYEE DETAILS-----------")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f" Salary : {self.salary}")
        print(f"Department : {self.department}")

employee= Employee("Krishna Singh", 21, 23000, "ISRO")
employee.display()

# practice question 3

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"Hello, My name is {self.name}")

class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)

        self.employee_id= employee_id
        self.salary=salary

    def display_employee(self):
        print("-----------EMPLOYEE DETAIL-------------")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Emplyee ID : {self.employee_id}")
        print(f"Salary : {self.salary}")
        print("----------------------------------------")


class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department):
        super().__init__(name,age,employee_id,salary)

        self.department=department

    def display_manager(self):
        print("-----------MANAGER DETAIL-------------")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Emplyee ID : {self.employee_id}")
        print(f"Salary : {self.salary}")
        print(f"Department : {self.department}")
        print("----------------------------------------")

manager= Manager("Krishna singh",22,"ISR345",45000,"ML ENGINEER")
manager.introduce()
manager.display_employee()
manager.display_manager()

# POLYMORPHISM = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                Two ways to achieve POLYMORPHISM
#                1. Inheritance
#                2. "Duck Typing " = Objects must have necessary attributes/methods.


# example:
class Dog:
    def Sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")
    
dog=Dog()
cat=Cat()
cow=Cow()

dog.Sound()
cat.sound()
cow.sound()

#  EXample with Inheritance

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog= Dog()
cat= Cat()

dog.sound()       
cat.sound()    # method overriding

# DUCK TYPING "If it walks like a duck and quacks like a duck then treat it like a duck "
#        Python doesn't care about the class, It only cares whether the required method exists
#  example 1 :without duck typing

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

dog = Dog()
cat= Cat()

make_sound(dog)
make_sound(cat)

# example 2:

class Student:
    def introduce(self):
        print("I am a student")

class Teacher:
    def introduce(self):
        print("I am a teacher")

class Doctor:
    def introduce(self):
        print("I am a doctor")

def intro(person):
    person.introduce()



intro(Student())
intro(Teacher())
intro(Doctor())


# Duck Typing vs inheritance
# Many beginners think Duck Typing requires inheritance but actually it doesn't.
#Example:

class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def start_flying(obj):
    obj.fly()

start_flying(Bird())
start_flying(Airplane())

#example:

class CNN:
    def predict(self):
        print("Predicting images")

class LSTM:
    def predict(self):
        print("Predicting Text")

def run(model):
    model.predict()

run(CNN())
run(LSTM())

#example:

class WhatsApp:
    def send_message(self):
        print("Helps in sending gthe messgae")

class Instagram:
    def send_message(self):
        print("Interaction makes easier")
    
class Email:
    def send_message(self):
        print("Sends Emails")

def send(app):
    app.send_message()

send(WhatsApp())
send(Instagram())
send(Email())

#example:
    
class Student:
    def speak(self):
        print("Student Speaking")

class Teacher:
    def speak(self):
        print("Teacher Speaking")

def talk(person):
    person.speak()

talk(Student())
talk(Teacher())   # Duck Typing



# OPERATOR OVERLOADING python secretly calls __add__()
#                                          ex = 5+10
#                                          secretly becomes  5.__add__(10)

# RUNTIME POLYMORPHISM  he method that gets executed is decided while the program is running(at runtime) not before
#example:

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()

#example 2:

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")


animals= [Dog(), Cat()]

for animal in animals:
    animal.sound()

#practice question 1:

class Shape:
    def area(self):
        print("according to the shape")


class Circle(Shape):
    def area(self):
        print("Area of circle is 3.14 * (radius)**2")

class Rectangle(Shape):
    def area(self):
        print("Area of rectangle is length * breadth")

class Triangle(Shape):
    def area(self):
        print("Area of triangle is 1/2 * breadth * height")

def calculate_area(Shape):
    Shape.area()

calculate_area(Circle())
calculate_area(Rectangle())
calculate_area(Triangle())

#practice question 2

class Employee:
    def work(self):
        print("My parent is a employee")


class Developer(Employee):
    def work(self):
        print(" I am a developer")

class Tester(Employee):
    def work(self):
        print(" I am a Testerr")

class Manager(Employee):
    def work(self):
        print(" I am a Manager")

def work(person):
    person.work()

employee= Developer()
work(employee)

#practice question 3

class Vehicle:
    def move(self):
        print("My parent has a vehicle")

class Car(Vehicle):
    def move(self):
        print("I have a Car")

class Boat(Vehicle):
    def move(self):
        print("I have a Boat")

class Plane(Vehicle):
    def move(self):
        print("I have a Plane")

def move(vehicle):
    vehicle.move()

move(Car())
move(Boat())
move(Plane())

#practice question 4:

class Payment:
    def pay(self,amount):
        print(f"Paid Rs. {amount}")

class CreditCard(Payment):
    def pay(self,amount):
        print(f"Pay RS. {amount} using creditcard")

class UPI(Payment):
    def pay(self,amount):
        print(f"Pay RS.{amount} using UPI")

class NetBanking(Payment):
    def pay(self,amount):
        print(f"Pay RS. {amount} using NetBAnking")

payments=[CreditCard(),UPI(),NetBanking()]

for payment in payments:
    payment.pay(500)


#EXAMPLES OF POLYMORPHISM
#EXAMPLE 1:
class Animal:
    def sound(self):
        print("Some Animals Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals=[Dog() , Cat()]
for animal in animals:
    animal.sound()

#Example 2:

class Employee:
    def work(self):
        print("Employee working")

class Developer(Employee):
    def work(self):
        print("Works as a Developer")

class Tester(Employee):
    def work(self):
        print("Works as a tester")

class Manager(Employee):
    def work(self):
        print("Manages Team")

employees=[Developer(), Tester() , Manager()]
for emp in employees:
    emp.work()

#ABSTRACTION  means showing only the essential features and hiding the internal implementation
#example 1:

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started using push")

class Bike(Vehicle):
    def start(self):
        print("Bike started using self ")

class Truck(Vehicle):
    def start(self):
        print("Truck started using diesel engine")


car = Car()
bike= Bike()
truck= Truck()

car.start()
bike.start()
truck.start()

#example 2:

from abc import ABC ,abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(Payment):
    def pay(self,amount):
        print(f"paid RS.{amount} using UPI")

class CreditCard(Payment):
    def pay(self,amount):
        print(f"paid RS.{amount} using Creditcard")

class NetBanking(Payment):
    def pay(self,amount):
        print(f"paid RS.{amount} using Netbanking")
        
UPI().pay(500)
CreditCard().pay(500)
NetBanking().pay(500)

#Composition (HAS- A Relationship)

#EXample 1:

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine= Engine()

car= Car()
car.engine.start()

#example 2:

class CPU:
    def start(self):
        print("processing......")

class Computer:
    def __init__(self):
        self.cpu=CPU()

pc = Computer()
pc.cpu.start()

#example 3:

class Address:
    def __init__(self,city,state):
        self.city=city
        self.state=state

class Student:
    def __init__(self,name,city,state):
        self.name=name
        self.address= Address(city,state)

student= Student("Krishna singh", "lucknow", "Uttar Pradesh")

print(student.address.city)


#practice question 1:

class Engine:
    def __init__(self,company,horsepower):
        self.company= company
        self.horsepower= horsepower
        print(f"Engine of {self.company} with {self.horsepower} ")

    def start(self):
        
        print(f"Engine of {self.company} with {self.horsepower} has been started")



    def stop(self):
        
        print(f"Engine of {self.company} with {self.horsepower} has been started")


class Car:
    def __init__(self,brand,model,engine):
        self.brand= brand
        self.model=model
        self.engine= engine  # composition

    def display(self):
        print("------------CAR DETAILS-----------------")
        print(f"company : {self.engine.company}")
        print(f"horsepower : {self.engine.horsepower}")
        print(f"Brand : {self.brand}")
        print(f"Model ; {self.model}")

    def start_car(self):
        print(f" {self.brand}{self.model} model has been started")
        self.engine.start()

    def stop_car(self):
        print(f" {self.brand}{self.model} model has been stopped")
        self.engine.stop()
          
engine1 = Engine("BMW",500)

car1= Car("BMW", "MS", engine1)

car1.display()
car1.start_car()
car1.stop_car()

#Aggregation (HAS-A Relationship)  is a special form of composition where the child can exist independently of the parent.

class Employee:
    def __init__(self,name):
          self.name= name

    def display(self) :
         print(f"Employee name : {self.name}")

class Company:
    def __init__(self,company_name,employee):
          self.company_name= company_name
          self.employee= employee

    
emp= Employee("krishna singh")

company= Company("Microsoft",emp)

emp.display()

#practice question

class Teacher:
    def __init__(self,name,subject):
        self.name= name
        self.subject= subject

    def teach(self):
        print(f" {self.name} teaches {self.subject}")

class School:
    def __init__(self,school_name,teacher):
        self.school=school_name
        self.teacher= teacher


    def display(self):
        print(" --------------Details------------")
        print(f" Name : {self.teacher.name}")
        print(f" Subject : {self.teacher.subject}")
        print(f" school name : {self.school}")
        print("---------------------------")

    def start_class(self):
        print(f"{self.school} has now been started")
        self.teacher.teach()


teach= Teacher("Krishna singh", "Social Science")
school= School("Cross Belly International School", teach)

school.start_class()

# Magic (Dunder)
#Examples :
# __init__()

# __str__()
# __repr__()
# __len__()
# __add__()
# __eq__()


#example 1:  __init__()

class Student:
    def __init__(self,name):
        self.name= name

student= Student("Krishna singh")
print(student)   #<__main__.Student object at 0x000001ED1A557D60>

#example 2:  __str__()

class Student:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"Student name: {self.name}"
    
student=Student("krishna singh")
print(student)

#example 3:  __len__()
class Book:
    def __init__(self,pages):
        self.pages=pages

    def __len__(self):
        return self.pages
    
book= Book(345)
print(len(book))

# exaample 4: __add__()

class Money:
    def __init__(self,amount):
        self.amount=amount

    def __add__(self,other):
        return self.amount + other.amount
    

m1= Money(500)
m2= Money(590)
print(m1+m2)

#example 5:

class Student:
    def __init__(self,marks):
        self.marks=marks

    def __eq__(self,other):
        return self.marks== other.marks
    
s1= Student(98)
s2= Student(90)

print(s1==s2)

#Practice Question 1

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __str__(self):
        return f"Name : {self.name} , Marks : {self.marks}"

s1= Student("krishna singh",98)       
print(s1)



























