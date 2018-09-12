from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Instructions: after the domain, type the name of the operation, with two arguments separated  by backslashes. e.g. add/1/2, subtract3/4</br>Valid operation names: add, subtract, multiply, divide"

@app.route('/<string:op_name>/<int:arg1>/<int:arg2>')
def calculator(op_name, arg1, arg2):
	if op_name == 'add':
		return "Result: " + str(arg1) + " + " + str(arg2) + " = "  + str(arg1 + arg2)
	elif op_name == 'subtract':
		return "Result: " + str(arg1) + " - " + str(arg2) + " = "  + str(arg1 - arg2)
	elif op_name == 'multiply':
		return "Result: " + str(arg1) + " * " + str(arg2) + " = "  + str(arg1 * arg2)	
	elif op_name == 'divide':
		return "Result: " + str(arg1) + " / " + str(arg2) + " = "  + str(arg1 / arg2)


