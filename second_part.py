# The second part of the semester's project
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

N = 1000

# Network topologies
regular = nx.random_regular_graph(4, N)
random = nx.gnp_random_graph(N, 0.25) # Returns a Gn,p random graph, also known as an Erdős-Rényi graph or a binomial graph
rand_geometric = nx.random_geometric_graph(N, 120, 100)
small_world = nx.watts_strogatz_graph(N, 4, 0.2)
scale_free = nx.barabasi_albert_graph(N, 2) # Generate a scale-free graph using the Barabási-Albert model

node_degrees = nx.degree(scale_free)



# Calculate the desired metrics
# Y = degree, X = node

y = []
x = []
for node, degree in node_degrees:
    x.append(node)
    y.append(degree)
    print(f"Node {node} has degree {degree}")


plt.plot(x, y)

plt.show()
