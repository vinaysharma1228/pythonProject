x=[42,37.5,43,1,21,13]

length=len(x)
mid=int(length/2)
print(x[::-1])
print(x[mid])
print(x[length-1])
x[length-1]=31
print(x)
print(x[3])
