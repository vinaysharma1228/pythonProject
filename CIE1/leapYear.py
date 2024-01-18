
print("Enter Year: ")
year=int(input())

if year%4==0:
    if year%100 and year%400 !=0:
        print(" Not Leap Year")

    else:
        print("Leap Year")

else:
    print("Not a leap year.")