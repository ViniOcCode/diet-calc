from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired

ALLOWED_ACTIVITIES = [(1.2, "Sedentário"), (1.375, "Levemente ativo"),
                      (1.55, "Moderadamente ativo"), (1.725, "Altamente ativo"),
                      (1.9, "Extremamente ativo")]

ALLOWED_GOALS = [("maintenance", "Manter peso"), ("cutting", "Perder peso"), ("bulking", "Ganhar peso")]

class PersonForm(FlaskForm):
    gender = RadioField("Sexo", choices=[('m', "Homem"), ('f', "Mulher")], validators=[DataRequired()])
    weight = IntegerField("Peso (kg)", validators=[DataRequired()])
    height = IntegerField("Altura (cm)", validators=[DataRequired()])
    age = IntegerField("Idade", validators=[DataRequired()])
    activity = SelectField("Nível de Atividade", choices=ALLOWED_ACTIVITIES, coerce=float, validators=[DataRequired()])
    goal = SelectField("Objetivo", choices=ALLOWED_GOALS, validators=[DataRequired()])
    submit = SubmitField("Calcular")

