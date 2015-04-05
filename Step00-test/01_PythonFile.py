# Remember: comments in python are denoted by the pound sign
import numpy as np                 #here we load numpy, calling it 'np' from now on
import matplotlib.pyplot as plt    #here we load matplotlib, calling it 'plt'
import time, sys                   #and load some utilities
#from IPython.core.display import clear_output #used for inline animation

#this makes matplotlib plots appear in the notebook (instead of a separate window)
%matplotlib inline 

nx = 41  # try changing this number from 41 to 81 and Run All ... what happens?
dx = 2./(nx-1)
nt = 25    #nt is the number of timesteps we want to calculate
dt = .025  #dt is the amount of time each timestep covers (delta t)
c = 1.      #assume wavespeed of c = 1

u = np.ones(nx)      #numpy function ones()
u[.5/dx : 1/dx+1]=2  #setting u = 2 between 0.5 and 1 as per our I.C.s
print(u)

plt.plot(np.linspace(0,2,nx), u);

