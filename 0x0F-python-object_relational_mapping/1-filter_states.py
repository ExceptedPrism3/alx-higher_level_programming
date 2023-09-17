#!/usr/bin/python3
"""
    Module connect to MySQL using MySQLdb Module
    – selects all states but filters by names
    starting with N using MySQL regex operator
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute(
        '''SELECT * FROM states WHERE states.name
        LIKE BINARY 'N%' ORDER BY states.id'''
    )
    result = cursor.fetchall()
    for row in result:
        print(row)
