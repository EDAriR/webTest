import sqlalchemy
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.orm import sessionmaker

conn = create_engine('postgresql://localhost:5432/measurementdb', echo=True)

Session = sessionmaker(bind=conn)
session = Session()

