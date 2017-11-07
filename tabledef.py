from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql://root:root@localhost/coen174', echo=True)
Base = declarative_base()


class Course(Base):
    __tablename__ = "course_info"

    id = Column(Integer, primary_key=True)
    school = Column(String(255))
    school_course = Column(String(255))
    scu_course = Column(String(80))
    determination = Column(String(80))
    advisor = Column(String(255))
    date = Column(Date)
    def __init__(self, school, school_course, scu_course, determination, advisor, date):
        self.school = school
        self.school_course = school_course
        self.scu_course = scu_course
        self.determination = determination
        self.advisor = advisor
        self.date = date


class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(80))
 
    #----------------------------------------------------------------------
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password

# create tables
Base.metadata.create_all(engine)
