in git bash
$export FLASK_APP=app.py (or run.py changed later)
$export FLASK_ENV=development (change to production mode when ready to deploy)
$flask run
$flask --debug run

#============================================#
1. Create App dir and populate with __init__.py and views.py
2. Create entry point for app to run (from app import app)


#============================================#
1. Render the html template when someone comes to domain
2. from flask import redner_template
#============================================#
1. Create static dir next to template dir
2. fill with static stuff like css,js,images
#============================================#
1. Create base template and fill with child templates