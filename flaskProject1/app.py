from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return 'render_template('home.html')

@app.route('/menu')
def render_menu_page():
    return render_template('menu_html')

