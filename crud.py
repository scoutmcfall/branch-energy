"""CRUD operations for Branch Energy app. """

from model import db, Record, connect_to_db


def create_record():
    """Create a new record (eg new branchId on customer enrollment)"""

    record = Record(email=email)

    db.session.add(record)
    db.session.commit()

    return record

def update_record():
    """Update a record (eg add billingAccountNumber) for a given branchId"""
    record = Record.query.filter(record.branch_id == branch_id).first()
    record.billing_account_number = new_billing_account_number
    
    db.session.commit()

    return record

def branch_id_attributes():
    """Read and return the branchId attributes in an easy to parse format"""
  
    record = Record.query.filter(Record.branch_id == branch_id).first()
    
    return record


if __name__ == '__main__':
    from server import app
    connect_to_db(app)