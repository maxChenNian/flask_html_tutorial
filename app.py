from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
#     return render_template('a007_vue_tutorial.html')
    return render_template('a007_vue_tutorial.html')
