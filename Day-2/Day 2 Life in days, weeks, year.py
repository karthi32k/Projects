#Period of Life Calculator

age = input("What is your current age? ")

print("Average life_in_years = 90years")

fixed_age = int(input("How long you want live?"))

#Write your code below this line 👇

age_as_int = int(age)

life_in_days=int(age_as_int*365)
left_days=int((fixed_age*365)-life_in_days)

life_in_weeks=int(age_as_int*52)
left_weeks=int((fixed_age*52)-life_in_weeks)

life_in_months=int(age_as_int * 12)
left_months=int((fixed_age*12) - life_in_months)

life_in_years = int(fixed_age-age_as_int)

print(f"you have {life_in_days} days,{life_in_weeks} weeks,{life_in_months} months, {age_as_int} years completed")

print(f"you have {left_days}days,{left_weeks}weeks,{left_months}months, {life_in_years} years left")
