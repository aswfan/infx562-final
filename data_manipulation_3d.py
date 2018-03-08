# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:47:10 2018

@author: Anthony Wang
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#Create State data

data_3d=pd.DataFrame(np.array(range(1,16)),np.array(["a"]*15))

data_3d2=pd.DataFrame(np.array(range(51,66)),np.array(["b"]*15))

data_3d3=pd.DataFrame(np.array(range(101,116)),np.array(["c"]*15))

state=data_3d3.append(data_3d.append(data_3d2))

#Rename col
state=state.rename(columns={0:'x'})

#Normalize

state=(state-state.mean())/state.std()    



#Use the x1 to get x2
def calculate_y(row):
    return row[0] * 3 +np.random.random()*row[0]

state['y']=state.apply(calculate_y, axis=1)

#Use the x1 to get x3
def calculate_y(row):
    return row[0] * 2 -np.random.random()*5

state['z']=state.apply(calculate_y, axis=1)

'''
#Get varx
mean_x=np.mean(state[0])
def calculate_var(row):
    return row[0]-mean_x

state['varx']=state.apply(calculate_var,axis=1)

#Get vary
mean_y=np.mean(state['y'])
def calculate_var(row):
    return row['y']-mean_y

state['vary']=state.apply(calculate_var,axis=1)

#Rename col
state=state.rename(columns={0:'x'})
'''

#Create States_transform_data
data_ori=state

pca=PCA(n_components=3)

pca.fit(data_ori)

data_transform=pd.DataFrame(pca.transform(data_ori))

#data_ori['id']=np.array(list(string.ascii_lowercase)[0:12])

#Get var after transform
#Get varpc1
'''
mean_pc1=np.mean(data_ori['pc1'])
def calculate_var(row):
    return row['pc1']-mean_pc1

data_ori['varpc1']=state.apply(calculate_var,axis=1)

#Get varpc2
mean_pc2=np.mean(data_ori['pc2'])
def calculate_var(row):
    return row['pc2']-mean_pc2

data_ori['varpc2']=state.apply(calculate_var,axis=1)
'''

plt.scatter(data_transform.loc[:,0],data_transform.loc[:,1]) 

data_transform=data_transform.round(1)

state=state.reset_index()
data_transform.reindex()

data_ori=pd.concat([state,data_transform], axis=1)

#Rename col
data_ori=data_ori.rename(columns={'index':'label'})


data_ori.to_csv("data/3data.csv")
