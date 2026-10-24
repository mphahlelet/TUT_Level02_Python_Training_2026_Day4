mark_str = input("Enter a mark between 0 and 100:")
print("Captured mark is:", f"{mark}")
print("")

if mark_str.isdigit():
    mark = int(mark_str)
       
    if 0 <= mark <= 100: 
        
        if mark >= 80 and mark <=100: # 80 <= mark <= 100:
            print("Outcome: Outstanding!")
        elif mark >= 70 and mark <=79:# 70 <= mark < 79:
            print("Outcome: Highly Competent!")
        elif mark >= 50 and mark <=69: # 50 <= mark < 69:
            print("Outcome: Competent!")
        elif mark >= 40 and mark <=49:# 40 <= mark < 49:
            print("Outcome: Not Yet Competent!")
        elif mark >= 0 and mark <=39: # 0 <= mark < 39:
            print("Outcome: Not Achieved!")
    else:
        print("Invalid mark! Only (0 - 100) allowed!")
        mark = int(input("Enter a mark between 0 and 100:"))

    
