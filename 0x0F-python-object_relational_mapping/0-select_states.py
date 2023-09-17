#!/usr/bin/env python3
"""Module uses mysqldb orm to query database"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    result = cursor.fetchall()
    for row in result:
        print(row)
