from flash import flask

app = flask(__name__)

@app.route("/")
def helloworld():
    return "<p>Hello World</p>"