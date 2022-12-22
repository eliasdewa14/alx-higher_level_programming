#!/usr/bin/python3
"""This script takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """To get all states from the database
    """
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=argv[1], passwd=argv[2], dbname=argv[3])
    cur = con.cursor()
    cur.execute("SELECT cities.id, cities.name \
                FROM cities JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id", [argv[4]])
    for state in cur.fetchall():
        print(", ".join(state))
