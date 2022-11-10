# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:14:08 2022

@author: st4r4x
"""
x = list(range(0, 100))
y = []
traj = []
for i in x:
    y.append(-((i)**2)-2*i+1000)
    traj.append([x[i], y[i]])
