from flask import Flask,render_template,url_for

app= Flask(__name__)



@app.route("/home")
def home():
    return render_template("home.html",title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="ABOUT")

@app.route("/contact")
def contact():
    return render_template("contact.html" ,title="CONTACT")

@app.route("/project")
def project():
    return render_template("project.html", title="PROJECT")


if __name__=="__main__":
    app.run(debug=True)