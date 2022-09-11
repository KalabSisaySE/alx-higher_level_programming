#!/usr/bin/python3
"""the `0-select_states.py` module
prints lists all states with a name starting with 'N' from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
