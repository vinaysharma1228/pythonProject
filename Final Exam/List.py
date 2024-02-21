
list=[23,45,67]
print(type(list))

print("Inserting....")
list.insert(3,61)
list.insert(2,51)
list.insert(4,1)
print(list)

print("Pop ....")
print(list.pop())
print(list)

print("Removing...")
list.remove(23)
print(list)

print("Sorting ....")
list.sort()
print(list)


height = [23.45, 72.14, 11.12, 7.5, 23.14]
print("Inserting...")
print(len(height))
height.insert(3,14)
print(height)

print("Reversing...")
height.reverse()
print(height)

print("Inserting negative value at starting postion...")
height.insert(0,-10)
print(height)

print("Sorting ....")
height.sort()
print(height)

print("Inserting duplicate Values...")
height.insert(2,30)
height.insert(2,30)
height.insert(2,60)
height.insert(2,60)
height.insert(2,90)
height.insert(2,90)

print(height)

count=len(height)
for i in range(0,count-1):
    if height[i]<0 :
        height.remove(height[i])


print(height)

print("Reversing Again..")
height.reverse()
print(height)

print("Counting element: ")
print(len(height))
print(height)

print("Deleting data which is at 3 position.")
height.pop(3)
print(height)
print("Displaying ascending order...")
height.sort()
print(height)













