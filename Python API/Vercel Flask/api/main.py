from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Vercel Flask"

@app.route("/about")
def about():
    return "Hello from About"