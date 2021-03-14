myList= [1.5, 3, 5, 3.5, 7, 9, 7.5, 1] #odd numbers
myList2= [c for c in range(2,17,2)] #even numbers

myList.extend(myList2)

for i in myList:
    i *= 2
    print(i)
    print(type(i))