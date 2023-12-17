#!/usr/bin/python3
#A python file that contains the class definition of a State and an instance Base = declarative_base():

"""
    model_state.py
"""
from sqlalchemy.orm import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
        Inherits from Base

        Args:
            Base (class): inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


