# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()
bill=0
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#size of the Pizza
if(size=="S"):
    bill+=15
elif(size=="M"):
    bill+=20
else:
    bill+=25

#add_pepperoni and Extra chesse
    if add_pepperoni == "y":
        bill+=1
    elif extre_cheese == "y":
            bill+=2
       
print(f"Here your final bill is {bill}")
       
      
