from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import xgboost as xgb
from scipy.spatial.distance import euclidean,pdist,squareform

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('NFL Draft Assistant.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      data = pd.read_csv(r'data.csv')
      drafted = data[data['y'] == 1]
      table = drafted.drop(columns = ['y'])
      table.set_index('Player')
      user_input = [request.form[i] for i in table.columns]
      filename = 'nfl.model'
      clf = xgb.Booster({'nthread': 4})
      clf.load_model('nfl.model')
      X_test = np.array([user_input]).astype(np.float64)
      draft_assisstant = clf.predict(X_test)
      if draft_assisstant in [1]:
         similarity = [euclidean(user_input,i) for i in range(0,len(table.index)]
         table_similar = table.insert(4,column = ['Similarity'],similarity) 
         table_similar[table_similar['Similarity'] is min].index()
      elif draft_assisstant in [0]:
         mean_stat = {}
         for i in table.columns:
            x = qb_drafted[[i]].mean(axis=1)
            qb_drafted[i] = x
         for a in mean_stat.keys:
            if a in ['40yd','3Cone'.'Shuttle']:
               if user_input[a] > mean_stat[a]:
                  print('Your {} status is too high'.format(a))
               if user_input[a] < mean_stat[a]:
                  print('Your {} status is too low'.format(a))
                 
      return jsonify(result=price.tolist())
      
if __name__ == '__main__':
   app.run()