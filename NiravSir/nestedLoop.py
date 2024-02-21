#
# list1=[1,2,3]
# list2=[7,8,9]
#
# for i in list1:
#     for j in list2:
#         print(i)


# for i in range(5):
#     for j in range(5):
#         print(i,end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

#
# for i in range(5):
#     for j in range(5):
#         print(j+1,end=" ")
#     print()

for i in range(5):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()
