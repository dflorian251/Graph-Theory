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
      degrees = dict(network[0].degree())
      degree_values = list(degrees.values())
      max_degree = max(degree_values)
      bins = range(0, max_degree + 2, 1)  # Define bins from 0 to max_degree + 1
      # Count the number of nodes in each bin
      degree_counts = [degree_values.count(degree) for degree in bins]
      axes.bar(bins, degree_counts, width=0.8, align='center')
      axes.set_title(network[1])


def calc_avg_shortest_path(network):
      return nx.average_shortest_path_length(network[0])


def calc_cc(network, axes):
      bins = [0.1 * i for i in range(11)] 
      clustering_coeffs = nx.clustering(network[0])
      cluster_coeff_counts = [sum(1 for cc in clustering_coeffs.values() if bin_val <= cc < bin_val + 0.1) for bin_val in bins]
      axes.bar(bins, cluster_coeff_counts, width=0.1, align='edge')
      axes.set_title(network[1])
            

def calc_closeness_centrality(network, axes):
      closeness_centrality = nx.closeness_centrality(network[0])
      axes.bar(closeness_centrality.keys(), closeness_centrality.values())
      axes.set_title(network[1])


def calc_betweenness_centrality(network, axes):
      betweenness_centrality = nx.betweenness_centrality(network[0])
      axes.bar(betweenness_centrality.keys(), betweenness_centrality.values())
      axes.set_title(network[1])


def calc_eigenvector_centrality(network, axes):
      eigenvector_centrality = nx.eigenvector_centrality(network[0], max_iter=500)
      axes.bar(eigenvector_centrality.keys(), eigenvector_centrality.values())
      axes.set_title(network[1])


fig, axs = plt.subplots(3, 2) # 3 rows and 2 columns
fig.suptitle("Degree Distribution")
fig2, axs2 = plt.subplots(3, 2)
# fig2.suptitle("Clustering Coefficient Distribution")
row = 1
column = 1
for network in networks:
      calc_node_degree(network, axs[row - 1, column - 1])
      calc_eigenvector_centrality(network, axs2[row - 1, column - 1])
      print(f"{network[1]} average shortest path: {calc_avg_shortest_path(network)}")
      if column % 2 == 0:
            row += 1
            column -= 1
      else :
            column += 1

fig.delaxes(axs[2, 1])
fig2.delaxes(axs2[2, 1])
fig.tight_layout() # padding between the subplots
fig2.tight_layout()
plt.show()

