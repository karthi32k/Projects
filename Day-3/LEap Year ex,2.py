#Solution 2 (slightly shorter than the first solution)

year=int(input("Which Year do you want to check?"))
         
if year % 4 == 0 and year % 100 > 0 or year % 100 == 0 and year % 400 == 0:

  print("Leap year.")

else:

  print("Normal year.")