import networkx as nx
import matplotlib.pyplot as plt


N = 140

def is_connected(adjlist_lines):
    graph = {}
    for line in adjlist_lines:
        nodes = line.strip().split()
        node = int(nodes[0])
        neighbors = [int(x) for x in nodes[1:]]
        graph[node] = neighbors

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS from an arbitrary node
    start_node = next(iter(graph.keys()), None)  # Get the first node, if available
    if start_node is not None:
        dfs(start_node)

    # Check if all nodes were visited
    return len(visited) == len(graph)


class Figure:
      def __init__(self, rows, columns):
            self.rows = rows
            self.columns = columns
            if self.columns == 0 :
                  self.fig, self.axs = plt.subplots(squeeze=False)
            else:
                  self.fig, self.axs = plt.subplots(self.rows, self.columns, squeeze=False)
                  self.fig.delaxes(self.axs[2, 1])
            
      def plot(self):
            pass


class FigureDegree(Figure):

      def plot(self, degrees, row, column, title):
            degree_values = list(degrees.values())
            max_degree = max(degree_values)
            bins = range(0, max_degree + 2, 1)  # Define bins from 0 to max_degree + 1
            # Count the number of nodes in each bin
            degree_counts = [degree_values.count(degree) for degree in bins]
            self.fig.suptitle("Node Degree")
            self.axs[row, column].bar(bins, degree_counts, width=0.8, align='center')
            self.axs[row, column].set_title(title)
            self.axs[row, column].set_ylabel("Frequency")
            self.axs[row, column].set_xlabel("Degree")
            self.fig.tight_layout()


class FigureShortestPath(Figure):

      def plot(self, shortest_paths):
            bins = [0.1 * i for i in range(11)] 
            networks = ["Regular", "Random", "Random Geometric", "Small World", "Scale Free"]
            bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:blue']
            self.axs[0,0].set_title("Average Shortest Paths")
            self.axs[0,0].set_ylabel("Hops")
            self.axs[0,0].bar(networks, shortest_paths, color=bar_colors, align='center')
            

class FigureCC(Figure):

      def plot(self, clustering_coeffs, row, column, title):
            bins = [0.1 * i for i in range(11)] 
            cluster_coeff_counts = [sum(1 for cc in clustering_coeffs.values() if bin_val <= cc < bin_val + 0.1) for bin_val in bins]
            self.fig.suptitle("Clustering Coefficient")
            self.axs[row, column].bar(bins, cluster_coeff_counts, width=0.1, align='edge')
            self.axs[row, column].set_title(title)
            self.axs[row, column].set_ylabel("Frequency")
            self.axs[row, column].set_xlabel("CC")
            self.fig.tight_layout()
            

class FigureClosenessCentr(Figure):

      def plot(self, closeness_centrality, row, column, title):
            self.fig.suptitle("Closeness Centrality")
            self.axs[row, column].bar(closeness_centrality.values(), closeness_centrality.keys())
            self.axs[row, column].set_title(title)
            self.axs[row, column].set_ylabel("Frequency")
            self.axs[row, column].set_xlabel("Closeness Centrality")
            self.fig.tight_layout()


class FigureBetweennessCentr(Figure):

      def plot(self, betweenness_centrality, row, column, title):
            self.fig.suptitle("Betweenness Centrality")
            self.axs[row, column].bar(betweenness_centrality.values(), betweenness_centrality.keys())
            self.axs[row, column].set_title(title)
            self.axs[row, column].set_ylabel("Frequency")
            self.axs[row, column].set_xlabel("Betweenness Centrality")
            self.fig.tight_layout()      


class FigureEigenvectorCentr(Figure):

      def plot(self, eigenvector_centrality, row, column, title):
            self.fig.suptitle("Eigenvector Centrality")
            self.axs[row, column].bar(eigenvector_centrality.values(), eigenvector_centrality.keys())
            self.axs[row, column].set_title(title)
            self.axs[row, column].set_ylabel("Frequency")
            self.axs[row, column].set_xlabel("Eigenvector Centrality")
            self.fig.tight_layout()  


