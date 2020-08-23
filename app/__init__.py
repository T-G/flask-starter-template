from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# import the controllers a.k.a views in Python 
from app import views
from app import admin_views