from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

sql_username = "<MySql_username>"
sql_password = "<MySql_password>"
hostname = "<MySql_Hostname>"
port = "" # Leave empty if your MySql server isn't attached to a specific port
database_name = "<MySql_DatabaseName>"


engine = create_engine('mysql://'+sql_username+':'+sql_password+'@'+hostname+port+'/'+database_name, echo=True)
Base = declarative_base()