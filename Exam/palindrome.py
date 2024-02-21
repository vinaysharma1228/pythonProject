##create a function in python where you need to perform palindrome
number = input("Enter Number : ")


def palindrome(number):
    num = number[::-1]

    if num == number:
        print("palindrome")
    else:
        print("not palindrome")


palindrome(number)
