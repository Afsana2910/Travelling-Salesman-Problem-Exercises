import networkx as nx
import matplotlib.pyplot as plt
from future.utils import iteritems
from random import randint
import os
import math
import random
import time
import csv

x = []
y = []
os.chdir("~/tsp")
with open('tsp_10.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

def distance(a1,b1,a2,b2):
    a = (a1-a2)**2
    b = (b1-b2)**2
    dis = math.sqrt(a+b)
    return dis
    
  
pos={}        
node_num=0

for i in range(len(x)):
    pos[node_num] = x[i], y[i]
    node_num+=1

X=nx.Graph()
X.add_nodes_from(pos.keys())

for n, p in iteritems(pos):
    X.nodes[n]['pos'] = p


print(pos)
for i in (X.nodes):
    value1 = X.nodes[i]['pos']
    x1 = value1[0]
    y1 = value1[1]
    for j in (X.nodes):
        value2 = X.nodes[j]['pos']
        x2 = value2[0]
        y2 = value2[1]
        
        if(i!=j):
            value = distance(x1,y1,x2,y2)
           
            X.add_weighted_edges_from([(i,j,value)])

t1 = time.clock()
#-----------------------------NN Neighbor---------------------------
nodelist = list(pos.keys())
visited_nodes = []
visited_edges = []
start = 0
infi = 999999
dest = 0
source = 0
while(not nodelist == False):
    if(len(nodelist)==0):
        #visited_nodes.append(start)
        visited_edges.append((source,start))
        break
    mindist = infi
    #print("source is ",source)
    visited_nodes.append(source)
 
    nodelist.remove(source)
    for i in nodelist:
        w = X[source][i]['weight']
        #print("distance ",source," and ",i," is ",w)
        if(w<mindist):
            dest = i
            #print(i)
            mindist = w
    if(source!=dest):
        visited_edges.append((source,dest))
    #print("distance ",source," and ",i," is ",w)
    source = dest

    #print(dest)
#print(visited_nodes)  
totaldist = 0  
"""for i in range(len(visited_nodes)-1):
    s = visited_nodes[i]
    d = visited_nodes[i+1]
    totaldist = totaldist + X[s][d]['weight']
print(totaldist)"""

#--------------------------2-OPT------------------------------------
#print(visited_nodes)


for i in range(len(visited_nodes)-1):
    s = visited_nodes[i]
    d = visited_nodes[i+1]
    totaldist = totaldist + X[s][d]['weight']
mindist = totaldist


counter = 0
swaps = 0
temp = visited_nodes[:]


while(counter<100000):
 
    #print(resultpath)
    temp = visited_nodes[:]
   
    rn = random.sample(range(1, 9), 2)
    rn[0] = temp.index(rn[0])
    rn[1] = temp.index(rn[1])
    #print(rn)
    if(rn[0]<rn[1]):
        begin = rn[0]
        end = rn[1]
    else:
        begin = rn[1]
        end = rn[0]
    temp[begin:end+1] = reversed(temp[begin:end+1])
    totaldistnew = 0 
    for i in range(len(temp)-1):
        
        s = temp[i]
        d = temp[i+1]
        totaldistnew = totaldistnew + X[s][d]['weight']
    if(totaldistnew<mindist):
        
        visited_nodes = temp[:]
        mindist = totaldistnew
        swaps = swaps +1
    counter = counter +1
    
#print("Execution Time ", time.clock()-t1)
mindist = mindist + X[visited_nodes[len(visited_nodes)-1]][0]['weight']
#print(visited_nodes,mindist)
#print("Number of swaps ", swaps)



file = open('ex3_10.txt', 'w')
for i in visited_nodes:
    file.write(str(i)+"->")
file.close()
file = open('ex31_10.txt', 'w')
for i in visited_nodes:
    file.write(str(i)+"\n")
file.close()

