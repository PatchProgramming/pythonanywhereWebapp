
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ("""<h1>Hello from Flask!</h1>
    <p> <a href="http://patchprogramming.pythonanywhere.com/test" click here to go to the next page</a></p>""")

@app.route('/test')
def secondFunc():
    return("<h1> testing new endpoint!</h1>")