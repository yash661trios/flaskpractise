from flask import Flask
from flask.templating import render_template
from flask import request

app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/solve', methods=["POST"])
def calculation():
    num = int(request.form['val'])
    cal = num ** 2
    return render_template('index.html',submit = cal)

if __name__ == '__main__':
    app.run()   