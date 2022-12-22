#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """To get all states from the database
    """
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=argv[1], passwd=argv[2], dbname=argv[3])
    cur = con.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states \
                WHERE cities.state_id = states.id \
                ORDER BY cities.id")
    for state in cur.fetchall():
        print(state)
