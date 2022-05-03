-- Customer table data
SELECT session_user, current_database();
INSERT INTO Customer (custId, custEmail, firstName, lastName)
 VALUES ('c001','dp@cowboys.com', 'Dakota', 'Prescott');

 INSERT INTO Customer (custId,  custEmail, firstName, lastName)
 VALUES ('c002', 'tb@buccaneers.com','Tom', 'Brady');

 INSERT INTO Customer (custId,  custEmail, firstName, lastName)
 VALUES ('c003', 'ja@bills.com','Josh', 'Allan');

 INSERT INTO Customer (custId,  custEmail, firstName, lastName)
 VALUES ('c004', 'lj@ravens.com','Lamar', 'Jackson');

 INSERT INTO Customer (custId, custEmail,  firstName, lastName)
 VALUES ('c005', 'pm@chiefs.com', 'Patrick', 'Mahomes');

--  Salesperson table data

INSERT INTO Salesperson (empId, empemail, firstName, lastName, dateHired)
VALUES ('y001','aj@yankees.com' , 'Aaron' , 'Judge', TO_DATE('1992-04-26','YYYY-MM-DD'));

INSERT INTO Salesperson (empId,empemail ,firstName, lastName, dateHired)
VALUES ('y002', 'gs@yankees.com','Giancarlo', 'Stanton', TO_DATE('1989-11-08','YYYY-MM-DD'));

INSERT INTO Salesperson (empId, empemail , firstName, lastName, dateHired)
VALUES ('y003', 'ar@yankees.com', 'Anthony', 'Rizzo', TO_DATE('1989-08-08','YYYY-MM-DD'));

INSERT INTO Salesperson (empId, empemail,firstName, lastName, dateHired)
VALUES ('y004', 'gc@yankees.com', 'Gerrit', 'Cole',  TO_DATE('1990-09-08','YYYY-MM-DD'));

INSERT INTO Salesperson (empId, empemail, firstName, lastName,dateHired)
VALUES ('y005', 'ac@yankees.com','Aroldis', 'Chapman', TO_DATE('1988-02-08','YYYY-MM-DD'));

-- Car table

 INSERT INTO Car (vin, make, model, listPrice, dateOfManufacture, color)
 VALUES ('JH4DB7550SS005262', 'Mini', 'Cooper', 24990.00, TO_DATE('2019-01-01','YYYY-MM-DD'),'Green');

 INSERT INTO Car (vin, make, model, listPrice, dateOfManufacture, color)
 VALUES ('JH4KA3140KC015221', 'Lincoln', 'MKZ', 18990.00, TO_DATE('2014-01-01','YYYY-MM-DD'), 'Red');

 INSERT INTO Car (vin, make, model, listPrice, dateOfManufacture, color)
 VALUES ('1G3NF52E3XC403652', 'Acura', 'TLX', 22590.00, TO_DATE('2015-01-01','YYYY-MM-DD'), 'White');

 INSERT INTO Car (vin, make, model, listPrice, dateOfManufacture, color )
 VALUES ('JF1SF63501H759113', 'Cadillac', 'CTS', 31990.00, TO_DATE('2015-01-01','YYYY-MM-DD'), 'Black');

 INSERT INTO Car (vin, make, model, listPrice, dateOfManufacture, color)
 VALUES ('WBANV93589C133312', 'Infiniti','Q50', 19590.00, TO_DATE('2014-01-01','YYYY-MM-DD'),  'Black');


-- CarSale

INSERT INTO Sale (invoiceNo, saleDate, salePrice, custId, empId)
VALUES ('i001', TO_DATE('2021-01-01','YYYY-MM-DD'), 24990, 'c001', 'y001');

INSERT INTO Sale (invoiceNo, saleDate, salePrice, custId, empId )
VALUES ('i002', TO_DATE('2021-02-01','YYYY-MM-DD'), 24990, 'c002', 'y002');

INSERT INTO Sale (invoiceNo, saleDate, salePrice, custId, empId)
VALUES ('i003', TO_DATE('2021-03-01','YYYY-MM-DD'), 24990, 'c003', 'y003');

INSERT INTO Sale (invoiceNo, saleDate, salePrice, custId, empId )
VALUES ('i004', TO_DATE('2021-04-01','YYYY-MM-DD'), 24990, 'c004', 'y004');

INSERT INTO Sale (invoiceNo, saleDate, salePrice, custId, empId )
VALUES ('i005', TO_DATE('2021-05-01','YYYY-MM-DD'), 24990, 'c005', 'y005');
