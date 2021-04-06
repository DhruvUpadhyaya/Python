#Tip Calculator
print("Welcome to the tip calculatore.")
total_bill = float(input("What was the total bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
num_of_people = int(input("How many people to split the bill\n"))
tip = total_bill*tip_percentage/100
amount_each = (total_bill+tip)/num_of_people
amount_round = round(amount_each,2)
final_amount = "{:.2f}".format(amount_round)
print(f"Each person should pay: ${final_amount}")