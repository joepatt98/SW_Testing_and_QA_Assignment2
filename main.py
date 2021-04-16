from flask import Flask, request
import retirement
import bmi

def list_functions():

    print("\n*****  Please type a function name as it is listed below.  *****")
    print("\nBMI\nRetirement\nExit\n")
    #check_input()

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

#list_functions()

app = Flask(__name__)
homepage = "<a href=\"/\">Go back Home</a>"
@app.route('/')
def index():
    return HTML

HTML = """
    <html><body>
        <a href="/bmi">BMI</a>
        <a href="/retirement">Retirement</a>
    </body></html>  """


@app.route('/bmi', methods=['GET', 'POST'])
def route_bmi():
    if request.method == 'POST':

        feet = int(request.form['feet'])
        inches = int(request.form['inches'])
        pounds = int(request.form['pounds'])
        BMI, category = bmi.BMI(feet, inches, pounds)

        return "<html><body>" + str(BMI) + "<br><br>" + str(category) + "<br><br><br><br>" + homepage + "</body></html>"

    return HTML2

HTML2 = """
    <html>
        <body>
            <a href="/bmi">BMI</a>
            <a href="/retirement">Retirement</a>
        </body>
        <br><br><br><br>
        Enter your body height and weight below:
        <br><br>
        <form action="/bmi" method="post">
            <label for="feet">Feet:</label><br>
            <input type="text" id="feet" name="feet" value=""><br>
            <label for="inches">Inches:</label><br>
            <input type="text" id="inches" name="inches" value=""><br><br>
            <label for="pounds">Pounds:</label><br>
            <input type="text" id="pounds" name="pounds" value=""><br><br>
            <input type="submit" value="Submit">
        </form>
    </html>"""

@app.route('/retirement', methods=['GET', 'POST'])
def route_retirement():
    if request.method == 'POST':

        age = int(request.form['age'])
        salary = float(request.form['salary'])
        percent_saved = float(request.form['percent_saved'])
        savings_goal = float(request.form['savings_goal'])
        print_out = retirement.Retirement(age, salary, percent_saved, savings_goal)

        return "<html><body>" + str(print_out) + "<br><br><br><br>" + homepage + "</body></html>"

    return HTML3

HTML3 = """
    <html>
        <body>
            <a href="/bmi">BMI</a>
            <a href="/retirement">Retirement</a>
        </body>
        <br><br><br><br>
        Enter your retirement details below:
        <br><br>
        <form action="/retirement" method="post">
            <label for="age">Age (in years):</label><br>
            <input type="text" id="age" name="age" value=""><br>
            <label for="salary">Salary (no commas):</label><br>
            <input type="text" id="salary" name="salary" value=""><br><br>
            <label for="percent_saved">Percentage of salary saved (decimal form):</label><br>
            <input type="text" id="percent_saved" name="percent_saved" value=""><br><br>
            <label for="savings_goal">Savings Goal (no commas):</label><br>
            <input type="text" id="savings_goal" name="savings_goal" value=""><br><br>
            <input type="submit" value="Submit">
        </form>
    </html>"""
