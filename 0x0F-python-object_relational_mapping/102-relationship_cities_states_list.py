#!/usr/bin/python3
"""This script lists all City objects from the database hbtn_0e_101_usa
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

    for city in session.query(State):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.commit()
    session.close()
