from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/menu')
def render_menu_page():
    producet_list = [["Flat white", "Minimal foam on a coffee", "250ml", 4.00],
                     ["Espresso", "A duble shot of coffee", "80ml", 3.00, "espresso"]]
    return render_template('menu.html')


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)
