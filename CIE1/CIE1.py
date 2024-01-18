
# maximum and minimum

print("Enter first number: ")
num1=int(input())

print("Enter second number: ")
num2=int(input())

print("Enter third number: ")
num3=int(input())

if num1>num2 and num1>num3:
    print(f"{num1} is maximum number.")
elif num2>num1 and num2>num3:
    print(f"{num2} is maximum number.")
else:
    print(f"{num3} is maximum number.")

