# print('hello world')
#a=71
#print(a)
#a="bibek"
#print(a)
#b=56
"""sum=a+b
sub=a-b
mul=a*b
div=a/b
print(sub)
print(sum)
print(mul)
print(div)"""


"""a=10;
print(type(a))
print(str(a))
print(int(a))
print(float(a))
"""
"""
a=input("enter a number")
b=input("enter no ")
print(a+b)"""
"""
a=int(input("enter a number"))
b=int(input("enter no "))
print(a+b)"""

#a="string"
# print(a[4])
# print(a[0:3])#0 1 2 index ko print hunxa
# print(a[3:])# last ko 3 index ko print hunxa
# # print(a[::3])
# print(len(a))
## print(a.count('s'))
# print(a.capitalize())
# print(a[-1])# reverse order ma first index
# print(a.find('ng'));


### escape sequence

# a="bibek \n \t \' \\"
# print(a)

# print("hello", end="")#by default last ma \n hunthyo end le khali string rakhi diyo
# print("world")
# sum=int(6)+int(6)
# print("your sum is :" + str(sum))
# print(f'your sum is :{sum}')
# a=(input("Enter your name"))
# print("Good morning "+ a)
# #OR
# # print(f'hello {a} \n')
# l1=[1,9,3,4,2]
# print(l1)
# print(l1[1])
# print(l1[:3])
# l1.sort()#list lai sort garera list mai save garxa
# print(l1)
# l2=l1#new list create gardaina l1 kai list ma point garxa
# print(l1 is l2)
# l2=l1.copy()#new list create garxa
# print(l1 is l2)
# print(l1.reverse())#reverse chai garxa tara return gardaina
# print(l1)
# l1.append(9)
# print(l1)
# l1.insert(3,5)
# print(l1)
# l1[3]=78
# print(l1)
# l1.pop()#last element pop huxa
# print(l1)
# a=l1.pop()#poped value a ma store huxa
# print(a)
# l1.pop(2)#index 2 ko pop huxa
# print(l1)
# l1.remove(1)#value check garera if tyo value xa vane teslai remove garxa
# print(l1)
# a=()#square bracket le list banauxa small  bracket le tupel banauxa... tupel ma insert remove garna mildaina
# a=(1,2,3,4)
# print(type(a))
# print(a)
# a=[]
# fruit1=input("Enter the first fruit")
# a.append(fruit1)
# fruit2=input("Enter the second fruit")
# a.append(fruit2)
# fruit3=input("Enter the third fruit")
# a.append(fruit3)
# print(a)
# b=[]
# m1=int(input("Enter the first mark"))
# b.append(m1)
# m2=int(input("Enter the second marks"))
# b.append(m2)
# m3=int(input("Enter the third marks"))
# b.append(m3)
# b.sort()
# print(b)
# a={
#     "name":"bibek",
#     "age": [20,34,35],
#       "roll":{
#           "a":100,
#           'b':12
#       }

# }# key vlaue
# print(a["roll"])
# print(a.keys())
# print(a.values())
# print(a['roll']['a'])
# a={
#     "name":input("Enter your name: "),
#     "age":int(input("enter your age: ")),
#     "roll":int(input("Enter your rollno: ")),
#     "marks":{
#         "maths":int(input("enter your marks of maths: ")),
#         "English":int(input("enter your marks of English: ")),
#         "Science":int(input("enter your marks of Science: "))
#         }
# }
# print("\nName:",a["name"])
# print("Age",a["age"])
# print("Roll Number",a["roll"])
# print("\nMaths:",a["marks"]["maths"])
# print("Science:",a["marks"]["English"])
# print("English:",a["marks"]["Science"])
# total=a["marks"]["maths"]+a["marks"]["English"]+a["marks"]["Science"]
# print("\nTotal=",total)
# print(f"percentage={(total/3)}%")
# if (total/3)>40:
#     print("Pass ✔️")
# else:
#     print("Failed ❌")
# l1=[1,2,39]
# for i in l1:
#     print(i)
# for i in range(10):
#     print(i)
#even no
# for i in range(11):
#     a=i%2
#     if a!=0:
#         continue
#     print(i)
# for i, name in enumerate(["bibek", "shasanka", "oshan"]):
#     print(f"{i}: {name}")
# row=5
# for i in range(row):
#     for j in range(row-i):
#         print("*\t", end=" ")
    
#     print()
# #factorial
# num=int(input("enter number "))
# factorial=1
# for i in range(1,num+1):
#     factorial*=i
# print(f"The factorial of {num} is {factorial}")
#fibonacci
# num= int(input("enter number "))
# a,b=0,1
# for i in range(num):
#     print(a, end="")
#     a,b=b, a+b
## 512-----> 5+1+2
# num= int(input("enter number "))
# b=0
# for i in range(num):
#     a=int(num%10)
#     b+=a
#     num=int(num/10)
# print(b)
# num= int(input("enter number "))
# nun=num
# b=0
# while(num>0):
#     a=int(num%10)
#     b=b*10+a
#     num=num//10
# print(b)
# if b==nun:
#     print(" palindrome")
# def add (a, b):
#     return a+b
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# result = add(a, b)
# print(result)
# def add(x,y, *args):
#     sum=0
#     print(args)
#     for num in args:
#         sum+=num
#     return sum
# result= add(1,2,3,4,5)
# print("Sum:", result)
# x,y, *unpack =[1,2,3,4,5,6]
# print(unpack)
# ##args
# def add(*args):
#     sum=0
#     for num in args:
#         sum=sum + num
#     return sum
# a=[]
# b=int(input("Enter the No. of data: "))
# for i in range(b):
#     c=int(input(f"Enter the {i+1} th term"))
#     a.append(c)
# result=add(*a)
# print("sum:", result)
"""student management system"""
# def add():
#     global count 
    
