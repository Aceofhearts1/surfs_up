from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

#def math_multiply():
#    number_1 = int(input("Type a number"))
#    number_2 = int(input("Type a number"))
#    number_3 = number_1 * number_2
#    return number_3

