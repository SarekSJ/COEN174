from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('<put db string here>', echo=True)
Base = declarative_base()