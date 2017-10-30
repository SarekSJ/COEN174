from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from tabledef import *
from datetime import datetime

engine = create_engine('mysql://root:root@localhost/coen174', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

session.add(Course('Gonzaga University', 'CS 145', 'COEN 122', 'Rejected', 'Figueira', datetime.now()))
session.add(Course('San Jose State University', 'RLGN 345', 'RSOC 12', 'Approved', 'Atkinson', datetime.now()))
session.add((Course('Saint Edwards University', 'MATH 2', 'AMTH 108', 'Rejected', 'Fang', datetime.now())))
session.add(User('Zach Graham', 'Zip Dog'))
session.add(User('Brandon Smith', 'Zip Dog'))

session.commit()