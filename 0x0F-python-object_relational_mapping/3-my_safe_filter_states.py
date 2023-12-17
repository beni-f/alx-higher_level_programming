#!/usr/bin/python3
"""
    3-my_safe_filter_states.py
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """Code"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    for states in cur.fetchall():
        if states[1] == sys.argv[4]:    
            print(states)