#!/usr/bin/python3
"""Definition of the State class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_city import Base

class State(Base):
    """State class that inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete")