#     name=input("Enter the name of Student: ")
#     roll=int(input("Enter your roll no."))
#     faculty=input("Enter Your Faculty")
#     s={ 
#         "name":name,
#         "ROLL":roll,
#         "faculty":faculty
#     }
#     student.append(s)
#     print("Successfully added student")
#     print(count)
#     count += 1
# def display():
#     for i in range(count):
#         print(f'Name:{student[i]["name"]} \nRoll:{student[i]["ROLL"]} \nFaculty: {student[i]["faculty"]}\n')
    
# def search():
   
#     a=int(input("Enter the the roll no you want to search"))
#     for i in range(count):
#         if a==student[i]["ROLL"]:
#             print(student[i]["name"])
# def update():
#     w=int(input("Enter the rollno you have incorrectly entered"))
#     for i in range(count):
#          if w==student[i]["ROLL"]:
#             while(1):
#                 x=input("Enter what you have incorrectly entered \n1.Name\n2.rollno\n3.faculty")
#                 if x==1:
#                     student[i]["name"]=input("Enter correct Name\n")
#                     break
#                 elif x==2:
#                     student[i]["roll"]=int(input("Enter correct Roll\n"))
#                     break
#                 elif x==3:
#                     student[i]["roll"]=input("Enter correct Faculty\n")
#                     break
#                 else:
#                     print("Enter correct value:")
#                     break
# def delete():
#    y=int(input("Enter the rollno you have incorrectly entered"))
#    for i in range(count):
#          if y==student[i]["ROLL"]:
#             student.pop(i)
# student=[]
# count = 0
# while(1):
#     choice=int(input("Enter your choice\n 1. add student\n 2. display student list\n 3. search student\n 4. update \n 5. delete\n 6. exit"))
#     if choice==1:
#         add()
#     elif choice==2:
#         display()
#     elif choice==3:
#         search()
#     elif choice==4:
#         update()
#     elif choice==5:
#         delete
#     elif choice==6:
#         print("Exiting the program")
#         break
#     else:
#         print("invalid choice")
"""inporting a library"""
##rock sissor paper 
# from random import randint as r

# def main(temp, user):
#     if temp == user:
#         print("It's a draw")
#     elif (temp == 'r' and user == 's') or (temp == 's' and user == 'p') or (temp == 'p' and user == 'r'):
#         print("You lose")
#     else:
#         print("You win")
# while(1):
#     play=input("enter p to play")
#     if play=='p':
#         game = ['r', 'p', 's']
#         temp = game[r(0, 2)]
#         user = input("Enter r for rock, s for scissors, p for paper: ")
#         main(temp, user)
#     else:
#         break
"""try and except"""
# try:
#     num1= int(input("Enter a number"))
#     num2= int(input("Enter a number"))
#     result=num1/num2
#     print("Result:", result)
# except Exception as e:
#     print(e)
# else:#exception ma error aayena vane else ma aauxa 
#     print("no error")
# # finally:
# #     print("End")#finally chai program crash vaye pani run hunxa
# try:
#     num=int(input("enter any no"))
#     if num<0:
#         raise ValueError("Number cannot be negative")#the raise statement is used to trigger exceptions manually
# except ValueError as error:
#     print(error)
""""""
# a=[]
# tot=5
# for i in range(tot):
#     roll=int(input("Enter roll no: "))
#     try:
#         if roll in a:
#             raise ValueError("This roll number is already entered\n")
#     except ValueError as e:
#         print(e)
#     else:
#         a.append(roll)
#         print(f"{roll} has successfully added\n")
"""nested try"""
# def triangle(x,y,z):
#     try:
#         if ((x+y)<z) or ((x+y)<z) or ((x+y)<z):
#             raise ValueError("Given value doesn't satisfies triangle")
#     except:
#         raise
#     else:
#         print("this is a triangle")
#     return 


# try:
#     a=int(input("Enter first side of triangle"))
#     b=int(input("Enter second side of triangle"))
#     c=int(input("Enter third side of triangle"))
#     triangle(a,b,c)
# except ValueError as e:
#     print(e)

"""recursive function"""
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n* factorial(n-1)
# result= factorial(5)
# print(f"Result:{result} ")
"""sum of natural no"""
# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n+ sum(n-1)
# result= sum(10)
# print(f"Result:{result} ")
"""fibonacci series"""
# def fibo(n):
#     if n<=1:
#         return 
#     else:
#         return fibo(n-1)+fibo(n-2)
# for i in range(10):
#     print(f"\t{fibo(i)}", end="")
# print()
"""function over loading """

# def sum(a:int, b=0, c=0):
#     print(a+b+c)


# a=1
# b=2
# c=3
# sum(a)
# sum(a,b)
# sum(a,b,c)
def sum(*args):
    result = 0
    for num in args:
        result += num
    print(result)

a = 1
b = 2
c = 3

sum(a)       
sum(a, b)    
sum(a, b, c) 
