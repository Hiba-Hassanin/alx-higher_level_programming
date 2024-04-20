#!/usr/bin/python3
"""Script to list all states with a name starting with N from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


def filter_states_by_name(username, password, database):
    """Connects to MySQL server and lists states starting with 'N'"""

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

    # Disconnect from server
    db.close()


if __name__ == "__main__":
    # Accept command line arguments
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    username, password, database = argv[1:]

    # Call the function to filter states by name
    filter_states_by_name(username, password, database)
