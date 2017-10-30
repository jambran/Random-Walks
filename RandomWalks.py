# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:07:12 2017

@author: jamie
"""
import numpy as np
import matplotlib.pyplot as plt


#%%
from numpy.random import random as rand
num_steps = 1000
Q = np.arange(1,5,1)

for a in Q:
    x_step = rand(num_steps) > .5
    y_step = rand(num_steps) > .5
    x_step = 2*x_step - 1
    y_step = 2*y_step - 1
    x_position = np.cumsum(x_step)
    y_position = np.cumsum(y_step)
     
    plt.subplot(2,2,a) #says make a 2x2 grid, put this graph in the first box.
    plt.plot(x_position, y_position)
    plt.axis([-50,50,-50,50])

#%%
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rand
num_steps = 4000
numWalks = 1000
Q = np.arange(0, numWalks, 1)
x_final = np.zeros(numWalks)
y_final = np.zeros(numWalks)
displacement = np.zeros(numWalks)
for i in Q:
    x_step = rand(num_steps)> .5
    y_step = rand(num_steps) > .5
    x_step = 2*x_step - 1
    y_step = 2*y_step - 1
    x_position = np.cumsum(x_step)
    y_position = np.cumsum(y_step)
    x_final[i] = x_position[-1]
    y_final[i] = y_position[-1]
    displacement[i] = np.sqrt(x_position[num_steps-1]**2 + y_position[num_steps-1]**2)
    
#a. Plot a scatter chart of final positions. 
plt.figure()
plt.scatter(x_final,y_final)

#b. Use plt. hist to make a histogram of the displacement values
plt.figure()
plt.hist(displacement)

#c. Make a historgram of the quantity displacement^2
plt.figure()
plt.hist(displacement**2)

#d. Your answer to (c) may inspire a guess as to the mathematical form of the historgram. 
#Try semilog and log-log axes to inspire and test your guess. 
#I bet it's a Poisson Distribution?   

#e. Use np.mean to find the average value of dislacement **2 (the mean-square displacement) for a random walk of 1000 steps.
np.mean(displacement**2)

#f. Find the mean-square displacement of a 4000-step walk. 
#If you wish to carry the analysis furhter, see if you can determine 
#how the mean-square displacement depends on the number of steps in a random walk.
#I got a mean of displacement squared of about 8000. 

#%%
#6.3 Rare Events

#a. plot the poisson distribution for lambda = .8
from scipy.special import factorial 
from numpy.random import random as rand

x_val = np.arange(0,25,1)
y_val = np.exp(-8)*(8**x_val) / factorial(x_val)
plt.figure()
plt.plot(x_val, y_val)

print(max(y_val))
#%%
#b.Simulate coin flips
from numpy.random import random as rand

trials = 1000000
Q = np.arange(0,trials, 1)
M =np.zeros(trials)

for i in Q:
    sample = rand(100)
    heads = (sample < .08)
    #c. M = num heads for each trial. 
    M[i] = np.sum(heads)

#d. Make a graph of the Poisson distribution multiplied by N. 
#What's the most probable outcome? 
#Graph this plot on the same axes as the histogram in c. 
x_val = np.arange(1,trials,1, float)
y_val = np.exp(-8)*(8**x_val)*trials / factorial(x_val)

plt.figure()
plt.hist(M, bins = 20)
plt.plot(x_val,y_val)

#The most probable outcome is the peak of the Poisson curve. 
#%%
