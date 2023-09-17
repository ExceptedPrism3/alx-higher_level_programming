#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument
from the database hbtn_0e_6_usa

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name to search (str)

"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from model_state import Base, State


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    st_name = sys.argv[4]
    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': usr, 'password': pwd, 'database': db_name}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    q = session.query(State).filter(State.name == st_name).order_by(State.id)

    if q.first():
        print(q.first().id)
    else:
        print("Not found")
