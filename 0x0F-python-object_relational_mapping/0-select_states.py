#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states")

    states = c.fetchall()
    for i in states:
        print(i)
    # Clean up process
    c.close()
    db.close()
