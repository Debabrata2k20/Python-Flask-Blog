from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about")
def papun():
    name = "papun"
    return render_template('about.html', name=name)


app.run(debug=True)