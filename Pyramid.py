blocks = int(input("Enter the number of blocks: "))
n = 2
while blocks >= 0:
    level = max(range(1,n))
    blocks -= level
    n += 1

print("The height of the pyramid:", level-1) 
