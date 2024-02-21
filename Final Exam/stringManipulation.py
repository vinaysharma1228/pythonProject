

def space(str):
    cspace=0
    for i in str:
        if i==' ':
            cspace=cspace+1

    return cspace
def vowel(str):

    vcount=0
    ccount=0
    for i in str:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            vcount=vcount+1
        else:
            ccount=ccount+1

    return list[vcount,ccount]
def stringManipulation():
    while True:
        num = input("Enter String (x for exit.): ")

        if num == 'x':
            break

        print("Length is : ",len(num))
        print("Reverse is : ",num[::-1])
        print("Vowel,consonant letter present : ",vowel(num))
        print("Space is : ",space(num))
        print("Capital")


stringManipulation()