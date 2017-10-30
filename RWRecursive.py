# -*- coding: utf-8 -*-
"""
Created on Tue May 23 23:14:24 2017

@author: jamie
"""
import numpy as np
import matplotlib.pyplot as plt

n=6

PathsOld = np.zeros((2*n+3,2*n+3))
PathsNew = np.zeros((2*n+3,2*n+3))

#start (step 0)
PathsNew[n+1][n+1] = 1

for step in range(1,n):
    #Reassign
    PathsOld = PathsNew
    #Wipe New paths so the old data doesn't mess up the current data
    PathsNew = np.zeros((2*n+3,2*n+3))
    for i in range(1,2*n+1):
        for j in range(1,2*n+1):
            #look at surrounding blocks
            PathsNew[i][j] = PathsOld[i][j-1] + PathsOld[i][j+1] + PathsOld[i+1][j] + PathsOld[i-1][j]

probMat= PathsNew/(4**n)