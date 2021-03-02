

def Retirement():

    print("\nEnter your retirement details below: \n")
    age = int(input("Age (in years): "))
    salary = float(input("Salary (no commas): "))
    percent_saved = float(input("Percentage of salary saved (decimal form): "))
    savings_goal = float(input("Savings Goal (no commas): "))

    savings_per_year = salary * percent_saved * 1.35
    years_til_goal = savings_goal // savings_per_year
    age_when_goal_met = int(age + years_til_goal)

    if (age_when_goal_met >= 100):

        print("\nDeath will occur before goal is met at " + str(age_when_goal_met) + " years old.\n")

    else:

        print("\nGoal will be met at " + str(age_when_goal_met) + " years old.\n")

    return
    
