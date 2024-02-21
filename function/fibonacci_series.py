def fibonacci(limit):
    n = limit
    i = 1
    first = 0
    second = 1

    print(first, second, end=" ")
    while i <= n - 2:
        sum = first + second
        print(sum, end=" ")
        first = second
        second = sum
        i = i + 1


limit = int(input("Enter limit of fibonacci series: "))
fibonacci(limit)
