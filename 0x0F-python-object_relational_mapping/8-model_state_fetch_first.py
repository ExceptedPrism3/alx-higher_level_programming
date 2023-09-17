#!/usr/bin/python3
""" queries and displays the first state in the State table """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sys import argv

if __name__ == "__main__":
    db_cred = '''mysql+mysqldb://{}:{}@localhost/{}'''.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_cred)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).first()
    if not res:
        print("Nothing")
    print("{}: {}".format(res.id, res.name))
