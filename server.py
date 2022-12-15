"""Server for easy money"""

from flask import Flask, render_template, request, jsonify, session, redirect, flash
from model import Transaction, Budget, Category, User, connect_to_db, db
from flask_sqlalchemy import SQLAlchemy
from seed_database import generate_access_token, get_api_data
from crud import get_user_by_id, get_user_by_email, update_access_token, create_user,add_transactions,get_all_user_transactions

app = Flask(__name__)
app.secret_key = 'big secret'

BANK_ID = {'First Platypus Bank': "ins_109508",
            'First Gingham Credit Union': "ins_109509",
            'Tattersall Federal Credit Union': "ins_109510",
            'Tartan Bank': "ins_109511",
            'Houndstooth Bank': "ins_109512",
            'Tartan-Dominion Bank of Canada': "ins_43"}

@app.route("/")
def welcome():
    """Displays the Welcome page"""
    return render_template("welcome.html")

@app.route("/signup")
def signup():
    """Displays the Sign Up page"""
    return render_template("signup.html")  

@app.route("/do-signup", methods=['POST'])
def do_signup():
    """Create User in database from the signup form"""
    # TODO check if email exists
    user = create_user(fname=request.form['first_name'],
                lname=request.form['last_name'],
                email=request.form['email'],
                password=request.form['password'])
    
    
    user = get_user_by_email(request.form['email']) # get the user object
    session['user_id'] = user.user_id  # add user id to session
   
    return render_template("create_account.html", bank_names=BANK_ID.keys())

@app.route("/create-account", methods=['POST'])
def create_account():

    return render_template("dashboard.html")

@app.route("/login")
def login():
    """Displayes the Login page"""
    return render_template("login.html")

@app.route("/do-login", methods=['POST'])
def do_login():
    """Log existing user into the application"""
    #TODO check if email is in database, if not, send them to signup
    user = get_user_by_email(request.form['email'])
    session['user_id'] = user.user_id

    return render_template("dashboard.html")


@app.route("/dashboard", methods=['POST'])
def dashboard():
    acc_tok = generate_access_token(BANK_ID[request.form['bankname']]) # generate the access token for the new user
    update_access_token(session['user_id'], acc_tok) # add token to User
    # get new transactions from api
    response_data = get_api_data(acc_tok) # for some reason data only comes thorugh on the second call. so first call to get it out of the way
    while len(response_data['added']) < 1:
        response_data = get_api_data(acc_tok)
     
    add_transactions(session['user_id'],response_data) # add the response to the database
    # query the database and display the data
    data = get_all_user_transactions(session['user_id'])
    # pass to html and use react to display
    return render_template("test.html", acc_tok=data)


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all() # create the tables if they aren't already created
    app.run(debug=True,port=5000)