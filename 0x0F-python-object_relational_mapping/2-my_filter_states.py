#!/usr/bin/python3
"""the `2-my_filter_states` module
prints lists of states with a name matches the given argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY \
    id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == "N":
            print(row)
    cur.close()
    db.close()
