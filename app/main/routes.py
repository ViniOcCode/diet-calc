from flask import request, render_template, Blueprint
from app.templates import *
from app.calculator import Person, ValidationError
from app.main import bp
from .forms import PersonForm


@bp.route('/', methods=['GET', 'POST'])
def calculate():
    form = PersonForm()
    result = None

    if form.validate_on_submit():
        try:
            person = Person(
                weight=form.weight.data,
                height=form.height.data,
                age=form.age.data,
                gender=form.gender.data,
                activity=form.activity.data,
                goal=form.goal.data
            )
            result = person.summary()
        except ValidationError as e:
            form.errors["validation"] = [str(e)]

    return render_template("index.html", form=form, result=result)


@bp.route('/about')
def render_about():
    return render_template("about.html")


@bp.route('/faq')
def render_faq():
    return render_template("faq.html")
