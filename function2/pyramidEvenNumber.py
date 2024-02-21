
def printPyramidEvenNumber(n):
    even=2
    for i in range(1,n+1):
        for k in range(1,n-i+1):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(even,end=" ")
            even=even+2

        print()


n=int(input("Enter number of row : "))
printPyramidEvenNumber(n)