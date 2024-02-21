
def reverseString(s):
    n=len(s)
    i=n-1

    while(i>=0):
        print(s[i],end="")
        i=i-1


x=input("Enter string : ")
reverseString(x)