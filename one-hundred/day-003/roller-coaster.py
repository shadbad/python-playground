print("welcome to the rollercoaster!")
height = int(input("What is your height in CM? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you? "))
    total_cost = 0
    if age < 12:
        print("Your ticket costs $5")
        total_cost = 5
    elif age < 18:
        print("Your ticket costs $7")
        total_cost = 7
    else:
        print("Your ticket costs $12")
        total_cost = 12
    include_photo = input("Would you like us to take a photo of you? (y/n) ")
    if include_photo == "y":
        total_cost += 3
    
    print(f"your ticket costs {total_cost}")
else:
    print("Sorry you have to grow taller before you can ride the rollercoaster.")