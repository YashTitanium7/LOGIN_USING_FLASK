from flask import Flask, app, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///loginDatabase.db"
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def home():
  return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    password = hash(password)
    return render_template('testing.html', email=email, password=password)
  return render_template('login.html')

@app.route("/reg", methods=['POST', 'GET'])
def reg():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    password = hash(password)
    return render_template('testing.html', name=name, email=email, password=password)
  return render_template('register.html')

if __name__ == '__main__':
  app.run(debug=True, port="5500")