class FigureDiagrams(Figure):
      
      def plot(self, network, row, column, title):
            self.fig.suptitle("Networks Diagrams")
            pos = nx.circular_layout(network)
            nx.draw(network, pos=pos, with_labels= True, ax= self.axs[row, column])
            self.axs[row, column].set_title(title)
            self.fig.tight_layout()


class FigureConnectivityRate(Figure):

      def plot(self, x, y):            
            plt.plot(x, y, label="Connectivity")
            plt.title("Connectivity Rate")
            plt.xlabel("Connection Probability")
            plt.ylabel("C %")
            plt.grid()
            plt.legend()


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

fig_degree = FigureDegree(3, 2)
fig_avg_path = FigureShortestPath(1, 0)
fig_cc = FigureCC(3, 2)
fig_closeness_centr = FigureClosenessCentr(3, 2)
fig_betweenness_centr = FigureBetweennessCentr(3, 2)
fig_eigenvector_centr = FigureEigenvectorCentr(3, 2)
fig_networks_diagrams = FigureDiagrams(3, 2)
fig_connectivity_rate = FigureConnectivityRate(1, 0)



networks = [
    [regular_network.calc_degree_distribution(), regular_network.calc_avg_shortest_path(), regular_network.calc_cc(), regular_network.calc_closeness_centrality(), regular_network.calc_betweenness_centrality(), regular_network.calc_eigenvector_centrality(), regular_network.network, "Regular"],
    [random_network.calc_degree_distribution(), random_network.calc_avg_shortest_path(), random_network.calc_cc(), random_network.calc_closeness_centrality(), random_network.calc_betweenness_centrality(), random_network.calc_eigenvector_centrality(), random_network.network,"Random"],
    [random_geometric_network.calc_degree_distribution(), random_geometric_network.calc_avg_shortest_path(), random_geometric_network.calc_cc(), random_geometric_network.calc_closeness_centrality(), random_geometric_network.calc_betweenness_centrality(), random_geometric_network.calc_eigenvector_centrality(), random_geometric_network.network,"Random Geometric"],
    [small_world_network.calc_degree_distribution(), small_world_network.calc_avg_shortest_path(), small_world_network.calc_cc(), small_world_network.calc_closeness_centrality(), small_world_network.calc_betweenness_centrality(), small_world_network.calc_eigenvector_centrality(), small_world_network.network,"Small World"],
    [scale_free_network.calc_degree_distribution(), scale_free_network.calc_avg_shortest_path(), scale_free_network.calc_cc(), scale_free_network.calc_closeness_centrality(), scale_free_network.calc_betweenness_centrality(), scale_free_network.calc_eigenvector_centrality(), scale_free_network.network,"Scale-Free"]
]






row = 1
column = 1
avg_paths = []
for network in networks:
      fig_degree.plot(network[0], row-1, column-1, network[len(network) - 1])
      avg_paths.append(network[1])
      fig_cc.plot(network[2], row-1, column-1, network[len(network) - 1])
      fig_closeness_centr.plot(network[3],  row-1, column-1, network[len(network) - 1])
      fig_betweenness_centr.plot(network[4], row-1, column-1, network[len(network) - 1])
      fig_eigenvector_centr.plot(network[5], row-1, column-1, network[len(network) - 1])
      fig_networks_diagrams.plot(network[6], row-1, column-1, network[len(network) - 1])
      if column % 2 == 0:
            row += 1
            column -= 1
      else :
            column += 1


fig_avg_path.plot(avg_paths)


p = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
connectivity = []
for probability in p:
      connected_graphs = 0
      for i in range (1, 51, 1):
            random_network = Random(probability, N)
            if is_connected(nx.generate_adjlist(random_network.network)):
                  connected_graphs += 1
      connectivity.append(connected_graphs / 50)   

fig_connectivity_rate.plot(p, connectivity)


plt.show()
