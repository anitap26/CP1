import http.client

from flask import Flask

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        result = CALCULATOR.multiply(num_1, num_2)
        return ("{}".format(result), http.client.OK, HEADERS)
    
    except TypeError as e:
        # Si ocurre un error de tipo, devolver un error 400 (Bad Request)
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        result = num_1 / num_2  # Esto lanzará un ZeroDivisionError si el divisor es cero
        return ("{}".format(result), http.client.OK, HEADERS)
    
    except ZeroDivisionError:
        # Si el divisor es cero, devolver un error 406 (Not Acceptable)
        return ("Cannot divide by zero", http.client.NOT_ACCEPTABLE, HEADERS)
    
    except ValueError as e:
        # Si ocurre un error de valor, devolver un error 400 (Bad Request)
        return (str(e), http.client.BAD_REQUEST, HEADERS)
    
    except TypeError as e:
        # Si ocurre un error de tipo, devolver un error 400 (Bad Request)
        return (str(e), http.client.BAD_REQUEST, HEADERS)
    
    except Exception as e:
        # Captura cualquier otro error inesperado y devuelve un error 500 (Internal Server Error)
        return (f"Internal server error: {str(e)}", http.client.INTERNAL_SERVER_ERROR, HEADERS)
