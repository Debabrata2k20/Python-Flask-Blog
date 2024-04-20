from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy




local_server = True
app =Flask(__name__,template_folder="templates")

db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)
 

@app.route("/")
def home7():
    return render_template('index.html')


@app.route("/home.html")
def home():
    return render_template('index.html')

@app.route("/index.html")
def home1():
    return render_template('index.html')


@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/contact.html", methods = ['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num=phone, msg=message, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')


app.run(debug=True)
