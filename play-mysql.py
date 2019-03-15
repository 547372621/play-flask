#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb
from MySQLdb.cursors import DictCursor
con = MySQLdb.connect(
    host='ali',
    user='root',
    passwd='1234',
    port=3306,
    db='xhb',
    charset='utf8',
    cursorclass=DictCursor
)

cursor = con.cursor()
cursor.execute('SELECT * FROM `xhb` limit 1')
rest = cursor.fetchone()
cursor.close()
print(rest)
