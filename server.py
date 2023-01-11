"""Server for easy money"""

from flask import Flask, render_template, request, jsonify, session, redirect, flash
from model import connect_to_db, db
from flask_sqlalchemy import SQLAlchemy
from seed_database import generate_access_token, get_api_data
from crud import get_user_by_email, update_access_token, create_user,add_transactions,get_all_user_transactions, get_all_user_transactions_json, create_budget, create_category, get_all_user_categories, update_transaction_category, check_user_password_by_email

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

@app.route("/login")
def login():
    """Displayes the Login page"""
    return render_template("login.html")

@app.route("/do-login", methods=['POST'])
def do_login():
    """Log existing user into the application"""
    #TODO check if email is in database, if not, send them to signup
    #TODO check that the password is correct
    user = get_user_by_email(request.form['email'])
    session['user_id'] = user.user_id
    return render_template("javadnd.html") # issue here maybe

@app.route('/login-check.json')
def login_check_json():
    email = request.json.get("email")
    password = request.json.get("password")

    if get_user_by_email(email) is None:
        return jsonify({'status': 'Email does not exist'})
    else:
        if check_user_password_by_email(email,password): #login successful
            user = get_user_by_email(email)
            session['user_id'] = user.user_id
            return render_template("javadnd.ht")
            # return jsonify({'status': 'Login successful'})
        else:
            return jsonify({'status': 'Incorrect Password'})
 
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
    return render_template("create_budget.html")
    # return render_template("create_account.html", bank_names=BANK_ID.keys())

@app.route("/do-create-budgets", methods=['POST'])
def do_create_budgets():
    for count in range(int(len(request.form)/2)):
        create_category(category_name=request.form["category" + str(count)],
                           max_amount=request.form["amount" + str(count)],
                           user_id=session['user_id'])
  
    return render_template("create_account.html", bank_names=BANK_ID.keys())

@app.route("/create-account", methods=['POST'])
def create_account():
    return render_template("javadnd.html")


@app.route("/dashboard", methods=['POST'])
def dashboard():
    acc_tok = generate_access_token(BANK_ID[request.form['bankname']]) # generate the access token for the new user
    update_access_token(session['user_id'], acc_tok) # add token to User
  
    response_data = get_api_data(acc_tok) # call the api until there is data
    while len(response_data['added']) < 1:
        response_data = get_api_data(acc_tok)
     
    add_transactions(session['user_id'],response_data) # add the response to the database
    data = get_all_user_transactions(session['user_id'])  # query the database and display the data
    return render_template("javadnd.html")

@app.route("/transaction.json")
def transaction():
    # i want the merchant name and amount
    trans_list = get_all_user_transactions_json(session['user_id'])
    return jsonify(trans_list)

@app.route("/categories.json")
def categories():
    # i want all the categories associated with the user
    cat_list = get_all_user_categories(session['user_id'])
    return jsonify(cat_list)

@app.route("/javadnd")
def javadnd():
    return render_template("javadnd.html")

@app.route("/create-budget")
def create_budgets():
    return render_template("create_budget.html")

@app.route("/update-trans-cat.json", methods=['POST'])
def update_trans_cat():
    trans_id = request.json.get('trans_id')
    
    category_name = request.json.get('category_name')
    print("here is the trans id " + category_name)
    update_transaction_category(session['user_id'],int(trans_id),category_name)
    
    return jsonify({'status': 'okay'})

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all() # create the tables if they aren't already created
    app.run(debug=True,port=5000)