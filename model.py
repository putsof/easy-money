from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy() # create sqlalchemy instance 

# assosiation tables for the many to many relationshipts
users_budgets = db.Table(
    "users_budgets",
    db.Column("users_budgets_id", db.Integer, primary_key=True, autoincrement=True),
    db.Column("user_id", db.ForeignKey("users.user_id")),
    db.Column("budget_id", db.ForeignKey("budgets.budget_id"))
)

budgets_categories = db.Table(
    "budgets_categories",
    db.Column("budgets_categories_id", db.Integer, primary_key=True, autoincrement=True),
    db.Column("category_id", db.ForeignKey("categories.category_id")),
    db.Column("budget_id", db.ForeignKey("budgets.budget_id"))
)

class User(db.Model):
    """Users of the application"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(64), nullable=False)
    lname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    access_token = db.Column(db.String(64), nullable=True)
    partner_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True) # is the partners user id


    # relationships
    partner = db.relationship("User")
    budgets = db.relationship("Budget", secondary="users_budgets", back_populates="users") # many to many to budgets

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Transaction(db.Model):
    """Transactions from the user accounts"""
    __tablename__ = "transactions"

    transaction_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    account_id = db.Column(db.String(64), nullable=False)
    merchant_name = db.Column(db.String(64), nullable=True)
    amount = db.Column(db.Numeric(6,2), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"), nullable=True)

    # relationships
    category = db.relationship("Category", back_populates="transactions") # one to one

    def __repr__(self):
        return f'<Transaction transaction_id={self.transaction_id} amount={self.amount}>'

class Category(db.Model):
    """User defined budget categories"""
    __tablename__ = "categories"

    category_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    category_name = db.Column(db.String(64), nullable=False)
    max_amount = db.Column(db.Numeric(6,2), nullable=False)
    shared_id = db.Column(db.String(64), nullable=True)

    # relationships
    transactions = db.relationship("Transaction", back_populates="category") # one to one
    budgets = db.relationship("Budget", secondary="budgets_categories", back_populates="categories") # many to many to budgets


    def __repr__(self):
        return f'<Category category_id={self.category_id} category_name={self.category_name}>'

class Budget(db.Model):
    """Budget categories defind by the user"""
    __tablename__ = "budgets"

    budget_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    max_amount = db.Column(db.Numeric(6,2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"), nullable=False)
    shared = db.Column(db.Boolean, nullable=False)

    #relationships
    categories = db.relationship("Category", secondary="budgets_categories", back_populates="budgets") # many to many to categories
    users = db.relationship("User", secondary="users_budgets", back_populates="budgets")

    def __repr__(self):
        return f'<Budget budget_id={self.budget_id} category_name={self.category_name} max_amount={self.max_amount}>'

def connect_to_db(flask_app, db_uri=f'postgresql:///easy', echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.