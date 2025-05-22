print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = total_bill * (tip_percentage / 100)
total_bill_with_tip = total_bill + tip
bill_per_person = round(total_bill_with_tip / people, 2)
print(f"Each person should pay: ${bill_per_person}")