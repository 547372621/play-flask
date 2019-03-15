#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import MySQLdb


con = MySQLdb.connect(
	host='ali',
	user='root',
	passwd='1234',
	port=3306,
	db='xhb',
	charset='utf8')

df = pd.read_sql("select * from log_size where dt = '20190308' order by create_time",con)
plt.plot(df['create_time'],df['file_size']/1024**3)
plt.show()

