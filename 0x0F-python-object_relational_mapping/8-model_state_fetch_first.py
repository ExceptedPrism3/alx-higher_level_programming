#!/usr/bin/python3
"""
This script prints the first `State` object from the database `hbtn_0e_6_usa`

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)

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
    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': usr, 'password': pwd, 'database': db_name}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    instance = session.query(State).order_by(State.id).first()
    if instance:
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")
