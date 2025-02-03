import random

random_num=random.randint(1,20)

for i in range(0,4):
    userinput=int(input(f"\t Guess the number\t\t\t\t{4-i} ❤️ \n\t"))
    if random_num==userinput:
        print("\n\t Congratulation You win!!!!!!!")
        break
    elif random_num>userinput:
        print("Entered number is smaller than actual number")
    else:
        print("Entered number is greater than actual number")

else:
    print(f"You lost the number was {random_num}")