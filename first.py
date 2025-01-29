print('hello world')
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

a="string"
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
a=[]
fruit1=input("Enter the first fruit")
a.append(fruit1)
fruit2=input("Enter the second fruit")
a.append(fruit2)
fruit3=input("Enter the third fruit")
a.append(fruit3)
print(a)
b=[]
m1=int(input("Enter the first mark"))
b.append(m1)
m2=int(input("Enter the second marks"))
b.append(m2)
m3=int(input("Enter the third marks"))
b.append(m3)
b.sort()
print(b)