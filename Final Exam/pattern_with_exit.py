def printPattern():
    while True:
        num = int(input("Enter number between 1 to 4 pattern print and 5 for exit : "))

        if num == 1:
            for i in range(1, 6):
                for j in range(1, i + 1):
                    print(j, end=" ")
                print()

        elif num==2:
            for i in range(1, 6):
                for j in range(1, i + 1):
                    print(i, end=" ")
                print()
        elif num==3:
            for i in range(1, 6):
                for j in range(1, i + 1):
                    print("*", end=" ")
                print()
        elif num==4:
            for i in range(1, 6):
                for j in range(1, i + 1):
                    print(i+j, end=" ")
                print()

        elif num==5:
            break


printPattern()
