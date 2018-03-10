# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:00:10 2018

@author: Anthony Wang
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import string

#Create State data

state=pd.DataFrame(np.array(range(1,13)))


#Use the x1 to get x2
def calculate_y(row):
    return row[0] * 3 +np.random.random()*row[0]

state['y']=state.apply(calculate_y, axis=1)

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

#Create States_transform_data
data_ori=state

pca=PCA(n_components=2)

pca.fit(data_ori.loc[:,["x","y"]])

data_transform=pd.DataFrame(pca.transform(data_ori.loc[:,["x","y"]]))

data_ori['pc1']=data_transform[0]
data_ori['pc2']=data_transform[1]

data_ori['id']=np.array(list(string.ascii_lowercase)[0:12])

#Get var after transform
#Get varpc1
mean_pc1=np.mean(data_ori['pc1'])
def calculate_var(row):
    return row['pc1']-mean_pc1

data_ori['varpc1']=state.apply(calculate_var,axis=1)

#Get varpc2
mean_pc2=np.mean(data_ori['pc2'])
def calculate_var(row):
    return row['pc2']-mean_pc2

data_ori['varpc2']=state.apply(calculate_var,axis=1)

data_ori=data_ori.round(1)

data_ori.to_csv("data/states.csv")


#SVD method
#u, s, vh = np.linalg.svd(data_ori.values.T, full_matrices=False)


