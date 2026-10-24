mark = int(input("Enter mark or -1 to stop: "))
total = 0
while mark != -1:
    print(f"The entered mark is {mark}")
    total+=mark
  
    
    mark = int(input("Enter mark or -1 to stop: "))
print('')
print(f'Total Mark: {total}')
