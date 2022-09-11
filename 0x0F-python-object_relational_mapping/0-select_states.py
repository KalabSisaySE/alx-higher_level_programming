#!/usr/bin/python3
"""the `0-select_states.py` module
prints all the states found in the database
"""
import MySQLdb
from sys import argv


db = MySQLdb.connect(host="localhost",
                     user=argv[1],
                     passwd=argv[2],
                     db=arvg[3],
                     port=3306)
cur = db.cursor()
cur.execute("SHOW * FROM `states` ORDERBY `states.id`")
rows = cur.fetchall()


if __name__ == "__main__":
    for row in rows:
        print(row)
