from flask import request, render_template, Blueprint
from myapp.models.calculator import Person
from myapp.templates import *

calc_control = Blueprint("calc_control", __name__)

@calc_control.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
    goal = None
    data =  request.form

    if request.method == 'POST':
        try:
            person = Person(
                weight=float(data["weight"]),
                height=float(data["height"]),
                age=int(data["age"]),
                gender=data["gender"],
                activity=float(data["activity"]),
                goal=str(data["goal"])
            )
        except ValueError as e:
            return render_template("index.html", error=str(e), result=result, data=data)
        else:
            goal = str(data["goal"]) 
       
        result = person.summary()

    return render_template("index.html", goal=goal, result=result, data=data)