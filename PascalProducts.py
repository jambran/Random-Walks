# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:40:10 2017

@author: jamie
"""
import numpy as np
import matplotlib.pyplot as plt

#%%
def triangle(rows):

    for rownum in range (rows):
        newValue = 1
        PrintingList = [newValue]
        for iteration in range (rownum):
            newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
            PrintingList.append(int(newValue))
        print(PrintingList)
    print()


#%%
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def PasLine(n):
    line = []
    for r in range(0,n+1):
        line.append(nCr(n,r))
    return line
    

#%%

#def prob(n):
n = 4
array = PasLine(n)
Matrix = np.zeros((n+1,n+1)) #initialize matrix

Matrix[0] = PasLine(n)      #fill first row with Pascal Line

for i in range(n+1):
    Matrix[i,0] = array[i]  #Fill first column with Pascal Line
    
    for i in range(1,n+1):      #Start taking products
        for j in range (1,n+1):
            if i+j >= n+1:     #if it's past the diag, fill it with 0
                Matrix[i,j] = 0
            else:
                Matrix[i,j] = Matrix[i,0] * Matrix[0,j]

goodPaths = np.zeros((n+1, n+1))
for i in range(0,n+1):      
    for j in range (0,n+1):
        goodPaths[i,j] = Matrix[i,j]

for i in range(1,n+1):      #
    for j in range (1,n+1):
            goodPaths[i,j] = Matrix[i,j] - Matrix[i-1,j-1]
            if goodPaths[i,j] < 0:
                goodPaths[i,j] = 0

prob = np.sum(goodPaths)/(4**n)
print(prob)
    #return prob
#%%
def probLeaveOrigin(n):
    #n = 4
    array = PasLine(n)
    Matrix = np.zeros((n+1,n+1))    # Initialize matrix
    
    Matrix[0] = PasLine(n)          # Fill first row with Pascal Line
    
    for i in range(n+1):
        Matrix[i,0] = array[i]      # Fill first column with Pascal Line
        
        for i in range(1,n+1):      # Start taking products
            for j in range (1,n+1):
                if i+j >= n+1:      # if it's past the diag, fill it with 0
                    Matrix[i,j] = 0
                else:
                    Matrix[i,j] = Matrix[i,0] * Matrix[0,j]
    
    goodPaths = np.zeros((n+1, n+1))
    for i in range(0,n+1):      
        for j in range (0,n+1):
            goodPaths[i,j] = Matrix[i,j]
    
    for i in range(1,n+1):
        for j in range (1,n+1):
                goodPaths[i,j] = Matrix[i,j] - Matrix[i-1,j-1]
                if goodPaths[i,j] < 0:
                    goodPaths[i,j] = 0
    
    #find the middle term 
    if(n % 2 == 0):                 # if it's possible to be at (0,1)
        numPaths = goodPaths[n/2,n/2]
    else: 
        numPaths = 0
    return numPaths/(4**n)/4
    

plt.figure()
sumThis = []
sumArray =[]
for t in range(1,200):
    #print(probLeaveOrigin(t))
    sumThis.append(probLeaveOrigin(t-1))
    sumArray.append(np.sum(sumThis))
    plt.scatter(t+1, sumArray[t-1])
    plt.xlabel("Time Steps")
    plt.ylabel("Prob to remain in Upper Half Plane")
    #plt.scatter(t+1, probLeaveOrigin(t))
    plt.grid()
plt.show()

    

