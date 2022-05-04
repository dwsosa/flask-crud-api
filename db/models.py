def create_classes(db):
    class Customer(db.Model):
        __tablename__ = 'customer'
        custid = db.Column(db.String(255), db.ForeignKey('sale.custid'), primary_key=True)
        custemail = db.Column(db.String(255))
        firstname = db.Column(db.String(255))
        lastname = db.Column(db.String(255))
        # one to many
        FK_children = db.relationship("Sale")

        def __repr__(self):
            return '<customer %r>' % (self.name)

    class Salesperson(db.Model):
        __tablename__ = 'salesperson'
        empid = db.Column(db.String(255), db.ForeignKey('sale.empid'), primary_key=True)
        empemail = db.Column(db.String(255))
        firstname = db.Column(db.String(255))
        lastname = db.Column(db.String(255))
        datehired= db.Column(db.Date)
        FK_children = db.relationship("Sale")
        def __repr__(self):
            return '<salesperson %r>' % (self.name)
    
    class Car(db.Model):
        __tablename__ = 'car'
        vin = db.Column(db.String(255), primary_key=True)
        make = db.Column(db.String(255))
        model = db.Column(db.String(255))
        listprice = db.Column(db.Numeric(10,2))
        color = db.Column(db.String(255))
        dateofmanufacture = db.Column(db.Date)
        def __repr__(self):
            return '<car %r>' % (self.name)
                
    class Sale(db.Model):
        __tablename__ = 'sale'
        invoiceno = db.Column(db.String(255), primary_key=True)
        saledate = db.Column(db.Date)
        saleprice = db.Column(db.Numeric(10,2))
        custid = db.Column(db.String(255))
        empid = db.Column(db.String(255))
        def __repr__(self):
            return '<sale %r>' % (self.name)    
    
    return Customer, Salesperson, Car, Sale