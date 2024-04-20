#!/usr/bin/python3
"""Script to print the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username, password, database = sys.argv[1:]

    # Create engine to interact with database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            username, password, database), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print result
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close session
    session.close()
