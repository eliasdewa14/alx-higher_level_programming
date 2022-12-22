#!/usr/bin/python3
"""This script takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time,
it is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """To get all states from the database
    """
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=argv[1], passwd=argv[2], dbname=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * \
                FROM states \
                WHERE Name = %s \
                ORDER BY states.id", [argv[4]])
    for state in cur.fetchall():
        print(state)
