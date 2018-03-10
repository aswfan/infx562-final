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

#and shift to range(0,1)
state['x']=state['x']-min(state['x'])
state['y']=state['y']-min(state['y'])
state['z']=state['z']-min(state['z'])   

state['x']=state['x']/max(state['x'])
state['y']=state['y']/max(state['y'])
state['z']=state['z']/max(state['z'])


#Create States_transform_data
data_ori=state

pca=PCA(n_components=3)

pca.fit(data_ori)

data_transform=pd.DataFrame(pca.transform(data_ori))

data_transform=data_transform.round(1)

#Reindex
state=state.reset_index()

data_transform.reindex()

data_ori=pd.concat([state,data_transform], axis=1)

#Rename col
data_ori=data_ori.rename(columns={'index':'label'})

#Add column step
data_ori["step"]=1
     
#add more dataset

data_ori_1=data_ori


#Second Round Dataset#######################################################################

#Create State data

data_3d=pd.DataFrame(np.array(range(101,116)),np.array(["a"]*15))

data_3d2=pd.DataFrame(np.array(range(31,46)),np.array(["b"]*15))

data_3d3=pd.DataFrame(np.array(range(1,16)),np.array(["c"]*15))

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

#and shift to range(0,1)
state['x']=state['x']-min(state['x'])
state['y']=state['y']-min(state['y'])
state['z']=state['z']-min(state['z'])   

state['x']=state['x']/max(state['x'])
state['y']=state['y']/max(state['y'])
state['z']=state['z']/max(state['z'])

#Create States_transform_data
data_ori=state

pca=PCA(n_components=3)

pca.fit(data_ori)

data_transform=pd.DataFrame(pca.transform(data_ori))

#plt.scatter(data_transform.loc[:,0],data_transform.loc[:,1]) 

data_transform=data_transform.round(1)

#Reindex
state=state.reset_index()

data_transform.reindex()

data_ori=pd.concat([state,data_transform], axis=1)

#Rename col
data_ori=data_ori.rename(columns={'index':'label'})

#Add column step
data_ori["step"]=2
#add more dataset

data_ori_2=data_ori


#Third Round Dataset#######################################################################

#Create State data

data_3d=pd.DataFrame(np.array(range(1,16)),np.array(["a"]*15))

data_3d2=pd.DataFrame(np.array(range(111,126)),np.array(["b"]*15))

data_3d3=pd.DataFrame(np.array(range(51,66)),np.array(["c"]*15))

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

#and shift to range(0,1)
state['x']=state['x']-min(state['x'])
state['y']=state['y']-min(state['y'])
state['z']=state['z']-min(state['z'])   

state['x']=state['x']/max(state['x'])
state['y']=state['y']/max(state['y'])
state['z']=state['z']/max(state['z'])

#Create States_transform_data
data_ori=state

pca=PCA(n_components=3)

pca.fit(data_ori)

data_transform=pd.DataFrame(pca.transform(data_ori))

#plt.scatter(data_transform.loc[:,0],data_transform.loc[:,1]) 

data_transform=data_transform.round(1)

#Reindex
state=state.reset_index()

data_transform.reindex()

data_ori=pd.concat([state,data_transform], axis=1)

#Rename col
data_ori=data_ori.rename(columns={'index':'label'})

#Add column step
data_ori["step"]=3
#add more dataset

data_ori_3=data_ori


#Fourth Round Dataset#######################################################################

#Create State data

data_3d=pd.DataFrame(np.array(range(21,36)),np.array(["a"]*15))

data_3d2=pd.DataFrame(np.array(range(61,76)),np.array(["b"]*15))

data_3d3=pd.DataFrame(np.array(range(91,106)),np.array(["c"]*15))

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

#and shift to range(0,1)
state['x']=state['x']-min(state['x'])
state['y']=state['y']-min(state['y'])
state['z']=state['z']-min(state['z'])   

state['x']=state['x']/max(state['x'])
state['y']=state['y']/max(state['y'])
state['z']=state['z']/max(state['z'])

#Create States_transform_data
data_ori=state

pca=PCA(n_components=3)

pca.fit(data_ori)

data_transform=pd.DataFrame(pca.transform(data_ori))

#plt.scatter(data_transform.loc[:,0],data_transform.loc[:,1]) 

data_transform=data_transform.round(1)

#Reindex
state=state.reset_index()

data_transform.reindex()

data_ori=pd.concat([state,data_transform], axis=1)

#Rename col
data_ori=data_ori.rename(columns={'index':'label'})

#Add column step
data_ori["step"]=4
#add more dataset

data_ori_4=data_ori

#plot
plt.scatter(data_ori_1.loc[:,0],data_ori.loc[:,1]) 
#Save all data

#Combine and save
data_final=pd.concat([data_ori_1,data_ori_2,data_ori_3,data_ori_4])
data_final.to_csv("data/3data.csv")



