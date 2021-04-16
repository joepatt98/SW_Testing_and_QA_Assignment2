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

@app.route('/')
def index():
    return HTML

HTML = """
     <html><body>
         <a href="/bmi">BMI</a>
         <a href="/retirement">Retirement</a>
     </body></html>"""


@app.route('/bmi', methods=['GET', 'POST'])
def route_bmi():
    if request.method == 'POST':

        feet = int(request.form['feet'])
        inches = int(request.form['inches'])
        pounds = int(request.form['pounds'])
        BMI, category = bmi.BMI(feet, inches, pounds)

        return "<html><body>" + str(BMI) + "<br><br>" + str(category) + "</body></html>"

    return HTML2

HTML2 = """
    <form action="/bmi" method="post">
      <label for="feet">Feet:</label><br>
      <input type="text" id="feet" name="feet" value=""><br>
      <label for="inches">Inches:</label><br>
      <input type="text" id="inches" name="inches" value=""><br><br>
      <label for="pounds">Pounds:</label><br>
      <input type="text" id="pounds" name="pounds" value=""><br><br>
      <input type="submit" value="Submit">
    </form> """
