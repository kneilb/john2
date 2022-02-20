input("WELCOME TO BIll CALCULATOR press enter to continue")

bill_amount = input("Please enter the bill amount:")
tip_percentage = input("Please enter the tip percentage:")
people_there = input("Please enter the amount of people sharing the bill:")

bill_amount = int(bill_amount)
tip_percentage = int(tip_percentage)
people_there = int(people_there)

tip_amount = bill_amount * tip_percentage / 100
total = tip_amount + bill_amount
tip_per = tip_amount / people_there
bill_per = total / people_there

print(f"The tip amount is {tip_amount}")
print(f"The total is {total}")
print(f"The tip per person is {tip_per}")
print(f"The total per person is {bill_per}")
