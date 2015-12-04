# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 07:32:36 2015

@author: jordanvarghese
"""

from numpy import copy, zeros, linspace
import time, sys
from pylab import plot
from matplotlib import pyplot, animation
from math import sin,pi

#Set initial parameters
xlen = 10  #looking at a distance of 4 units
num_pos = 101 #there are 101 positions were are studying
x_dis = xlen/(num_pos-1) #distance between each position
num_timesteps = 50 #how many times steps we will study
timestep = .05 #duration of a timestep
c =1 #waveform speed
print (x_dis)

#Set Initial conditions

u = zeros (num_pos)
#creating triangle waveform
wflen = 2  #setting length of waveform
u[wflen/2/x_dis:wflen/x_dis] = 1
print (u)   
pyplot.plot (linspace(0,xlen,num_pos),u)
ylim (0,2) 

#Solve Linear Convection Equation for  this waveform initial condition

udum = zeros(num_pos)     #create dummy array for solution of differential equation

for i in range (num_timesteps):
    udum = u.copy()
    for k in range (1,num_pos):
        u[k] = udum[k] - udum[k] * (timestep/x_dis) * (udum[k]-udum[k-1])  #FD in time , #BD in space
pyplot.plot (linspace(0,xlen,num_pos),u) 