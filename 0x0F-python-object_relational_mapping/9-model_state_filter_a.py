#!/usr/bin/python3
"""
    9-model_state_filter_a
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
        A script that lists all State objects
        that contain the letter a from the database hbtn_0e_6_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for states in query:
        print('{}: {}'.format(states.id, states.name))
    
    session.close()