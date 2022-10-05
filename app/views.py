#Contains all views/routes
from doctest import script_from_examples
from app import app
from app.data_scripting.setup import get_employees_azure, get_user_info
from flask import render_template, request, redirect
from datetime import datetime

#Decorator route/view
#===================================================================#
@app.route("/")
def index():

    users = get_employees_azure()

    return render_template("public/index.html", users=users)
#===================================================================#
@app.route("/about")
def about():
    return render_template("public/about.html")

#===================================================================#
@app.route("/userlist")
def userlist():
    return render_template("public/userlist.html")

#===================================================================#
@app.route("/jinja")
def jinja():

    my_name = "Max Chalitsios"

    age = 22

    langs = ["Python", "JavaScript", "Bash", "C++", "R"]

    friends = {
        "Tom" : 30,
        "Bob" : 20,
        "Jax" : 60,
        "Mel" : 19,
    }

    colors = ("Red", "Green", "Blue")

    swagging = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pulling repo {self.name}"
        
        def clone(self):
            return f"Cloning into {self.url}"
    
    myRemote = GitRemote(
        name="Flask Jinja",
        description="Template Design tutorial",
        url="https://github.com/fygure.git"
    )
        

    my_html = "<h1>THIS IS SOME HTML</h1>"
    suspicious= "<script>alert('YOU GOT HACKED')</script>"
    
    def repeat(x, n):
        return x * n

    date = datetime.utcnow()

    return render_template("public/jinja.html", my_name=my_name, age=age, langs=langs,
    friends=friends, colors=colors, swagging=swagging, 
    myRemote=myRemote, repeat=repeat, date=date, my_html=my_html, suspicious=suspicious
    )
#===================================================================#
@app.route("/createuser", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        username = req["username"]
        password = req.get("password")

        print(username, password)

        return redirect(request.url)





    return render_template("public/createuser.html")
#===================================================================#
# DUMMY DATA
users = {
    "max": {
        "name": "Max",
        "bio": "pro fps gamer"
    },
    "brad": {
        "name": "Brad",
        "bio": "decent fps gamer"
    },
    "cris": {
        "name": "Cris",
        "bio": "nooby fps gamer"
    }
}
#===================================================================#
@app.route("/profile/<userid>")
def profile(userid):

    user = get_user_info(userid)[0]
    print(user)



    return render_template("public/profile.html", user=user)
#===================================================================#

#===================================================================#

#===================================================================#

#===================================================================#