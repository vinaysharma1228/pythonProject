print("Enter number to find sum of each digit: ",end=' ')
num = int(input())
summ = 0
original_num=num

while num != 0:
    rem = num % 10
    summ=(summ*10)+rem
    num //= 10

print(summ)
