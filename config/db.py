from curses import echo
from sqlalchemy import create_engine, MetaData

engine=create_engine('mysql+pymysql://dbtest:1234@localhost:3306/py_crud', echo=True)
meta=MetaData()
con = engine.connect()
