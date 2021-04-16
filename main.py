from flask import Flask
import retirement
import bmi


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"
