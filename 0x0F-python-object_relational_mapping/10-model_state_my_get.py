#!/usr/bin/python3
"""Script to print the State object's ID with the name passed as argument"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username, password, database, state_name = sys.argv[1:]

    # Create engine to interact with database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            username, password, database), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the given state name
    state = session.query(State).filter(State.name == state_name).first()

    # Print result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
