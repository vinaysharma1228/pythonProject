
def factorial(x):
    fact=1
    i=1
    while i<=x:
        fact*=i
        i=i+1
    return fact


n=int(input("Enter a number : "))
print(f"Factorial of {n} is : ",factorial(n))
