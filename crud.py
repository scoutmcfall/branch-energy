"""CRUD operations for Branch Energy app. """

from model import db, connect_to_db
# User, Donki, Epic, Rating,


def create_record():
    """Create a new record (eg new branchId on customer enrollment)"""

    # user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return record

def update_record():
    """Update a record (eg add billingAccountNumber) for a given branchId"""
    # user = User.query.filter(User.email == email).first()
    # user.email = new_email
    
    db.session.commit()

    return record

def branch_id_attributes():
    """Read and return the branchId attributes in an easy to parse format"""
  
    # user = User.query.filter(User.email == email).first()
    # user.password = new_password
    
    db.session.commit()
    return branch_id. #which attributes?


if __name__ == '__main__':
    from server import app
    connect_to_db(app)