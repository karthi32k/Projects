#Leap Year Exercise
Year=int(input("Which Year do you want to check?"))
#
if(Year%4==0):
    if(Year%100==0):
        if(Year%400==0):
            print("Leap Year")
        else:
              print("Not a leap Year")
    else:
        print("leap Year")
else:
    print("Not a Leap Year")