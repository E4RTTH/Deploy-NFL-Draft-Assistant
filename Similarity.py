import pandas as pd
import numpy as np
qb_stats = pd.read_csv(r'data.csv',encoding= 'UTF-8')

#Similarity
from scipy.spatial.distance import euclidean,pdist,squareform
user_input = {'userinput from website'}
qb_drafted = qb_stats[qb_stats['y']==1].fillna(0)
euclidean_max = []

for i in range(0,len(qb_drafted.index)):
    euclidean_max.append(euclidean(user_input,i))

max(euclidean_max)