import networkx as nx
import matplotlib.pyplot as plt


N = 140

class Figure:
      def __init__(self):
            self.fig, self.axs = plt.subplots(3, 2, squeeze=False)     # 3 rows and 2 columns
            self.fig.delaxes(self.axs[2, 1])
            
      def plot(self):
            pass


class FigureDegree(Figure):
      def __init__(self):
            super().__init__()      # We should always call the parent's contructor

      def plot(self, degrees, row, column, title):
            degree_values = list(degrees.values())
            max_degree = max(degree_values)
            bins = range(0, max_degree + 2, 1)  # Define bins from 0 to max_degree + 1
            # Count the number of nodes in each bin
            degree_counts = [degree_values.count(degree) for degree in bins]
            self.fig.suptitle("Node Degree")
            self.axs[row, column].bar(bins, degree_counts, width=0.8, align='center')
            self.axs[row, column].set_title(title)
            self.fig.tight_layout()
            

class FigureCC(Figure):
      def __init__(self):
            super().__init__()      # We should always call the parent's contructor

      def plot(self, clustering_coeffs, row, column, title):
            bins = [0.1 * i for i in range(11)] 
            cluster_coeff_counts = [sum(1 for cc in clustering_coeffs.values() if bin_val <= cc < bin_val + 0.1) for bin_val in bins]
            self.fig.suptitle("Clustering Coefficient")
            self.axs[row, column].bar(bins, cluster_coeff_counts, width=0.1, align='edge')
            self.axs[row, column].set_title(title)
            self.fig.tight_layout()
            

class FigureClosenessCentr(Figure):
      def __init__(self):
            super().__init__()

      def plot(self, closeness_centrality, row, column, title):
            self.fig.suptitle("Closeness Centrality")
            self.axs[row, column].bar(closeness_centrality.keys(), closeness_centrality.values())
            self.axs[row, column].set_title(title)
            self.fig.tight_layout()


class FigureBetweennessCentr(Figure):
      def __init__(self):
            super().__init__()

      def plot(self, betweenness_centrality, row, column, title):
            self.fig.suptitle("Betweenness Centrality")
            self.axs[row, column].bar(betweenness_centrality.keys(), betweenness_centrality.values())
            self.axs[row, column].set_title(title)
            self.fig.tight_layout()      


class FigureEigenvectorCentr(Figure):
      def __init__(self):
            super().__init__()

      def plot(self, eigenvector_centrality, row, column, title):
            self.fig.suptitle("Eigenvector Centrality")
            self.axs[row, column].bar(eigenvector_centrality.keys(), eigenvector_centrality.values())
            self.axs[row, column].set_title(title)
            self.fig.tight_layout()  


class FigureDiagrams(Figure):
      def __init__(self):
            super().__init__()
      
      def plot(self, network, row, column, title):
            self.fig.suptitle("Networks Diagrams")
            pos = nx.circular_layout(network)
            nx.draw(network, pos=pos, with_labels= True, ax= self.axs[row, column])
            self.axs[row, column].set_title(title)
            self.fig.tight_layout()


class NetworkTopology:
      def __init__(self, name, network):
            self.name = name
            self.network = network


      def calc_degree_distribution(self):
            degrees = dict(self.network.degree())
            return degrees
            
      def calc_avg_shortest_path(self):
            return nx.average_shortest_path_length(self.network)

      def calc_cc(self):
            return nx.clustering(self.network)

      def calc_closeness_centrality(self):
            return nx.closeness_centrality(self.network)


      def calc_betweenness_centrality(self):
            return nx.betweenness_centrality(self.network)

      def calc_eigenvector_centrality(self):
            return nx.eigenvector_centrality(self.network, max_iter=500)
     

class Regular(NetworkTopology):
      def __init__(self, degree, nodes):
            super().__init__("Regular", network= nx.random_regular_graph(degree, nodes))


class Random(NetworkTopology):
      def __init__(self, probability, nodes):
            super().__init__("Random", network= nx.gnp_random_graph(nodes, probability))


