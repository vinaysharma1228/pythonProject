
def pyramid(n):
    i=1;

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")

        print()


def counter(n):
    i = 1
    count=1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(count, end=" ")
            count=count+1

        print()


def star(n):
    i = 1;

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")

        print()


def invertedPyramid(n):
    i = 1;

    for i in range(1, n + 1):
        for j in range(1, (n+1)-i):
            print("*", end=" ")

        print()


def nepaliFlag(n):
    i = 1;

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")

        print()

    i = 1;

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")

        print()

    i = 1;

    for i in range(1, n + 1):
        for j in range(1, 2):
            print("*", end=" ")

        print()

    print("Nepali Flag -:")



pyramid(5)
counter(5)
star(5)
invertedPyramid(5)
nepaliFlag(5)
