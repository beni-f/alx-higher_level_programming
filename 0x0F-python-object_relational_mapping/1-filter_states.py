#!/usr/bin/python3
# A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

"""
    1-filter_states.py
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """List all states with a name starting with N"""

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%"')

    for states in cur.fetchall():
        print(states)

    cur.close()
    db.close()