#!/usr/bin/python3
"""Script to list all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username, password, database = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to select all cities with their respective states
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
