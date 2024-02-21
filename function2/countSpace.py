
def countSpace(str):
    count = 0
    for i in str:
        if i==" ":
            count=count+1
    print("Number of Spaces is : ",count)


sentence=input("Enter sentece to count space : ")
countSpace(sentence)