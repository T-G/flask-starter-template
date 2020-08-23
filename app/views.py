from app import app # app from app/__init__.py file

from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template('public/index.html')


@app.route("/about")
def about():
    return render_template('public/about.html')