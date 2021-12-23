"""CRUD operations for Branch Energy app. """

from model import db, Record, connect_to_db
#id updated at and created at for each record
# dont turn off the lambda after each requrest, leave up for 2 min to handle butsts
#optimize for reading  
#remember to delete everything when you're done with it so you don't get a huge bill
#make an endpoint in lambda that returns the number 1 when you hit it
# postgres cuz of relationships and don't like storing duplicate data
#rds(connect to rds via lambda tutorial)/aurora?

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