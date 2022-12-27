#!/usr/bin/python3

"""This script define a class of City
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    """Representation of a city class that inherits from base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
