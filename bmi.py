

def Height_Input():

    print("\nEnter your height in feet and inches below: ")
    feet = int(input("\nFeet: "))
    inches = int(input("\nInches: "))

    return feet, inches

def Height(feet, inches):

    total_inches = (feet * 12) + inches

    meters = total_inches * 0.025

    return meters

def Weight_Input():

    print("\nEnter your weight in pounds below: ")
    pounds = float(input("\nPounds: "))

    return pounds

def Weight(pounds):

    kilograms = pounds * 0.45

    return kilograms

def Calculate_BMI(meters, kilograms):

    squared_meters = pow(meters, 2)
    BMI = int(kilograms / squared_meters)

    return BMI

def Calculate_Category(BMI):

    if (BMI < 18.5):
        category = "Underweight"

    elif (BMI >= 18.5 and BMI < 25):
        category = "Normal weight"

    elif (BMI >= 25 and BMI < 30):
        category = "Overweight"

    elif (BMI >= 30):
        category = "Obese"

    return category

def BMI(feet, inches, pounds):

    #feet, inches = Height_Input()
    meters = Height(feet, inches)
    #pounds = Weight_Input()
    kilograms = Weight(pounds)
    BMI = Calculate_BMI(meters, kilograms)
    category = Calculate_Category(BMI)
    #print("\nBMI: ", BMI, "\nCategory: ", category)

    return BMI, category
