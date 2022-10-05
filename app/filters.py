from app import app

from flask import render_template

from datetime import datetime

#Register custom template filter on our app
@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")
