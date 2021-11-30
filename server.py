from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index.html")
def my_home():
    return render_template('./index.html')


@app.route("/works.html")
def works():
    return render_template('./works.html')


@app.route("/about.html")
def about():
    return render_template('./about.html')


@app.route("/contact.html")
def contact():
    return render_template('./contact.html')


@app.route("/components.html")
def components():
    return render_template('./components.html')
