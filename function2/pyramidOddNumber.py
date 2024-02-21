
def printPyramidOddNumber(n):
    odd=1
    for i in range(1,n+1):
        for k in range(1,n-i+1):
            print(" ",end="")
        for j in range(1,i+1):
            print(odd,end=" ")
            odd=odd+2

        print()


n=int(input("Enter number of row : "))
printPyramidOddNumber(n)