from flask import request, render_template, Blueprint
from myapp.models.calculator import Person
from myapp.templates import *

calc_control = Blueprint("calc_control", __name__)

@calc_control.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
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
            return str(e), 400
        else:
            print(data["age"])
            print(data["gender"])
            print(data["activity"])
            print(data["goal"])
        result = person.summary()

    return render_template("index.html", result=result)