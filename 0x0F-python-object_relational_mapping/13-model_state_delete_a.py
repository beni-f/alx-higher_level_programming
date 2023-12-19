#!/usr/bin/python3
# A script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
"""
    12-model_state_update
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%'))

    for delete_query in query:
        session.delete(delete_query)

    session.commit()