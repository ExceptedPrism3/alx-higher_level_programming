#!/usr/bin/python3
"""
    Module connect to MySQL using MySQLdb Module
    – selects all states and filters by the fouth
    argument passed to script
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    query = '''SELECT cities.id, cities.name, states.name
                FROM cities LEFT JOIN states
                ON cities.state_id = states.id ORDER BY cities.id'''
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
