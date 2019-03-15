#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('aaa.txt')
p = df.groupby(['dt','time'])
print(p)
u = p.unstack(0)
print(u)
