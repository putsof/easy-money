from model import User, Transaction, Category, Budget, connect_to_db, db

def create_user(fname,lname,email,password):
    user = User(fname=fname,lname=lname,email=email,password=password)
    db.session.add(user) 
    db.session.commit()
    return user
    
def create_transaction(user_id,account_id,merchant_name,amount,date):
    trans = Transaction(user_id=user_id,account_id=account_id,merchant_name=merchant_name,amount=amount,date=date)
    db.session.add(trans)
    db.session.commit()
    return trans

def create_category(category_name):
    cat = Category(category_name=category_name)
    db.session.add(cat)
    db.session.commit()
    return cat

def create_budget(max_amount,category_id,shared):
    bud = Budget(max_amount=max_amount,category_id=category_id,shared=shared)
    db.session.add(bud)
    db.session.commit()
    return bud

def get_user_by_id(user_id):
    """Return user from primary key"""
    return User.query.get(user_id)

def get_user_by_email(email):
    """Return user from email"""
    return User.query.filter_by(email=email).one() # this will fail if there is more than one
    # so maybe need some error handling here

def update_access_token(user_id, access_token):
    """Update the users access token in the database"""
    user = get_user_by_id(user_id)
    user.access_token = access_token
    db.session.commit()
    # in the future lets check that the commit was successful

def add_transactions(user_id, response):
    for trans_action in response['added']:
        if trans_action['merchant_name'] is None or trans_action['merchant_name'] == "":
            create_transaction(user_id=user_id,
                                account_id=trans_action['account_id'],
                                merchant_name=trans_action['name'],
                                amount=trans_action['amount'],
                                date=trans_action['date'])
        else:
            create_transaction(user_id=user_id,
                                account_id=trans_action['account_id'],
                                merchant_name=trans_action['merchant_name'],
                                amount=trans_action['amount'],
                                date=trans_action['date'])

def get_all_user_transactions(user_id):
    """Get all transactions from a user
    TODO - add ability to get from a certain date"""
    return Transaction.query.filter_by(user_id=user_id).all()

def get_all_user_transactions_json(user_id):
    trans_list = Transaction.query.filter_by(user_id=user_id).all()
    list_of_dicts = []

    for transaction in trans_list:
        trans_dict = {
                "trans_id": transaction.transaction_id,
                "merchant_name": transaction.merchant_name,
                "amount": str(transaction.amount),
                "date": transaction.date
        }
        list_of_dicts.append(trans_dict)
    return list_of_dicts



if __name__ == '__main__':
    from server import app
    connect_to_db(app)