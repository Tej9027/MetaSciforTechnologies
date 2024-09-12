from flask import Flask,render_template,request,redirect,url_for

app= Flask(__name__)


@app.route("/")

def home():
    return render_template('tej.html',username="Tej",Hobbies="Watching Movies, Travelling")

app.run(debug=True)