from app import app # app from app/__init__.py file

from flask import render_template, request, redirect, abort, json, jsonify, make_response

from datetime import datetime


@app.route("/")
@app.route("/index")
def index():
    print(f"Flask app is set to: {app.config['ENV']}")
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

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        
        """
        Various ways to get the html form data
        """

        req = request.form

        username = req["username"]
        email = req.get("email")
        
        password = request.form['password']

        print(username, email, password)

        # redirect to the same url 
        return redirect(request.url) 

    return render_template('public/signup.html')


@app.route("/profile/<username>")
def profile(username:str):
    try:
        with open("db.json", "r") as f:
            users = json.load(f)

    except FileNotFoundError:
        abort(404)
        print("File not found.")
    
    user = None
    if username in users:
        user = users[username]

    return render_template('public/profile.html', user=user, username=username)

@app.route("/multiple/<foo>/<bar>/<baz>")
def multiple(foo, bar, baz):
    return f"foo is {foo}, bar is {bar}, baz is {baz}"


# Javascript Fetch API example
@app.route("/guestbook")
def guestbook():
    return render_template('public/guestbook.html')

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()
    
    print(req)
    
    res = make_response(jsonify(req), 200)

    return res

# Query String
@app.route("/query")
def query():

    if request.args:
        args = request.args

        #if "title" in args:
        #    title = args.get("title") # request.args.get("title")
    
    #print(title)
        serialized = ", ".join(f"{k}:{v}" for k, v in args.items())
        return f"(Query) {serialized}", 200
    #return "Query received", 200
    else:
        return "No query received", 200