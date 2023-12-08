
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ("""<h1>Hello from Flask!</h1>
    <p> <a href="http://patchprogramming.pythonanywhere.com/test"> click here to go to the next page</a></p>
            <h3><a href="https://patchprogramming.pythonanywhere.com/tammy"> Tammy click here</a></h3>""")

@app.route('/test')
def secondFunc():
    return("""<h1> testing new endpoint!</h1>
           <a href="https://patchprogramming.pythonanywhere.com/">Click here to go home</a>""")

@app.route('/tammy')#this is to show off to my wife
def flexingOnWife():
    return("""<h1>Hello my wonderful wife. I love you!!!</h1>
            <a href=https://patchprogramming.pythonanywhere.com/>Click here to go home</a>""")