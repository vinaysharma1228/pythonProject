
def pattern(limit):

    for i in range(1,limit):
        for j in range(1,i+1):
            print(j,end=" ")

        print()

limit=int(input("Enter limit: "))
pattern(limit)