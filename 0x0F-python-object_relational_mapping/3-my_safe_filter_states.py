#!/usr/bin/python3
"""Script to display all values in the states table of hbtn_0e_0_usa
where name matches the provided argument (safe from SQL injection)"""

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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the state name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all the rows that match the query
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
