from flash import flask

app = flask(__name__)

@app.route("/")
def helloworld():
    return "<p>Hello World</p>"
@app.route("/test")
def helloworld():
    return "<p>Testing new route</p>"