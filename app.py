from flask import Flask

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



if __name__=="__main__":
  app.run(debug=True)
