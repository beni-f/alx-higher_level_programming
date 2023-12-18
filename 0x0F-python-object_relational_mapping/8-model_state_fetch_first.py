#!/usr/bin/python3
"""
    8-model_state_fetch_first
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
        A script that prints the first State
        object from the database hbtn_0e_6_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).first()

    if query is None:
        print('Nothing')
    else:
        print('{}: {}'.format(query.id, query.name))
    
    session.close()