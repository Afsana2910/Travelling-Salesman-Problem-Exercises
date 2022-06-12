# Travelling Salesman Problem Exercises
The 'tsp' folder contains the files having the coordinates for 10,20,100 and 100 hypothetical cities.
Our goal is to find the shortest route through all cities (solve the TSP). Assume that there exists a direct road between any pair of cities (Euclidean distance; two points p1=(100,100), p2=(103,104) will have distance (p1, p2)=5 ).

**EX1:** Run the Nearest Neighbour (NN) algorithm to generate a route through all cities starting from any node (e.g. from node 0). Your route should also end in this node. If distances tie, choose the first city. Report the shortest tour and time it took to complete it for cities of size 10, 20 and 100. 

**EX2:** Implement a very simple 2-opt local search optimization technique using the same cities as in EX1. At first, create a random route through all cities. Then, pick two random nodes from your route: i and k. Preserve the original route until i-1 node, then insert nodes from i to k in the reverse order and finally add nodes from k+1 to the end of the route in the original order. If the resulting path is shorter than the original - accept the swap and reject the change otherwise. If you accept the change, in the next iteration use new path as the original. Repeat this operation many times. Report the final number of iterations and the number of successful swaps for each city from EX1. What is the shortest path and execution time for each city? How does it compare to the results produced by the Nearest Neighbour algorithm? Visualize resulting tours.

As an example for 2-opt, consider sequence of [0,1,2,3,4]. Let i = 1 and k = 3, then the resulting sequence after switch would be [0,3,2,1,4].

**EX3:** Use a tour produced by the Nearest Neighbour algorithm in EX1 as a starting point for 2-opt optimization. Report the resulting path, its length and total execution time (time for NN + time for 2-opt) for each city (sizes 10, 20 and 100). How the length of the resulting path compares to results from EX1 and EX2? Elaborate on this comparison.

**EX4:** Implement another optimization method of your choice (e.g. simulated annealing, genetic algorithm, ant colony optimization, hill climbing etc.) on provided cites (again, all, except 1000). As usual - report resulting path, its length, and execution time. Comment on comparison with previous methods.


**Exercise Credits**<br />
*Algorithmics Course<br />
Institute of Computer Science<br />
University of Tartu*
