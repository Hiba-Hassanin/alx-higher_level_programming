#!/usr/bin/python3
"""Script to list all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    # Create a cursor object using cursor() method
    cur = db.cursor()

    # Execute SQL query to select all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows in a list of tuples
    rows = cur.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
