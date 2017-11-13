from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from tabledef import *
from datetime import datetime

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

session.add(Course('Gonzaga University',  'United States', 'CS 145', 'COEN 122', 'Rejected', 'Figueira', datetime.now(), "Not close enough to the syllabus of COEN 122"))
session.add(Course('San Jose State University',  'United States', 'RLGN 345', 'RSOC 12', 'Approved', 'Atkinson', datetime.now(), "Covered everything in RSOC 12"))
session.add((Course('Saint Edwards University',  'United States', 'MATH 2', 'AMTH 108', 'Rejected', 'Fang', datetime.now(), "AMTH 108 has a completely different syllabus")))
session.add(User('Figueira', 'Zip Dog'))
session.add(User('Fang', 'Zip Dog'))
session.add(User('Atkinson', 'Zip Dog'))

session.commit()