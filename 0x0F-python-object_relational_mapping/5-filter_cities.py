#!/usr/bin/python3
"""Script to list all cities of a given state from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (argv[4],))
    rows = cursor.fetchall()

    # Print results
    print(", ".join(city[0] for city in rows))

    # Close the cursor and database connection
    cursor.close()
    db.close()
