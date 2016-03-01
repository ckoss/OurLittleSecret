# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 21:56:00 2016

@author: ChrisX
"""

path='C:/Users/ChrisX/Desktop/workfolder/'

f = open(path+'history.csv', "rU");
data=[line.replace('\n','') for line in f]
f.close()

array=[line.split(',') for line in data]
del array[0]

mid=[line[0] for line in array]
pid=[line[1] for line in array]
name=[line[2] for line in array]
role=[line[3] for line in array]
stat1=[line[4] for line in array]
stat2=[line[5] for line in array]
stat3=[line[6] for line in array]
stat4=[line[7] for line in array]
points=[line[8] for line in array]
won=[line[9] for line in array]
teamcolor=[line[10] for line in array]
duration=[line[11] for line in array]


timetest=[]
for line in array:
    if line[4]=='0' and line[5]=='0' and line[6]=='0':
        time=line[-1].split(':')
        time=int(time[1])*60+int(time[2])
        timetest.append((line[8], time))

        
        
import matplotlib.pyplot as plt

plt.scatter(*zip(*timetest))
plt.show()