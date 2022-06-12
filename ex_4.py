from satsp import solver
import os
import math
import time
import csv

x = []
y = []
nodes = []
node_num = -1
os.chdir("~/tsp")
with open('tsp_1000.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        node_num = node_num + 1
        nodes.append(node_num)
        x.append(int(row[0]))
        y.append(int(row[1]))

cities=[]
t1 = time.clock()
for i in range(len(nodes)):
   
    l = [nodes[i],x[i],y[i]]
    cities.append(l)

solver.Solve(cities)
solver.PrintSolution()
print("Execution Time is ",time.clock()-t1)