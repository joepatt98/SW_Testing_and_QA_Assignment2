

def Output(age_when_goal_met):

    if (age_when_goal_met >= 100):

        print("\nDeath will occur before goal is met at " + str(age_when_goal_met) + " years old.\n")

    else:

        print("\nGoal will be met at " + str(age_when_goal_met) + " years old.\n")

    return

def Calculate_Retirement(age, salary, percent_saved, savings_goal):

    savings_per_year = salary * percent_saved * 1.35
    years_til_goal = savings_goal // savings_per_year
    age_when_goal_met = int(age + years_til_goal)

    Output(age_when_goal_met)

def Input():

    print("\nEnter your retirement details below: \n")
    age = int(input("Age (in years): "))
    salary = float(input("Salary (no commas): "))
    percent_saved = float(input("Percentage of salary saved (decimal form): "))
    savings_goal = float(input("Savings Goal (no commas): "))

    Calculate_Retirement(age, salary, percent_saved, savings_goal)

def Retirement():

    Input()

    return
