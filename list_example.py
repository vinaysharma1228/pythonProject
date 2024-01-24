
list=[23,45,67]
print(type(list))

print("Inserting....")
list.insert(3,61);
list.insert(2,51);
list.insert(4,1);
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

# // heigth=23.45,72.14,11.12,7.5,23.14
# insert 3 postion-> 14
# reverse the list
# insert negative value at the starting of the list
#
# sort your data
# insert duplicate 3 values with the series of 30
#
# remove negation value from list
#
# reverse your data
#
# count the value int the list
# delete the data which is start from 3
# display ascending order data->

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






x=[67,{78,89},(90)]
print(type(x))

y=(56,{78,56},[34,67,8])
print(type(y))


z={(56,56),(1,2),78,34,56,9}
z.add(1)

print(z)
z.pop()

print(z)
z.remove(78)

print(z)
z.clear()
print(z)





