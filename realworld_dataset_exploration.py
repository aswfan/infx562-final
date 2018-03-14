# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:21:10 2018

@author: Anthony Wang
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import preprocessing

import matplotlib.pyplot as plt

def rangeto_positive(data_pd):
    k=len(data_pd.columns)
    for i in range(0,k):
        data_pd.iloc[:,i]=(data_pd.iloc[:,i]-min(data_pd.iloc[:,i]))/max(data_pd.iloc[:,i])
    return data_pd


def rangeto_01(data_pd):
    k=len(data_pd.columns)
    for i in range(0,k):
        data_pd.iloc[:,i]=data_pd.iloc[:,i]/max(data_pd.iloc[:,i])
    return data_pd

data_pd=pd.read_csv("./data/Wholesale customers data.csv")

data_pd=data_pd.iloc[:,1:9]

data_norm_pd=(data_pd-data_pd.mean())/data_pd.std()

data_norm_pd_range01=rangeto_01(rangeto_positive(data_norm_pd))  

data_final=data_norm_pd.loc[:,"Fresh":"Delicassen"]

pca=PCA()

pca.fit(data_final)

data_transform=pd.DataFrame(pca.transform(data_final))

data_transform=data_transform.rename(columns={0:'PC1',1:'PC2',2:'PC3',3:'PC4',4:'PC5',5:'PC6'})

data_final.to_csv("data/Wholesale_customers_data_norm.csv",index=False)

data_transform.to_csv("data/Wholesale_customers_data_norm_pca.csv",index=False)


plt.scatter(data_transform.loc[:,5],data_transform.loc[:,4]) 

