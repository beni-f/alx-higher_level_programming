#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
"""
    0-select_states
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
        list all states from the database
    """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    for states in cur.fetchall():
        print(states)

    cur.close()
    db.close()
    
