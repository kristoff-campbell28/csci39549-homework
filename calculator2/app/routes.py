from app import app
from app.forms import Calculator
from flask import render_template, flash, redirect

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Calculator()
    if form.validate_on_submit():
        flash(calculator(form.op_name.data, form.arg1.data, form.arg2.data))
        return redirect('/index')
    return render_template('index.html', title='Calculator', form=form)

def calculator(op_name, arg1, arg2):
	if op_name == 'add':
		return "Result: " + str(arg1) + " + " + str(arg2) + " = "  + str(arg1 + arg2)
	elif op_name == 'sub':
		return "Result: " + str(arg1) + " - " + str(arg2) + " = "  + str(arg1 - arg2)
	elif op_name == 'mul':
		return "Result: " + str(arg1) + " * " + str(arg2) + " = "  + str(arg1 * arg2)	
	elif op_name == 'div':
		return "Result: " + str(arg1) + " / " + str(arg2) + " = "  + str(arg1 / arg2)


