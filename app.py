from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def home():
  return "home"


@app.route('/about')

def about():
  return "about"

@app.route('/ab')

def ab():
  return "don"

@app.route('/git')

def git():
  return render_template("/htm.html")


if __name__=="__main__":
  app.run(debug=True)
