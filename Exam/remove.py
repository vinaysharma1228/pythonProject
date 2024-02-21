string1 = input("Enter your string : ")

def remv(string):
    string = string.replace("@"," ")
    string = string.replace("!"," ")
    string = string.replace("/"," ")
    string = string.replace(" ","")
    print(string)

remv(string1)
