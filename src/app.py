from flask import Flask, render_template, request
import requests
import webbrowser

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("map.html")

if __name__ == "__main__":
    webbrowser.open('http://localhost:5000/', new=2, autoraise=False)
    app.run(debug=True)
