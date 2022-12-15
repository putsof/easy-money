from model import User, Transaction, Category, Budget, connect_to_db, db

def create_user(fname,lname,email,password):
    user = User(fname=fname,lname=lname,email=email,password=password)
    db.session.add(user) 
    db.session.commmit()
    return user
    
def create_transaction(user_id,bank_name,vendor,amount):
    return Transaction(user_id=user_id,bank_name=bank_name,vendor=vendor,amount=amount)

def create_category(category_id,category_name):
    return Category(category_id=category_id,category_name=category_name)

def create_budget(max_amount,category_id,shared):
    return Budget(max_amount=max_amount,category_id=category_id,shared=shared)

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
    
    



if __name__ == '__main__':
    from server import app
    connect_to_db(app)