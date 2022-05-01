import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response, make_response, jsonify, abort
from config import *

app = Flask(__name__)

############################# DATABASE SETUP ############################
LOCAL_DB = f"{DIALECT}://{USERNAME}/{PASSWORD}@localhost:{PORT}/{DATABASE_NAME}"

# default to local db if no DB environmental variable provided i.e., not a production environment
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or LOCAL_DB

############################# API ROUTES ############################
# list all cars for sale
@app.route("/forsale", methods=["GET"])
def all_cars_for_sale():
    # print("test")
    return "<p>Hello, World!</p>"

# list details for specific car using VIN for reference
@app.route("/forsale/<VIN>", methods=["GET"])
def details_for_specific_car(VIN):
    # print("param value: {}".format(VIN))
    return "<p>Hello, World!</p>"

# list details regarding a transaction by referencing employee ID and the orderID
@app.route("/employee/<employeeId>/order/<orderId>", methods=["GET"])
def add_ons_for_specific_car(employeeId, orderId):
    # print("employee value: {}\norder value: {}".format(employeeId, orderId))
    return "<p>Hello, World!</p>"

# API error handler
@app.errorhandler(404)
def resource_not_found(e):
    response = make_response(jsonify({"message" : "no match on API server for the data requested"}), 404)
    response.headers["Content-Type"] = "application/json"
    return response





############################# HTML ROUTES ############################

# 404 for any html routes that dont match 
@app.route("/", defaults={"path": ""})
@app.route("/<string:path>") 
@app.route("/<path:path>")
def hello_world(path):
    return "<p>{}<br><br>RESOURCE NOT FOUND <br>ERROR 404 <br>NO MATCHING ROUTES ON SERVER</p>".format(path), 404

if __name__ =='__main__':
    app.run(port=718)
