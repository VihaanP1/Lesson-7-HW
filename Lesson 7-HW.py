y = int(input("Enter a year: "))
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("The year is a leap year")
else: 
    print("The year is not a leap year")


C = int(input("Enter your temperature in degrees Celsius: "))
F = (C * 9/5) + 32
print(F, "F")