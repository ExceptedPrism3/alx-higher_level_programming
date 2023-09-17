#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name searched (str)

"""

import sys
import MySQLdb

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    searched_name = sys.argv[4]

    db = MySQLdb.connect(user=usr, passwd=pwd, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
                .format(searched_name))
    rows = cur.fetchall()

    for row in rows:
        print(row)
