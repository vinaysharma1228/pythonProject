password = input("Enter password : ")

hasLength = False
hasUcase = False
hasLcase = False
hasDigit = False
hasSpChar = False

if 8 <= len(password) <= 15:
    hasLength = True

    for i in password:
        if i.isupper():
            hasUcase = True
        elif i.islower():
            hasLcase = True
        elif i.isdigit():
            hasDigit = True
        elif i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*':
            hasSpChar = True
else:
    print("Password length must be greater or equal to 8 and less or equal to 15 characters.")
if hasLength and hasUcase and hasLcase and hasDigit and hasSpChar:
    print("Valid Password")
else:
    print("Invalid Password")
