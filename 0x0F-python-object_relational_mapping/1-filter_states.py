#!/usr/bin/python3
"""This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
        dbname=argv[3])

    curs = con.cursor()
    curs.execute("SELECT * \
                FROM states \
                WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    for state in curs.fetchall():
        print(state)

    curs.close()
    con.close()
