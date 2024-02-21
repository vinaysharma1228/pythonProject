
def checkVowelConsonant(ch):

    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        print(f"{ch} is vowel.")
    else:
        print(f"{ch} is Consonant.")


str=input("Enter character to check vowel or not : ")
checkVowelConsonant(str)