import retirement
import bmi

def list_functions():

    print("\n*****  Please type a function name as it is listed below.  *****")
    print("\n              BMI\n           Retirement\n              Exit\n")
    check_input()

def check_input():

    function = input("Chosen Function: ")

    if (function == "BMI"):

        bmi.BMI()
        list_functions()

    elif (function == "Retirement"):

        retirement.Retirement()
        list_functions()

    elif (function == "Exit"):
        print("\n")
        return

    else:

        print("\nA valid input was not detected. Try again.")
        list_functions()

list_functions()
