from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

class Calculator(FlaskForm):
    arg1 = IntegerField('Addend 1', validators=[DataRequired()])
    arg2 = IntegerField('Addend 2', validators=[DataRequired()])
    op_name = SelectField('Operation', choices = [('add', 'Add'),('sub', 'Subtract'),('mul', 'Multiply'),('div','Divide')])
    submit = SubmitField('Calculate')