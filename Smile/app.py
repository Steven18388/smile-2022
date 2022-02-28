from flask import Flask, render_template

app = Flask(__name__)
DATABASE = "smile.db"

def create_connection(db_file):
    ###
    Create a connection with the database
    parameter:name of the database file
    returns: a connection to the file
    ###
    try:
        connection = sqlite3.connect(db_file)
        return connection
    excpet Error as e:
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

    producet_list = [["Flat white", "Minimal foam on a coffee", "250ml", 4.00],
                     ["Espresso", "A duble shot of coffee", "80ml", 3.00, "espresso"]]
    return render_template('menu.html')


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)
