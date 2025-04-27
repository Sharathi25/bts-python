# class MyPhone:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# phone = MyPhone(brand="Apple", model="14")
# phone1 = MyPhone(brand="Apple", model="14")
# print(phone.brand, phone.model)
# print(phone1.brand, phone1.model)

# class Student:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#     def display(self):
#         print(self.name)
#         print(self.roll_no)


# student = Student(name="Sharathi", roll_no="001")
# student.display()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def Adult(self):
#         if self.age >= 18:
#             return True
#         else:
#             return False

# P1 = Person("SHARATHI", 25)
# print(P1.Adult())


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def __give_raise(self, amount):
        self.__salary += amount

    def display(self):
        print(self.__name)
        print(self.__salary)
        self.__give_raise(1000)

e1  = Employee("SHARATHI", 25000)
print(e1.display())
# e1.__give_raise(1000)

e1.display()  