"""server for Branch Energy microservice"""

# The microservice requires a handful of endpoints to support 3 common CRUD transactions:
# Create a new record (eg new branchId on customer enrollment)
# Update a record (eg add billingAccountNumber) for a given branchId
# Read and return the branchId attributes in an easy to parse format 
# Endpoints should support the Flow of a given branchId and Uses by the business

from flask import (Flask, render_template, request, flash, session,
                   redirect)
import os
import requests
import pprint
import pytest
import crud



app = Flask(__name__)

@app.route("/create", methods=["POST"])
def create_record():
    """Create a new record."""

    # email = request.form.get("email")
    # billing_account_number = request.form.get("password")
    # record = crud.get_user_by_branch_id(branch_id)
 
    # if record:
    #     flash("Cannot create an account with that email. Try again.")
    # else:
    #     record = crud.create_record(email, billing_account_number)
    #     session["record_branch_id"] = record.branch_id 
       
    #     flash("Account created! You are logged in.")

    return redirect("/")


@app.route("/update", methods = ["POST"])
def update_record():
    """Update record"""
    # new_billing_account_number = request.form.get("new_billing_account_number")
    # record = crud.get_user_by_branch_id(branch_id)
    # branch_id = session["record_branch_id"]
    # #check to see if new_email already in db, and change info if not
    # if record:
    #         flash ("Sorry, taken, try again with a different email address.")
    #         return redirect("/")
    # else:
    #         record = crud.update_record(email = email, new_email = new_email)
    #         session["record_branch_id"] = record.branch_id
    #         session["billing_account_number"] = record.billing_account_number #but do i need to put this in session?
    #         return redirect("/")
    return redirect("/")

@app.route("/attributes")
def display_attributes():
    """Read and return the branchId attributes in an easy to parse format """
    # record = crud.get_user_by_branch_id(session["record_branch_id"])
    # branch_id = record.branch_id
    

    return record.branch_id, record.email, record.billing_account_number

if __name__ == "__main__":

    app.run(port=5000, threaded=True, debug=True) #adding threaded means that concurrent requests can be made