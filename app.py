from flask import Flask, app, request, redirect, flash
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///loginDatabase.db"
db = SQLAlchemy(app)

class Register(db.Model):
  sno = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(200), nullable=False)
  password = db.Column(db.String(200), nullable=False)

  def __repr__(self) -> str:
    return f"{self.sno} - {self.name}"

@app.route('/', methods=['GET', 'POST'])
def home():
  return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password').encode("utf-8")
    try:
      ac = Register.query.filter_by(email=email).first()
      print(type(ac))
      name = ac.name
      saved_password = ac.password
      if bcrypt.checkpw(password, saved_password):
        return render_template('loggedin.html', name=name)
      else:
        return "<h1>OOPS!!....Heads up!....</br>WRONG CREDINTIALS.</h1>"
    except:
      pass
  else:
    return render_template('login.html')

@app.route("/reg", methods=['POST', 'GET'])
def reg():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password').encode("utf-8")
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    ACs = Register(name=name, email=email, password=hashed_password)
    db.session.add(ACs)
    db.session.commit()
    return render_template('registered.html', name=name, email=email, password=hashed_password)
  return render_template('register.html')

if __name__ == '__main__':
  app.run(debug=True, port="5500")
