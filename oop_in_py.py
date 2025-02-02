class Student:
    def __init__(self, name, age, address):
        self.name= name
        self.age =age
        self.address= address

    def get_name(self):
        return self.name
    
student1= Student('bibek', 19,'kathmandu')
student2= Student('bg', 20,'lalitpur')
print(student1.get_name())
print(student2.name)

#class list 
    # def __init__(self, numbers):
    #     self.numbers=numbers
    # def append():
    #     pass