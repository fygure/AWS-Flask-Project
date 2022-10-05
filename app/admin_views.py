#Contains all views/routes
from app import app

from flask import render_template
#Decorator route/view
@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route("/admin/profile")
def admin_profile():
    return render_template("admin/profile.html")