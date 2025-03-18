#1 to print a program that prints the following (f-strings):

# print(f"My name is Blackie.\nI am 20 years old.\nI love python programming.")

#2 swapping variables. with two variables only 

# a=12
# b=10
# print(a,b,"before swapping the value of a and b  respectively")
# a=a+b 
# b=a-b 
# a=a-b
# print(a,b,"after swapping of a and b respectively")

#3 simple calculator

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))

# print("addition",a+b)
# print("subtraction",a-b)
# print("multiplication",a*b)
# print("division",a/b)

#4 type checking

# x=10
# y=3.14
# z="HUCISA"
# a=True

# print(type(x))
# print(type(y))  
# print(type(z))
# print(type(a))

#5 list operations

# a=[2,4,6,8,10]
# print(len(a),"the number of elements in the list")
# a[5]=12
# print(a,"after adding new number")

# print(a,"before removing the element")
# a.remove(2)
# print(a,"after removing the element")

# Max=max(a)
# Min=min(a)
# print(Max,Min,"the maximum and minimum elements in the list respectively")

#6 dictionary manipulation
# dic={"daniel":21,"abel":22,"john":23}
# dic["sami"]=24
# print(dic,"after adding new element")

# dic["abel"]=20
# print(dic,"after updating the element")

# del dic["daniel"]
# print(dic,"after removing the element")

#7 tuple Unpacking

# a=(10,20,30)
# b,c,d=a #tuple unpacking
# print(a,b,c)

#8 sum of even numbers
# s=0
# for i in range(1,101):
#     if i%2==0:
#         s=s+i
# print(s)

#9 factorial calculation

# n=int(input("enter the number:"))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)
#10 multiplication table
# def mul_table(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",n*i)

# n=int(input("enter the number:"))
# mul_table(n)
#11 reverse a string using loop

# s=input("enter the string:")
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end="")
#12 fibonacci sequence
# def fibonacci(n):
#     fib=[0,1]
#     for i in range(2,n):
#         fib.append(fib[i-1]+fib[i-2])
#     return fib

# n=int(input("enter the number:"))
# print(fibonacci(n))
#13 counts digits in a number 

# def count_digits(n):
#     return len(str(abs(n)))

# n=int(input("enter the number:"))
# print(count_digits(n))
#14 prime number check
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return "it is not prime"
#     return "it is prime"

# n=int(input("enter the number:"))
# print(prime(n))
#15 finding common elements
# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]

# common_elements=[element for element in list1 if element in list2]
# print(common_elements)
#16 define class
# class Student:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course

#     def display_info(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Course:",self.course)


# student1=Student("abel",20,"Computer Science")
# student1.display_info()

#16 inheritance
#Create a Course class with a method get_details(). Then, create a subclass WebDevClass that inherits from Course and overrides get_details().
# class Course:
#     def __init__(self,name):
#         self.name=name

#     def get_details(self):
#         print("Course name:",self.name)

# class WebDevClass(Course):
#     def get_details(self):
#         super().get_details()
#         print("Web Development Class")

# course=Course("Computer Science")
# course.get_details()

# web_dev_class=WebDevClass("Web Development")
# web_dev_class.get_details()
# #18 Encapsulation Implement a BankAccount class with a private balance attribute (__balance) and methods deposit() and withdraw(). Ensure that __balance cannot be accessed directly.
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance

#     def deposit(self,amount):
#         self.__balance+=amount

#     def withdraw(self,amount):
#         if self.__balance>=amount:
#             self.__balance-=amount
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.__balance

# account=BankAccount(1000)   
# account.deposit(500)
# account.withdraw(200)
# print(account.get_balance())
# 19 Polymorphism Create two classes, Car and Bike, both with a method move(). The Car should print "The car is moving fast", and Bike should print "The bike is moving slowly". Write a function that takes an object and calls move().
# class Car:
#     def move(self):
#         print("The car is moving fast")

# class Bike:
#     def move(self):
#         print("The bike is moving slowly")  

# def move_object(obj):
#     obj.move()

# car=Car()
# bike=Bike()
# move_object(car)
# move_object(bike)

#Method Overloading (Using Default Arguments Write a MathOperations class with a method add(), which should take either two or three numbers and return their sum. Use default parameters to achieve this.

# class MathOperations:
#     def add(self,a,b,c=0):
#         return a+b+c

# operations=MathOperations()
# print(operations.add(1,2))
# print(operations.add(1,2,3))



