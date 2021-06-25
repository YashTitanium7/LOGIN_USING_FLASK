from flask import Flask, app
from flask.templating import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, port="5500")
