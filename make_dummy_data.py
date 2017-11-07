from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from tabledef import *
from datetime import datetime

engine = create_engine('mysql://root:root@localhost/coen174', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

session.add(Course('Gonzaga University',  'United States', 'CS 145', 'COEN 122', 'Rejected', 'Figueira', datetime.now(), "Not close enough to the syllabus of COEN 122"))
session.add(Course('San Jose State University',  'United States', 'RLGN 345', 'RSOC 12', 'Approved', 'Atkinson', datetime.now(), "Covered everything in RSOC 12"))
session.add((Course('Saint Edwards University',  'United States', 'MATH 2', 'AMTH 108', 'Rejected', 'Fang', datetime.now(), "Not good")))
session.add(User('Zach Graham', 'Zip Dog'))
session.add(User('Brandon Smith', 'Zip Dog'))

session.commit()