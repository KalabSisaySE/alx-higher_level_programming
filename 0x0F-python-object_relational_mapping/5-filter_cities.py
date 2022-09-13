#!/usr/bin/python3
"""the `5-filter_cities` module
lists all the cities under the state, state is given as an argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT `name` FROM `cities` WHERE `state_id` \
                 in (SELECT `id` FROM `states` WHERE `name`=%s)", (argv[4], ))
    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))

    cur.close()
    conn.close()
