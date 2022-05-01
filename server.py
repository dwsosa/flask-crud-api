import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response, make_response, jsonify, abort, redirect, url_for, render_template
from config import *
from db.models import create_classes
import requests
import json

app = Flask(__name__)

############################# DATABASE SETUP ############################
LOCAL_DB = f"{DIALECT}://{USERNAME}:{PASSWORD}@localhost:{PORT}/{DATABASE_NAME}"

# default to local db if no DB environmental variable provided i.e., not a production environment
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or LOCAL_DB

# SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Customer, Salesperson, Car, Sale = create_classes(db)

############################# API ROUTES ############################

# list all cars on the lot 
@app.route("/car", methods=["GET"])
def all_cars_for_sale():
    try:
        rows = db.session.query(Car.vin, Car.make, Car.model, Car.listprice, Car.color, Car.dateofmanufacture).all()
        cars = [{'VIN': row[0], 'make': row[1], 'model': row[2], 'sticker price': row[3], 'color' : row[4], 'manufacture date' : row[5]} for row in rows]
        response = jsonify({"rows": cars, "columns": list(cars[0].keys())})
        return response
    except:
        abort(500)

# list all employees
@app.route("/employee", methods=["GET"])
def all_employees():
    try:
        rows = db.session.query(Salesperson.empid, Salesperson.empemail, Salesperson.firstname, Salesperson.lastname, Salesperson.datehired ).all()
        employees = [{'employee id': row[0], 'employee email': row[1], 'first name': row[2], 'last name': row[3], 'date hired' : row[4]} for row in rows]
        response = jsonify({"rows": employees, "columns": list(employees[0].keys())})
        return response
    except:
        abort(500)

# list all sales
@app.route("/sale", methods=["GET"])
def all_sales():
    try:
        rows = db.session.query(Sale.invoiceno, Sale.saledate, Sale.saleprice, Sale.custid, Sale.empid ).all()
        sales = [{'invoice number': row[0], 'sale date':row[1], 'sale price': row[2], 'customer id': row[3], 'employee id' : row[4]} for row in rows]
        return jsonify({"rows": sales, "columns": list(sales[0].keys()) })
    except:
        abort(500)

# list all customers
@app.route("/customer", methods=["GET"])
def all_customers():
    try:
        rows = db.session.query(Customer.custid, Customer.custemail, Customer.firstname, Customer.lastname ).all()
        customers = [{'id': row[0], 'email':row[1], 'first name': row[2], 'last name': row[3]} for row in rows]
        return jsonify({"rows": customers, "columns": list(customers[0].keys())  })
    except:
        abort(500)

# list details for specific car using VIN for reference
@app.route("/car/<VIN>", methods=["GET"])
def specific_car(VIN):
    try:
        rows = db.session.query(Car.vin, Car.make, Car.model, Car.listprice, Car.color, Car.dateofmanufacture).filter(Car.vin==VIN).all()
        cars = [{'VIN': row[0], 'make': row[1], 'model': row[2], 'sticker price': row[3], 'color' : row[4], 'manufacture date' : row[5]} for row in rows]
        response = jsonify({"rows": cars, "columns": list(cars[0].keys()) })
        return response
    except:
        abort(500)

# list all sales for a given employee by referencing employee ID
@app.route("/employee/<employeeId>/order", methods=["GET"])
def all_sales_for_specific_employee(employeeId):
    try:
        employee_row = db.session.query(Salesperson.empid, Salesperson.empemail, Salesperson.firstname, Salesperson.lastname, Salesperson.datehired ).filter(Salesperson.empid==employeeId).all()
        employee_info = [{'employee id': row[0], 'employee email': row[1], 'first name': row[2], 'last name': row[3], 'date hired' : row[4]} for row in employee_row][0]
        sales_rows = db.session.query(Sale.invoiceno, Sale.saledate, Sale.saleprice, Sale.custid, Sale.empid ).filter(Sale.empid==employeeId).all()
        sales = [{'invoice number': row[0], 'sale date':row[1], 'sale price': row[2], 'customer id': row[3], 'employee id' : row[4]} for row in sales_rows]
        return jsonify({"rows": sales, "columns": list(sales[0].keys())})
    except:
        abort(500)

