print("Enter number to find sum of each digit: ", end=' ')
num = int(input())
summ = 0
original_num = num

while num != 0:
    rem = num % 10
    summ += (rem * rem * rem)
    num //= 10

if summ == original_num:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
