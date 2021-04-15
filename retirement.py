import math

def Input():

    print("\nEnter your retirement details below: \n")
    age = int(input("Age (in years): "))
    salary = float(input("Salary (no commas): "))
    percent_saved = float(input("Percentage of salary saved (decimal form): "))
    savings_goal = float(input("Savings Goal (no commas): "))
    #test comment
    return age, salary, percent_saved, savings_goal

def Calculate_Retirement(age, salary, percent_saved, savings_goal):

    savings_per_year = salary * percent_saved * 1.35
    years_til_goal = math.ceil(savings_goal / savings_per_year)
    age_when_goal_met = int(age + years_til_goal)

    return age_when_goal_met

def Output(age_when_goal_met):

    if (age_when_goal_met >= 100):

        result = "\nDeath will occur before goal is met at "

    else:

        result = "\nGoal will be met at "

    return result

def Retirement():

    age, salary, percent_saved, savings_goal = Input()
    age_when_goal_met = Calculate_Retirement(age, salary, percent_saved, savings_goal)
    result = Output(age_when_goal_met)
    print(result + age_when_goal_met + " years old.\n")

    return
