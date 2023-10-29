#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?Rs."))
tip = int(input("What the percentage would like to give? 10,12 or 15 "))
people = int(input("How many people would like to split the bill?"))

# tip_percentage = tip/100
# bill_with_tip = bill*tip_percentage

tip_bill = bill*tip/100
total_bill = bill + tip_bill                          #bill_with_tip
bill_per_person = total_bill/people

final_amount="{:.2f}".format(bill_per_person)

print(f"Each person should pay:Rs.{final_amount}")
