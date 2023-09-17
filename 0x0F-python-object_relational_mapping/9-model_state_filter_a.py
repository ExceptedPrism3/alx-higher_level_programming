#!/usr/bin/python3
""" Query db using sqlalchemy module
    filter results which contains letter a
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    con_str = "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3])
    engine = create_engine(con_str)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id)
    for row in res:
        print("{}: {}".format(row.id, row.name))
