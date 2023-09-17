#!/usr/bin/env python3
""" Query db using sqlalchemy module
    filter results by search term passed as script argument
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    con_str = "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3])
    engine = create_engine(con_str)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        res = session.query(State).filter(
            State.name == argv[4]).order_by(State.id).one()
        print(res.id)
    except NoResultFound:
        print("Not found")
