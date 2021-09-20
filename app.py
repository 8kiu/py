from flask import Flask
import string
from random import *

app = Flask(__name__)
characters = string.ascii_letters + string.digits
password =  "".join(choice(characters) for x in range(randint(9, 9)))
characters =  string.digits
n1 =  "".join(choice(characters) for x in range(randint(9, 9)))
while True:
    @app.route('/')
    def hello():
        return password
        return n1
    if   __name__ == "__main__":
        app.run()

    
href="{{ url_for('static', filename='py.css')}}"
@app.route('5')
def py():
    return password