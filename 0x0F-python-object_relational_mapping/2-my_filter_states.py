#!/usr/bin/python3
"""This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """To get all states from the database
    """
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    curs = con.cursor()
    curs.execute("SELECT * \
                FROM states \
                WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC").format(argv[4])

    for state in curs.fetchall():
        print(state)

    curs.close()
    con.close()
