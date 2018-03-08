# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:21:10 2018

@author: Anthony Wang
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import string
from sklearn import preprocessing

import matplotlib.pyplot as plt

data_pd=pd.read_csv("./data/Wholesale customers data.csv")

data_norm_pd=(data_pd-data_pd.mean())/data_pd.std()    

data_final=data_norm_pd.loc[:,"Fresh":"Delicassen"]

pca=PCA()

pca.fit(data_final)

data_transform=pd.DataFrame(pca.transform(data_final))


plt.scatter(data_transform.loc[:,5],data_transform.loc[:,4]) 

