from flask import Flask,render_template
app=Flask(__name__,template_folder="templates")
@app.route("/")
@app.route("/Home")
def hello():
    return render_template("base.html",title="Home",active="active")
@app.route("/contact")    
def contact():
   return render_template("contact.html",title="Contact",active="active")
@app.route("/about" ,methods=["GET","POST"]) 
def about():
    return render_template("about.html")  
@app.route("/courses")
def courses():
    return None
@app.route("/events")   
def events():
    return render_template("events.html") 
@app.route("/register")
def register():
    return render_template("register.html")    
