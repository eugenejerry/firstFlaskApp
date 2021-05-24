from flask import Flask, app
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<b>WELCOME</b>"

@app.route("/about")
def aboutus():
    return "<h1>THIS IS ABOUT US</h1>"

@app.route("/products")
def products():
    return "<h2>WE GOT THE FOLLOWING PRODUCTS</h2>"

@app.route("/services")
def services():
    return "<h2> OUR SERVICES INCLUDES THE FOLLOWING </h2>"

@app.route("/contact")
def  contact():
    return "<b> Contact Us on the following numbers</b>"
