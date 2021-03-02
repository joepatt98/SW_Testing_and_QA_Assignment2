

def list_functions():

    print("\nPlease type a function name as it is listed below.")
    print("\nBMI\nRetirement\nExit\n")
    check_input()

def check_input():

    function = input("Chosen Function: ")

    if (function == "BMI"):

        print("BMI()")
        list_functions()

    elif (function == "Retirement"):

        print("Retirement()")
        list_functions()

    elif (function == "Exit"):
        print("\n")
        return

    else:

        print("\nA valid input was not detected. Try again.")
        list_functions()

list_functions()
