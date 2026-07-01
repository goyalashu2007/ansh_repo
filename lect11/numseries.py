#This program is used to print the numbers in a specific series in a pattern.
x=1
for i in range(1,5):
    for j in range(1,i+1):
        print(f"{x}",end=" ")
        x=x+1
    print(f"")    