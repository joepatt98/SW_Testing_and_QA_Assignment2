import math

def Height():

    print("\nEnter your height in feet and inches below: ")
    feet = int(input("\nFeet: "))
    inches = int(input("\nInches: "))
    total_inches = (feet * 12) + inches

    meters = total_inches * 0.025

    return meters

def Weight():

    print("\nEnter your weight in pounds below: ")
    pounds = float(input("\nPounds: "))

    kilograms = pounds * 0.45

    return kilograms

def Calculate_BMI(meters, kilograms):

    squared_meters = pow(meters, 2)
    BMI = math.ceil(kilograms / squared_meters)

    if (BMI < 18.5):
        category = "Underweight"

    elif (BMI >= 18.5 and BMI < 25):
        category = "Normal weight"

    elif (BMI >= 25 and BMI < 30):
        category = "Overweight"

    elif (BMI >= 30):
        category = "Obese"

    print("\nBMI: ", BMI, "\nCategory: ", category)

    return

def BMI():

    Calculate_BMI(Height(), Weight())

    return
