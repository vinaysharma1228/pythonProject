
def calculate_bill(units):
    if units<=100:
        return units*4
    elif units<=150:
        return (100*4)+((units-100)*5)
    elif units<=200:
        return (100*4)+(50*5)+((units-150)*6)
    elif units<=300:
        return (100*4)+(50*5)+(50*6)+((units-200)*8)
    elif units>300:
        return (100*4)+(50*5)+(50*6)+(100*8)+((units-300)*10)
    else:
        return 0


units=350
print("The electricity bill is : ",calculate_bill(units))



