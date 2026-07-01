#This program prints a pattern of numbers using nested for loops
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"{j}", end=" ")
    print(f"")