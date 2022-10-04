# 1. Write a python program to create a user class with 3 properties : name, age, email.
# 2. Write a python program to create a user class with a method to greet the user.
# 3. Write a python program to create 2 objects of the user class and assign different
# values.
# 4. Write a python program to init default values for user object using __init__ method.
# 5. Write a python program to delete the age property of the user.
# 6. Write a python program to create 3 user objects and find the youngest of all.
# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
# hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
# values).
# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
# order based on the ram size.
# 9. Write a python program to create a School class and 3 instance variables and 1 class
# variable.
# 10. Define a class Employee with instance object variables empid, name, salary. Write
# __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field values



# 1) .......................................................
# class User:
#     x=1
#     def __init__(self,name,age,email):
#         self.name=name        
#         self.age=age
#         self.email=email
# b1=User('harikesh',18,'xyz@gmail,com')
# print(b1.__dict__)


# 2) ......................................................
# class user :
#     def __init__(self,a) -> None:
#         self.a=a
#         print('geerting for your topper!',self.a)
        
# u1=user('harry')
# print(u1.__dict__)


# 3) ......................................................
# class user:
#     def __init__(self,a) -> None:
#         self.a=a
#         print('a =',self.a)
#     def f1(self):
#         self.b=200
#         print('b =',self.b)
        
# u1=user(100)

# u1.f1()
# print(u1.__dict__)


# 4) ...........................................................
# class user:
#     def __init__(self,a) -> None:
#         self.a=a
#         print('a =',self.a)
#     def f1(self):
#         self.b=200
#         print('b =',self.b)
        
# u1=user(100)
# u2=user(200)
# print(u1.__dict__)


# 5) ....................................................
# class user:
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age
#         
        
# a1=user('harikesh',18)
# del a1.age
# print(a1.__dict__)


# 6) ...........................................................
# class young:
#     def __init__(self,a,b,c) -> None:
#         self.a=a
#         self.b=b
#         self.c=c
    
#     def check_youngest(self):
#         if self.a<self.b:
#             if self.a<self.c:
#                 print(self.a)
#             else:
#                 print(self.c)
#         elif self.b<self.c:
#             print(self.b)
#         else:
#             print(self.c)
            
         
# y1=young(1,2,3)
# y1.check_youngest()


# 7) .........................................................
# class laptop:
#     def __init__(self,brand, ram, cpu,ssd) -> None:
#         self.brand=brand
#         self.ram=ram
#         self.cpu=cpu
#         self.ssd=ssd
    
#     def showCinfig(self):
#         print(self.brand)
#         print(self.ram)
#         print(self.cpu)
#         print(self.ssd)
        
# l=laptop('dell','16GB',6200,'256GB')
# l.showCinfig()


# 8) .............................................................
# l=[]
# class laptop:
#     def __init__(self,ram) -> None:
#         self.ram=ram
#         l.append(self.ram)     
#         l.sort()
#         print(l)
        
# l1=laptop("16GB")
# l2=laptop("4GB")
# l3=laptop("8GB")


# 9) ................................................
# class School:
#     class_var=40  #class variable 
#     def __init__(self,a) -> None:
#         self.a=a
#         self.b=20
#         self.c=30
#         print(self.a,self.b,self.c)
    
    
# def main():
#     s=School(10)
#     print(s.__dict__)
#     print(School.class_var)
# main()


# 10) ...........................................................
l=[]
class Employee:
    def __init__(self,empid, name, salary) -> None:
        self.empid=empid
        self.name=name
        self.salary=salary
        
    def show(self):
        print(self.empid,self.name,self.salary)
        
def main():         
    while True:
        ans=input("Enter ans [y/n] : ")    
        if ans=='y':
            e=Employee(
            input("Enter empid : "),(input("Enter name : ")),int(input("Enter salary : ")))
            e.show()
main()