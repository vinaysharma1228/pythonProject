str="Kasturbadam-360020"

alpha=0
digit=0

for i in str:
    if(i.isalpha()):
        alpha=alpha+1
    
    elif i.isdigit():
        digit=digit+1


print("Alpha number : ",alpha)
print("digit number : ",digit)