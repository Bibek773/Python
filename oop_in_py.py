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
student=[]
class Stu:
    def __init__(self, name, age, address):
        self.name= name
        self.age= age 
        self.address= address

n=int(input("Enter the total no of student: "))
for i in range(n):
    
    name=input(f"enter name of {i+1}th student: ")
    age=input(f"enter age of {i+1}th student: ")
    address=input(f"enter address of {i+1}th student: ")

    std = Stu(name, age, address)
    student.append(std)
new=input("Enter the name of student to change address: ")
for stu in student:
    if stu.name==new:
        stu.address=input("Enter new address: ")
for stu in student:
    print(f"Name:{stu.name}\n Age: {stu.age}\n Address:{stu.address}")

