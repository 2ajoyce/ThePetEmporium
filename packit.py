from flask import Flask, url_for
app = Flask(__name__)

def from_py(hello):
  def wrapper(*args, **kwargs):
    return hello(*args, **kwargs) + " From Python!"
  return wrapper

@app.route('/login')
def login():
    return "You Logged In!"
    
@app.route("/")
@from_py
def hello():
    return "Hello World! " + "<a href=" + url_for('login') + "> Login </a><br>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')