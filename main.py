# The second part of the semester's project
import networkx as nx
import matplotlib.pyplot as plt

N = 140


# GENERATE THE NETWORK TOPOLOGY
# ADD THAT GENERATED GRAPH AND ITS NAME TO A 2D LIST 
# BECAUSE THE TOPOLOGY'S NAME ITS NEEDED IN ORDER TO SET A MEANINGFUL TITLE OF ITS PLOT 
networks = []
# Network topologies
regular = nx.random_regular_graph(4, N)
row = [regular, "Regular"]
networks.append(row)
random = nx.gnp_random_graph(N, 0.25) # Returns a Gn,p random graph, also known as an Erdős-Rényi graph or a binomial graph
row = [random, "Random"]
networks.append(row)
rand_geometric = nx.random_geometric_graph(N, 120, 100)
row = [rand_geometric, "Random Geometric"]
networks.append(row)
small_world = nx.watts_strogatz_graph(N, 4, 0.2)
row = [small_world, "Small World"]
networks.append(row)
scale_free = nx.barabasi_albert_graph(N, 2) # Generates a scale-free graph using the Barabási-Albert model
row = [scale_free, "Scale Free"]
networks.append(row)


def calc_node_degree(network,axes):
      node_degrees = nx.degree(network[0]) # calculates and the degree of each node
      y = []
      x = []
      for node, degree in node_degrees:
            x.append(node)
            y.append(degree)
      axes.plot(x, y)
      axes.set_title(network[1])


fig, axs = plt.subplots(3, 2) # 3 rows, 2 columns
row = 1
column = 1
for network in networks:
      calc_node_degree(network, axs[row - 1, column - 1])
      if column % 2 == 0:
            row += 1
            column -= 1
      else :
            column += 1
fig.tight_layout() # padding between the subplots
plt.show()

