#!/usr/bin/python3
""" link to table class and querying """
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sys import argv


if __name__ == "__main__":
    db_url = '''mysql+mysqldb://{}:{}@localhost/{}'''.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).order_by(State.id)
    for row in res:
        print('{}: {}'.format(row.id, row.name))
