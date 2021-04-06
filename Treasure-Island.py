# Treasure Island Project
print("Welcome to the rolarCoaster ride")
height = int(input("What is your height?\n"))
if height >= 120:
    print("You can ride hurray!!")
    age = int(input("What is your age taller!!"))
    if age <= 12:
        print("You need to pay $5")
    elif age<18:
        print("You need to pay $7")
    else:
        print("You need to pay $18")
else:
    print("Grow up baby then come!! ha ha haaaa")