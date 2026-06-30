#This program prints a pyramid pattern of numbers with spaces.
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(f"_",end="")
        j=j+1
    j=1    
    while j<=i:
        print(f"{j}",end="")
        j=j+1
    j=i-1    
    while j>=1:
        print(f"{j}",end="")
        j=j-1
    print(f"")
    i=i+1