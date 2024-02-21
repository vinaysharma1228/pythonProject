import math


def compoundInterest(amount, time, rate):
    ci = amount * math.pow(1 + (rate / 100), time)
    print("Compound Interest: ", ci)


amount = float(input("Enter Amount: "))
time = float(input("Enter time: "))
rate = float(input("Enter rate: "))

compoundInterest(amount, time, rate)
