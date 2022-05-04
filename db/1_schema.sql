SELECT session_user, current_database();

GRANT ALL PRIVILEGES ON DATABASE dealership TO postgres;

CREATE TABLE Customer (
 	custid VARCHAR(255),
 	custemail VARCHAR(255),
 	firstname VARCHAR(255),
 	lastname VARCHAR(255)
     );
     
 CREATE TABLE Salesperson (		 
 	empid VARCHAR(255),
	empemail VARCHAR(255),
 	firstname VARCHAR(255),
 	lastname VARCHAR(255),
    datehired DATE
);

 CREATE TABLE Car (
 	vin VARCHAR(255),
 	make VARCHAR(255),
 	model VARCHAR(255),
 	listprice DECIMAL(10,2),
 	dateofmanufacture DATE,
    color VARCHAR(255)
);

CREATE TABLE Sale (
    invoiceno VARCHAR(255),
	saledate DATE,
	saleprice DECIMAL(10,2),
   	custid VARCHAR(255),
    empid VARCHAR(255)
);

ALTER TABLE Customer ADD CONSTRAINT PK_Customer PRIMARY KEY (custid);
ALTER TABLE Salesperson ADD CONSTRAINT PK_Salesperson PRIMARY KEY (empid);
ALTER TABLE Car ADD CONSTRAINT PK_Car PRIMARY KEY (vin);
ALTER TABLE Sale ADD CONSTRAINT PK_Sale PRIMARY KEY (invoiceno);

ALTER TABLE Sale ADD CONSTRAINT FK_Sale_empid_Salesperson_empid  FOREIGN KEY (empid) REFERENCES Salesperson(empid);
ALTER TABLE Sale ADD CONSTRAINT FK_Sale_custid_Salesperson_custid FOREIGN KEY (custid) REFERENCES Customer(custid);