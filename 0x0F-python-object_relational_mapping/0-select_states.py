#!/usr/bin/python3
"""the `0-select_states.py` module
prints all the states found in the database
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `states.id`")
    rows = cur.fetchall()
    for row in rows:
        print(row)
