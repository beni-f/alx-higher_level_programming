#!/usr/bin/python3
# A script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""
    11-model_state_insert
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

    query = session.query(State)

    add_state = State(name="Louisiana")
    session.add(add_state)
    session.commit()

    query = session.query(State).order_by(State.id.desc()).first()

    print(query.id)
    session.close()