class RandomGeometric(NetworkTopology):
      def __init__(self, radius, dimension, nodes):
            super().__init__("Random Geometric", network= nx.random_geometric_graph(nodes, radius, dimension))


class SmallWorld(NetworkTopology):
      def __init__(self, degree, probability, nodes):
            super().__init__("Small World", network= nx.watts_strogatz_graph(nodes, degree, probability))


class ScaleFree(NetworkTopology):
      def __init__(self, edges_attach, nodes):
            super().__init__("Scale Free", network= nx.barabasi_albert_graph(nodes, edges_attach))


regular_network = Regular(4, N)
random_network = Random(0.25, N)
random_geometric_network = RandomGeometric(120, 100, N)
small_world_network = SmallWorld(4, 0.2, N)
scale_free_network = ScaleFree(3, N)

fig_degree = FigureDegree()
fig_cc = FigureCC()
fig_closeness_centr = FigureClosenessCentr()
fig_betweenness_centr = FigureBetweennessCentr()
fig_eigenvector_centr = FigureEigenvectorCentr()
fig_networks_diagrams = FigureDiagrams()


networks = [
    [regular_network.calc_degree_distribution(), regular_network.calc_avg_shortest_path(), regular_network.calc_cc(), regular_network.calc_closeness_centrality(), regular_network.calc_betweenness_centrality(), regular_network.calc_eigenvector_centrality(), regular_network.network, "Regular"],
    [random_network.calc_degree_distribution(), random_network.calc_avg_shortest_path(), random_network.calc_cc(), random_network.calc_closeness_centrality(), random_network.calc_betweenness_centrality(), random_network.calc_eigenvector_centrality(), random_network.network,"Random"],
    [random_geometric_network.calc_degree_distribution(), random_geometric_network.calc_avg_shortest_path(), random_geometric_network.calc_cc(), random_geometric_network.calc_closeness_centrality(), random_geometric_network.calc_betweenness_centrality(), random_geometric_network.calc_eigenvector_centrality(), random_geometric_network.network,"Random Geometric"],
    [small_world_network.calc_degree_distribution(), small_world_network.calc_avg_shortest_path(), small_world_network.calc_cc(), small_world_network.calc_closeness_centrality(), small_world_network.calc_betweenness_centrality(), small_world_network.calc_eigenvector_centrality(), small_world_network.network,"Small World"],
    [scale_free_network.calc_degree_distribution(), scale_free_network.calc_avg_shortest_path(), scale_free_network.calc_cc(), scale_free_network.calc_closeness_centrality(), scale_free_network.calc_betweenness_centrality(), scale_free_network.calc_eigenvector_centrality(), scale_free_network.network,"Scale-Free"]
]






row = 1
column = 1
for network in networks:
      fig_degree.plot(network[0], row-1, column-1, network[len(network) - 1])
      fig_cc.plot(network[2], row-1, column-1, network[len(network) - 1])
      print(f"Average shortest path of: {network[len(network) - 1]} is {network[1]}")
      fig_closeness_centr.plot(network[3],  row-1, column-1, network[len(network) - 1])
      fig_betweenness_centr.plot(network[4], row-1, column-1, network[len(network) - 1])
      fig_eigenvector_centr.plot(network[5], row-1, column-1, network[len(network) - 1])
      fig_networks_diagrams.plot(network[6], row-1, column-1, network[len(network) - 1])
      if column % 2 == 0:
            row += 1
            column -= 1
      else :
            column += 1

# fig, ax = plt.subplots(3, 2)
# fig.suptitle("Network Diagrams")
# pos = nx.circular_layout(small_world_network.network)
# nx.draw(small_world_network.network, pos=pos, with_labels=True, ax=ax[row-1, column-1])

# pos = nx.circular_layout(small_world_network.network)
# nx.draw(scale_free_network.network, pos=pos, with_labels=True, ax=ax2, node_color="#2E8B57")

plt.show()
