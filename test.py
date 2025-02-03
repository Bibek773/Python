"""decorator"""
# def decorator(func):
#     def wrapper():
#         print("first")
#         func()
#         print("second")
#     return wrapper
# @decorator 
# def hello():
#     print("hello")
# hello()
""""""
# commands= {}
# def command(func):
#     def wrapper():
#         commands[func.__name__] = func
#     return wrapper
# @command
# def hello():
#     print("hello world")
# @command
# def tey():
#     print("this is tey")

# hello()#function call garera dictonary ma store gareko
# tey()
# commands['tey']()
# print(commands)

abc = {}

def fnc(func):
    def wrapper():
        abc[func.__name__] = func
        # func()
    return wrapper

@fnc
def evening():
    print("This is evening")

@fnc
def morning():
    print("This is morning")

@fnc
def night():
    print("This is night")
@fnc
def day():
    print("This is day")

morning()
day()
evening()
night()

user_input = input("\nAvailable functions:\n 1. morning\n 2. day\n 3. evening\n 4. night\n \t Enter any: ")

abc[user_input]()
