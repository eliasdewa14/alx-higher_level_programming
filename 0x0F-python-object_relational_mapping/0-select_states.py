#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """To get all states from the database
    """
    con = MySQLdb.connect(host="localhost",
                          port=3306,
                          user=argv[1],
                          passwd=argv[2],
                          db=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * \
                FROM states \
                ORDER BY states.id ASC")

    for data in cur.fetchall():
        print(data)

    cur.close()
    con.close()
