#!/usr/bin/python3
"""This script lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import Base, City


if __name__ == "__main__":
    """To get the state of the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.commit()
    session.close()