# list details regarding a transaction by referencing employee ID and the orderID
@app.route("/employee/<employeeId>/order/<orderId>", methods=["GET"])
def specific_sale(employeeId, orderId):
    try:
        rows = db.session.query(Sale.invoiceno, Sale.saledate, Sale.saleprice, Sale.custid, Sale.empid ).filter(Sale.empid==employeeId).filter(Sale.invoiceno==orderId).all()
        sales = [{'invoice number': row[0], 'sale date':row[1], 'sale price': row[2], 'customer id': row[3], 'employee id' : row[4]} for row in rows]
        return jsonify({"sale data": sales})
    except:
        abort(500)

# API error handler
@app.errorhandler(404)
def resource_not_found(e):
    try:
        response = make_response(jsonify({"message" : "no match on API server for the data requested"}), 404)
        response.headers["Content-Type"] = "application/json"
        return response
    except:
        abort(500)

############################# HTML ROUTES ############################

obj={}
obj["style"]="./static/css/style.css"
obj["logic"]="./static/js/logic.js"

@app.route("/")
def home():
    return redirect(url_for("home_route"))

@app.route("/home")
def home_route():
    return '<div>Welcome</div>'

@app.route("/dashboard/cars")
def cars_route():
    obj["title"]="Car Data Dashboard"
    CAR_DATA_API = "http://localhost:718/car"
    data = requests.get(CAR_DATA_API).json()
    return render_template("index.html", obj=obj, data=data )

@app.route("/dashboard/employees")
def employees_route():
    obj["title"]="Employee Data Dashboard"
    EMPLOYEE_DATA_API = "http://localhost:718/employee"
    data = requests.get(EMPLOYEE_DATA_API).json()
    return render_template("index.html", obj=obj, data=data )

@app.route("/dashboard/sales")
def sales_route():
    obj["title"]="Sales Data Dashboard"
    SALE_DATA_API = "http://localhost:718/sale"
    data = requests.get(SALE_DATA_API).json()
    return render_template("index.html", obj=obj, data=data )

@app.route("/dashboard/customers")
def customer_route():
    obj["title"]="Customer Data Dashboard"
    CUSTOMER_DATA_API = "http://localhost:718/customer"
    data = requests.get(CUSTOMER_DATA_API).json()
    return render_template("index.html", obj=obj, data=data )

@app.route("/summary/employee/<salespersonid>")
def salesperson_summary_report_route(salespersonid):
    obj["title"]=f"Employee {salespersonid} Report"
    SALESPERSON_REPORT_API = f"http://localhost:718/employee/{salespersonid}/order"
    data = requests.get(SALESPERSON_REPORT_API).json()
    return render_template("index.html", obj=obj, data=data )

@app.route("/saledetailed/employeee/<salespersonid>/order/<orderid>")
def detailed_sale_report_route(salespersonid, orderid):
    obj["title"]=f"Employee {salespersonid} Report"
    DETAILED_SALE_REPORT_API = f"http://localhost:718//employee/{salespersonid}/order/{orderid}"
    data = requests.get(DETAILED_SALE_REPORT_API).json()
    return render_template("index.html", obj=obj, data=data )

# 404 for any html routes that dont match 
@app.route("/", defaults={"path": ""})
@app.route("/<string:path>") 
@app.route("/<path:path>")
def hello_world(path):
    return "<p>{}<br><br>RESOURCE NOT FOUND <br>ERROR 404 <br>NO MATCHING ROUTES ON SERVER</p>".format(path), 404

if __name__ =='__main__':
    app.run(port=718, debug=True)
