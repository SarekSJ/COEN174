from flask import Flask, flash, redirect, render_template, request, session, abort
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from tabledef import *
from app import app

engine = create_engine('mysql://root:root@localhost/coen174', echo=True)
Base = declarative_base()

# @app.route('/table')
# def table_screen():
#     Session = sessionmaker(bind=engine)
#     s = Session()
#     items = s.query(Course).all();
#     return render_template('table.html', items=items)

def add_row():
    pass