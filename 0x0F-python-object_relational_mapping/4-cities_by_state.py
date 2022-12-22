#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa
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
    curs.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")

    for state in curs.fetchall():
        print(state)

    curs.close()
    con.close()
