#!/usr/bin/python3
"""Script to list all states with a name starting with N
from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows that match the query
    rows = cursor.fetchall()

    # Iterate through each row and print it if the state name starts with 'N'
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    # Close the cursor and database connection
    cursor.close()
    connection.close()
