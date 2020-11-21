import pandas as pd
import numpy as np
qb_stats = pd.read_csv(r'data.csv',encoding= 'UTF-8')

#Recomendation
user_input = {'userinput from website'}
qb_drafted = qb_stats[qb_stats['y']==1]

mean_stat = {}
for i in qb_drafted.columns:
    x = qb_drafted[[i]].mean(axis=1)
    qb_drafted[i] = x

for a in mean_stat.keys:
    if a in ['40yd','3Cone'.'Shuttle']:
        if user_input[a] > mean_stat[a]:
            print('Your {} status is too high'.format(a))
        if user_input[a] < mean_stat[a]:
            print('Your {} status is too low'.format(a))
