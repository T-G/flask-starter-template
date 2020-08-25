"""
Custom filter to be used in Jinja Template files
"""

from app import app

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")