def decorator(func):
    def wrapper():
        print("first")
        func()
        print("second")
    return wrapper
@decorator 
def hello():
    print("hello")
hello()