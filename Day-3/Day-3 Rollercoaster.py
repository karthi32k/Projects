print("Welcome'The Great karikalan Rollercoaster'")
height=int(input("What is your height in cm?"))
age=int(input("what is your age?"))
bill=0
# conditions
if(height>120):
        print("You are eligible to ride rollercoaster")
        if(age<=12):
            bill=5
            print("Child Ticket are $5")
        elif(age<=18):
            bill=7
            print("Youth Tickets are $7")
        elif(age>=45 and age<=55):
            bill=0
            print("Everything is going to be ok.Have a free ride on us")
        else:
            bill=12
            print("Audult Tickets are $12")
            
        want_photos=input("Do you want a photo taken? Yes or No")
        if(want_photos=='Yes'):
            bill+=3   
            print(f"Total bill for your ride with taken photo {bill}.")
        else:
            print(f"Total bill for your ride {bill}.")
else:
    print("Sorry,You are not eligible to ride")

