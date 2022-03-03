from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "C:/Users/18388/OneDrive - Wellington College/13DTS/Smile/smile.db"

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/menu')
def render_menu_page():
    con = create_connection(DATABASE)

    query = "SELECT name, description, volume, price, image FROM product"
    cur = con.cursor()
    cur.execute(query)
    product_list = cur.fetchall()

    #product_list = [["Flat white", "Minimal foam on a coffee", "250ml", 4.00],
         #            ["Espresso", "A double shot of coffee", "80ml", 3.00, "espresso"]]
    return render_template('menu.html', products=product_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')

@app.route('/login')
def render_contact_page():
    return render_template('login.html')

@app.route('/signup')
def render_contact_page():
    return render_template('signup.html')

app.run(host='0.0.0.0', debug=True)
