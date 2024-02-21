
def mini_cal():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    ch = input("Enter operator(+,-,*,/) : ")

    if ch == '+':
        print("Addition is : ", num1 + num2)

    elif ch == '-':
        print("Subtraction is : ", num1 - num2)

    elif ch == '*':
        print("multiplication is : ", num1 * num2)

    elif ch == '/':
        print("Division is : ", num1 / num2)

    else:
        print("Invalid input..")


mini_cal()  
