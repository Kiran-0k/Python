myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
for i in myList:
    temp = myList[i]
    if temp in myList:
        del myList[i]

#
print("The list with unique elements only:")
print(myList) 
