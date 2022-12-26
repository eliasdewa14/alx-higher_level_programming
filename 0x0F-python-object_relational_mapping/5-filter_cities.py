#!/usr/bin/python3
"""This script takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
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
    curs.execute("SELECT cities.id, cities.name \
                FROM cities JOIN states ON cities.state_id = states.id \
                WHERE name LIKE BINARY %(state_name)s \
                ORDER BY cities.id ASC", {'state_name': argv[4]})

    for state in curs.fetchall():
        print(", ".join(state))

    curs.close()
    con.close()
