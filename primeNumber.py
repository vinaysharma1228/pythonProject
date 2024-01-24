import math

num = int(input("Enter number to check prime: "))

temp = 0
i = 2
while i <= math.sqrt(num):

    if num == 2:
        print("Number is prime.")
        break
    if num % i == 0:
        temp = temp + 1

    i = i + 1

if temp == 0:
    print("NUmber is prime.")
else:
    print("NUmber is not prime.")
