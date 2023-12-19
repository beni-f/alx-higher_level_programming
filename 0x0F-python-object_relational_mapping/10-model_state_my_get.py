#!/usr/bin/python3
"""
    10-model_state_my_get
"""
# A script that prints the State object with the name passed as argument from the hbtn_0e_6_usa
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

    list_state = []

    for states in query:
        list_state.append(states.name)

    query = session.query(State)\
            .filter(State.name == '{}'.format(sys.argv[4])).first()
    
    if sys.argv[4] not in list_state:
        print("Not found")
    else:
        print(query.id)