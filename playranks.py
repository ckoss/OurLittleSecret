# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 00:28:20 2016

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
team=[line[10] for line in array]
duration=[line[11] for line in array]



player_and_id={}
for line in array:
    player_and_id[line[1]]=line[2]


id_l=len(list(set(mid)))
ids=list(set(pid))

winners=[line[1] for line in array if line[9]=="won match"]
losers=[line[1] for line in array if line[9]=="lost match"]

from collections import Counter
wins=Counter(winners)
lose=Counter(losers)

stats=[(n, wins[n]+lose[n], wins[n], lose[n] ) for n in ids]
stats=sorted(stats, key=lambda stat: stat[1], reverse=True)

save=[line[0]+','+player_and_id[line[0]]+','+str(line[1])+','+str(line[2])+','+str(line[3])+'\n' for line in stats]
save[-1]=save[-1][:-1]

f = open(path+"playranks.txt", "w");
line = f.writelines( save )
f.close() 