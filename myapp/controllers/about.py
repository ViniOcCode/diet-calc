from flask import request, render_template, Blueprint
from myapp.templates import *

about = Blueprint("about", __name__)

@about.route('/about')
def render_about():
    return render_template("about.html")