from app import app

from flask import render_template, request

@app.errorhandler(404)
def not_found(e):
    return render_template("public/error_templates/404.html")

@app.errorhandler(403)
def not_found(e):
    #LOGGING THE ERROR
    app.logger.error(f"Forbidden access: {e}, route: {request.url}")
    return render_template("public/error_templates/403.html")

@app.errorhandler(500)
def server_error(e):
    #LOGGING THE ERROR
    app.logger.error(f"Server error {e}, route: {request.url}")

    # TODO's
    # CREATE A CUSTOM FUNCTION TO SEND AN EMAIL TO NOTIFY THE ADMIN OF THIS ERROR
    #email_admin(message="Server error", error=e, url=request.url)

    return render_template("public/error_templates/500.html")

