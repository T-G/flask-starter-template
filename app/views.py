from app import app # app from app/__init__.py file

from flask import render_template, request, redirect, abort, json, jsonify, make_response

from datetime import datetime



@app.route("/")
@app.route("/index")
def index():
    print(f"Flask app is set to: {app.config['ENV']}")
    abort(403)
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
import os

from werkzeug.utils import secure_filename

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


"""
Types/converters

string: #by default
int:
float:
path:
uuid:

Allow client to download files from server directory
"""
from flask import send_from_directory

# Download images file
@app.route("/get-image/<string:filename>")
def get_image(filename:str):
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename=filename, as_attachment=True)
    
    except FileNotFoundError:
        abort(404)

# Download .csv file
@app.route("/get-csv/<string:filename>")
def get_csv(filename:str):
    try:
        return send_from_directory(app.config["CLIENT_CSV"], filename=filename, as_attachment=True)
    
    except FileNotFoundError:
        abort(404)

# Download .pdf file
@app.route("/get-pdf/<string:filename>")
def get_pdf(filename:str):
    try:
        return send_from_directory(app.config["CLIENT_PDF"], filename=filename, as_attachment=True)
    
    except FileNotFoundError:
        abort(404)

# Download .xls file
@app.route("/get-report/<path:path>")
def get_report(path):
    try:
        return send_from_directory(app.config["CLIENT_REPORTS"], filename=path, as_attachment=True)
    
    except FileNotFoundError:
        abort(404)

"""
Setting Cookies
Modules: response and make_response
make_response() allows us to add or modify the response before
sending the response to the browser

"""
@app.route("/cookies")
def cookies():
    # Create a response object
    res = make_response("Cookies", 200)

    #Get the cookies
    cookies = request.cookies

    flavour = cookies.get("flavour")
    chocolateType = cookies.get("chocolateType")
    chewy = cookies.get("chewy")

    print(f"flavour: {flavour}")
    print(f"chocolate type: {chocolateType}")
    print(f"chewy: {chewy}")


    #Setting Cookies
    res.set_cookie(
        "flavour",
        value="chocolate chip",
        max_age=10, # 10 sec
        expires=None,
        path=request.url,
        domain=None,
        secure=False,
        httponly=False,
        samesite=None
    )

    res.set_cookie("chocolateType", "dark")
    res.set_cookie("chewy", "yes")

    return res

"""
Working with Flask Session object
requires SECRET_KEY token 
Here is the steps to create one from python shell

import secrets
secrets.token_urlsafe(16)

Important note: Do not store sensetive information in session, use redis or database to store 
them.

"""
from flask import session, url_for

@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():

    if request.method == "POST":
        
        req = request.form
        
        username = req.get("username")
        password = req.get("password")

        with open("db.json", "r") as f:
            users = json.load(f)
            
            print(users)
            
            if not username in users:
                return redirect(request.url)
            else:
                user = users[username]   

            if not password == user["password"]:
                print("Password incorrect!")
                return redirect(request.url)
            else:
                session["USERNAME"] = user["username"]
                print("User added to session")
                return redirect(url_for("profile", username=session["USERNAME"]))

    return render_template("public/signin.html")


@app.route("/sign-out")
def sign_out():
    session.pop("USERNAME", None)
    return redirect(url_for("sign_in"))

"""
MESSAGE FLASHING
Required Module: request, redirect and flash

"""
from flask import flash

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        
        """
        Various ways to get the html form data
        """

        req = request.form

        #username = req["username"]
        #password = request.form['password']

        username = req.get("username")
        email = req.get("email")
        password = req.get('password')

        if username == "" and len(username) < 3:
            flash("Username cannot be empty or less than 3 characters", "warning")
            return redirect(request.url)

        elif email == "":
            flash("Please provide a valid Email", "warning")
            return redirect(request.url, email)

        elif not len(password) >= 10:
            flash("Password must be at least 10 characters in length", "warning")
            return redirect(request.url)
        else:
            flash("Account Created", "success") 
            return redirect(request.url) 

    return render_template('public/signup.html')

