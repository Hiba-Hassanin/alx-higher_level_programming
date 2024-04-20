#!/usr/bin/python3
"""Script to list all cities of a given state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username, password, database, state_name = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Prepare the SQL query with a parameter placeholder
    query = """
            SELECT GROUP_CONCAT(name SEPARATOR ', ')
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """

    # Execute the query with the state name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Print results
    if result:
        print(result)

    # Close the cursor and database connection
    cursor.close()
    db.close()
