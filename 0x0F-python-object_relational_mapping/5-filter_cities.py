#!/usr/bin/python3
# A script that takes in the name of a state as an argument and 
# lists all cities of that state, using the database hbtn_0e_4_usa
"""
    5-filter_cities.py
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """
        Code
    """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM `cities` as `c`\
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id`\
                ")
    out = []
    for cities in cur.fetchall():
        if cities[4] == sys.argv[4]:
            out.append(cities[2])
    
    print(', '.join(out))

    cur.close()
    db.close()