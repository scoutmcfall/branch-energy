"""Models for Branch Energy microservice."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    """A customer."""
    __tablename__ = 'customers'

    branch_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    email = db.Column(db.String, unique=True)
    billing_account_number = db.Column(db.Integer) #should this be unique?

    def __repr__(self):
        return f'<Record branch_id={self.branch_id} email = {self.email} billing = {self.billing_account_number}>'
    


def connect_to_db(somedatabase, db_uri="postgresql:///", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

    
if __name__ == "__main__":
        from server import app

        connect_to_db(app)
        db.create_all()