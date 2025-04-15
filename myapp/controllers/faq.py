from flask import request, render_template, Blueprint
from myapp.templates import *

faq = Blueprint("faq", __name__)

@faq.route('/faq')
def render_faq():
    return render_template("faq.html")