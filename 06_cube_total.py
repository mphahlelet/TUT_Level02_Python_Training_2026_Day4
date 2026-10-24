import math

number = int(input("Enter a whole number:"))
total = 0
cube = 0
if number <= 0:
        print("Invalid number entered!")
        print("No Total")
else:
    
    for n in range(1,number + 1):
        cube = pow(n,3)
        print(cube, end=" ,")
        total = total + cube
        

    print(" Total:",total)