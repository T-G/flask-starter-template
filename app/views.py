from app import app # app from app/__init__.py file

from flask import render_template, request, redirect, abort, json, jsonify, make_response

from datetime import datetime

import os

from werkzeug.utils import secure_filename


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

"""
function allowed_image(filename:str) will check for validation in the filename
and return bool True of False
"""
def allowed_image(filename:str):
    
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

@app.route("/upload-image", methods=["GET","POST"])
def upload_image():

    if request.method == "POST":
        if request.files:
            
            #print(request.cookies)
            if not allowed_image_filesize(request.cookies.get("filesize")):
                print("File exceeded maximum file size")
                return redirect(request.url)

            image = request.files["image"]

            # Check for filename validation
            if image.filename == "":
                print("Image must have a file name")
            
            if not allowed_image(image.filename):
                print("The uploaded image extension is not allowed")
                return redirect(request.url)
            else:
                # If the filename is of melicious nature, change the file name 
                # before uploading to the server
                filename = secure_filename(image.filename)
            
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
            
            print("Image saved..")
            
            return redirect(request.url)

    return render_template("public/upload_image.html")