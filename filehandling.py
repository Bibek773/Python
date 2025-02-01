import json

def add():
    global count 
    
    name = input("Enter the name of Student: ")
    roll = int(input("Enter your roll no.: "))
    faculty = input("Enter Your Faculty: ")
    s = { 
        "name": name,
        "ROLL": roll,
        "faculty": faculty
    }
    student.append(s)
    try:
        with open('student.json', 'w') as file:
            json.dump(student, file)
        print("Successfully added student and updated student.json file.")
    except Exception as e:
        print(f"An error occurred while writing to student.json file: {e}")
    print(count)
    count += 1

def display():
    for i in range(count):
        print(f'Name: {student[i]["name"]} \nRoll: {student[i]["ROLL"]} \nFaculty: {student[i]["faculty"]}\n')

def search():
    a = int(input("Enter the roll no. you want to search: "))
    for i in range(count):
        if a == student[i]["ROLL"]:
            print(student[i]["name"])

def update():
    w = int(input("Enter the roll no. you have incorrectly entered: "))
    for i in range(count):
        if w == student[i]["ROLL"]:
            while True:
                x = input("Enter what you have incorrectly entered \n1. Name\n2. Roll no.\n3. Faculty: ")
                if x == "1":
                    student[i]["name"] = input("Enter correct Name: ")
                    break
                elif x == "2":
                    student[i]["ROLL"] = int(input("Enter correct Roll: "))
                    break
                elif x == "3":
                    student[i]["faculty"] = input("Enter correct Faculty: ")
                    break
                else:
                    print("Enter correct value:")
                    break

def delete():
    y = int(input("Enter the roll no. you have incorrectly entered: "))
    for i in range(count):
        if y == student[i]["ROLL"]:
            student.pop(i)
            try:
                with open('student.json', 'w') as file:
                    json.dump(student, file)
                print("Successfully deleted student and updated student.json file.")
            except Exception as e:
                print(f"An error occurred while writing to student.json file: {e}")

student = []
count = 0
while True:
    choice = int(input("Enter your choice\n1. Add student\n2. Display student list\n3. Search student\n4. Update\n5. Delete\n6. Exit: "))
    if choice == 1:
        add()
    elif choice == 2:
        display()
    elif choice == 3:
        search()
    elif choice == 4:
        update()
    elif choice == 5:
        delete()
    elif choice == 6:
        print("Exiting the program")
        break
    else:
        print("Invalid choice")
