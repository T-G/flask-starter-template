from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

# import the controllers a.k.a views in Python 
from app import views
from app import admin_views
from .filters import clean_date
from app import error_handlers
