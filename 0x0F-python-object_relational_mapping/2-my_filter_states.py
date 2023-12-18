#!/usr/bin/python3
# A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""
    2-my_filter_states
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """Code"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM `states` \
                WHERE `name` = '{}'".format(sys.argv[4]))

    for states in cur.fetchall():
        print(states)