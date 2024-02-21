def check_number_type(number):
    if isinstance(number, int):
        return "Integer"
    elif isinstance(number, float):
        return "Float"
    else:
        return "Not a valid number"


result = check_number_type(5)
print(result)


