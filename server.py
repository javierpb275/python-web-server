from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('./index.html')

@app.route("/about.html")
def about():
    return render_template('./about.html')

@app.route("/blog")
def blog():
    return "<p>My blog</p>"

@app.route("/blog/2021/dogs")
def blog2():
    return "<p>My dog</p>"