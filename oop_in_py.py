# class Student:
#     def __init__(self, fname, lname, age, address):
#         self.name= fname
#         self.lname= lname
#         self.age =age
#         self.address= address

#     def get_name(self):
#         return self.name + ' ' + self.lname
#     def update_address(self, address):
#         self.address= address
# student1.update_address=
# student1= Student('bibek',"ghimire", 19,'kathmandu')
# student2= Student('bg', "g",20,'lalitpur')
# print(student1.get_name())
# print(student2.name)

# #class list 
#     # def __init__(self, numbers):
#     #     self.numbers=numbers
#     # def append():
#     #     pass"""
"""append obj in the list"""
# student=[]
# class Stu:
#     def __init__(self, name, age, address):
#         self.name= name
#         self.age= age 
#         self.address= address

# n=int(input("\nEnter the total no of student: "))
# for i in range(n):
    
#     name=input(f"\nenter name of {i+1}th student: ")
#     age=input(f"\nenter age of {i+1}th student: ")
#     address=input(f"\nenter address of {i+1}th student: ")

#     std = Stu(name, age, address)
#     student.append(std)

# new=input("\nEnter the name of student to change address: ")
# for stu in student:
#     if stu.name==new:
#         stu.address=input("\nEnter new address: ")
#     else:
#         print("\nName does not match")
# for stu in student:
#     print(f"\nName:{stu.name}\n Age: {stu.age}\n Address:{stu.address}\n")

class Student:
    def __init__(self, fname, lname, age, address):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.address = address

    def __repr__(self):
        return f'{self.fname} {self.age} {self.address}'

    def __len__(self):
        return self.age

    def __str__(self):
        return f'{self.fname}'
    def __add__(self, other):
        return self.fname+other.fname
    def __mul__(self, other):
        return self.age*other.age

student_list = [Student('Bibek', 'Ghimire', 19, 'Kathmandu'), Student('BG', 'G', 20, 'Lalitpur')]

print(student_list)

print(len(student_list))

print(str(student_list))

print(student_list[0] * student_list[1])

# for student in student_list:
#     print(f'Student: {student}, Age: {len(student)}')
