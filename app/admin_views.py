from app import app # app from app/__init__.py file

from flask import render_template

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template('admin/dashboard.html')


@app.route("/admin/profile")
def admin_profile():
    return render_template('admin/profile.html')