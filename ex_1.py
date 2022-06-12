import networkx as nx
import matplotlib.pyplot as plt
from future.utils import iteritems
from random import randint
import os
import math
import time
import csv

x = []
y = []
os.chdir("~/tsp")
with open('tsp_100.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

def distance(a1,b1,a2,b2):
    a = (a1-a2)**2
    b = (b1-b2)**2
    dis = math.sqrt(a+b)
    return dis
    
#print(distance(564,449,129,414))      
pos={}        
node_num=0

for i in range(len(x)):
    pos[node_num] = x[i], y[i]
    node_num+=1

X=nx.Graph()
X.add_nodes_from(pos.keys())
#X.clear()
print(node_num)
for n, p in iteritems(pos):
    X.nodes[n]['pos'] = p
    #print(p)
#nx.draw(X, pos)
#plt.show()


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
            #print("distance between ",value1," and ", value2," is ",value)
            X.add_weighted_edges_from([(i,j,value)])
#print(X[0][1]['weight'])           
nodelist = list(pos.keys())
visited_nodes = []
visited_edges = []
start = 0
infi = 999999
dest = 0
source = 0
t1 = time.clock()
while(not nodelist == False):
    if(len(nodelist)==0):
        visited_nodes.append(start)
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
print(visited_nodes)  
totaldist = 0  
for i in range(len(visited_nodes)-1):
    s = visited_nodes[i]
    d = visited_nodes[i+1]
    totaldist = totaldist + X[s][d]['weight']
print(totaldist)
print("Execution Time is :",time.clock()-t1)
#print(visited_edges)  
file = open('path_100.txt', 'w')
for i in visited_nodes:
    file.write(str(i)+"->")
file.close()
#print(X.edges)
#nx.draw(X, pos, with_labels = True)
#plt.show()