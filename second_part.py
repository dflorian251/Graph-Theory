# The second part of the semester's project
import networkx as nx
import matplotlib.pyplot as plt

N = 140

regular = nx.random_regular_graph(4, N)
random = nx.gnp_random_graph(N, 0.25) # Returns a Gn,p random graph, also known as an Erdős-Rényi graph or a binomial graph
rand_geometric = nx.random_geometric_graph(N, 120, 100)
small_world = nx.watts_strogatz_graph(N, 4, 0.2)
scale_free = nx.barabasi_albert_graph(N, 5) # Generate a scale-free graph using the Barabási-Albert model

nx.draw(scale_free, with_labels=True, node_color='skyblue', font_size=12)

# Display the graph
plt.show()
