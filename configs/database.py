from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.configs.config import Settings
#from sshtunnel import SSHTunnelForwarder

param = Settings()

'''
print('Connecting to the PostgreSQL Database...')

try:
    server = SSHTunnelForwarder(
        param.db_ssh_server,
        ssh_username=param.db_ssh_user,
        ssh_password=param.db_ssh_pass,
        remote_bind_address=('localhost', int(param.db_port))
    )
    server.start()
    print("server succesfully connected")
    database_url = f"postgresql://{param.db_user}:{param.db_password}@{param.db_server}:{server.local_bind_port}/{param.db_name}" #PostgreSQL TUNNEL
except:
    print("failed to connect ...")
'''

#database_conn = f"mssql+pymssql://{param.db_user}:{param.db_password}@{param.db_server}:{param.db_port}/{param.db_name}" #SQLSERVER
database_url = f"postgresql://{param.db_user}:{param.db_password}@{param.db_server}:{param.db_port}/{param.db_name}" #PostgreSQL


#server = 'nomad2805'
#database = 'DMSTEST'

#database_url = f"mssql+pymssql://{check.db_user}:{check.db_password}@{check.db_server}/{check.db_name}" #MSSQL SERVER
#database_url = 'mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
#database_url = f"postgresql://{param.db_user}:{param.db_password}@{param.db_server}:{param.db_port}/{param.db_name}" #POSTGRESQL

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()