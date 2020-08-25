from app import app # app from app/__init__.py file

from flask import render_template

from datetime import datetime


@app.route("/")
@app.route("/index")
def index():
    return render_template('public/index.html')


@app.route("/about")
def about():
    return render_template('public/about.html')


@app.route("/jinja")
def jinja():
    
    myname = 'Theo'

    age = 40
    
    langs = ['Python', 'JavaScript', 'Bash', 'C', 'Ruby']

    friends = {
        'Tom' : 30,
        'Amy' : 60,
        'Tony' : 56,
        'Clampad' : 23 
    }

    colors = ("Red", "Green")

    cool = True

    class GitRemote():
        def __init__(self, name:str, description:str, url:str):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pulling repo {self.name}"
        
        def clone(self):
            return f"Cloning into {self.url}"

    my_remote = GitRemote(
        name = "Flask Jinja",
        description = "Template design in Jinja",
        url = "https://github.com/t-g/jinja.git"
    )

    def repeat(x:str, qty:int):
        return x * qty
    
    date = datetime.utcnow()

    my_html = "<h1>Hi There</h1>"

    suspecious = "<script>alert('You got hacked!!!')</script>"

    return render_template('public/jinja.html', 
        myname = myname,
        age = age,
        langs = langs,
        colors = colors,
        cool = cool,
        friends = friends,
        GitRemote = GitRemote,
        repeat = repeat,
        my_remote = my_remote,
        date = date,
        my_html = my_html,
        suspecious = suspecious

    )
