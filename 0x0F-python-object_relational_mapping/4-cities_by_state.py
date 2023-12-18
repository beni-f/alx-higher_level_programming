#!/usr/bin/python3
# A script that lists all cities from the database hbtn_0e_4_usa
"""
    4-cities_by_state
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """
        Code
    """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name`\
                 FROM `cities` as `c`\
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id`\
                ")

    for cities in cur.fetchall():
        print(cities)