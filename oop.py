import networkx as nx
import matplotlib.pyplot as plt


N = 140

class Figure:
      def __init__(self):
            self.fig, self.axs = plt.subplots(3, 2, squeeze=False)     # 3 rows and 2 columns
            self.fig.tight_layout()
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
            self.axs[row, column].bar(bins, degree_counts, width=0.8, align='center')
            self.axs[row, column].set_title(title)


class FigureCC(Figure):
      def __init__(self):
            super().__init__()      # We should always call the parent's contructor

      def plot(self, clustering_coeffs, row, column, title):
            bins = [0.1 * i for i in range(11)] 
            cluster_coeff_counts = [sum(1 for cc in clustering_coeffs.values() if bin_val <= cc < bin_val + 0.1) for bin_val in bins]
            self.axs[row, column].bar(bins, cluster_coeff_counts, width=0.1, align='edge')
            self.axs[row, column].set_title(title)
            


class NetworkTopology:
      def __init__(self, name, network):
            self.name = name
            self.network = network


      def calc_degree_distribution(self):
            degrees = dict(self.network.degree())
            return degrees
            

      def calc_avg_shortest_path(self):
            pass

      def calc_cc(self):
            return nx.clustering(self.network)

      def calc_closeness_centrality(self):
            pass

      def calc_betweenness_centrality(self):
            pass

      def calc_eigenvector_centrality(self):
            pass


class Regular(NetworkTopology):
      def __init__(self):
            super().__init__("Regular", network= nx.random_regular_graph(4, N))


class Random(NetworkTopology):
      def __init__(self):
            super().__init__("Random", network= nx.gnp_random_graph(N, 0.25))


class RandomGeometric(NetworkTopology):
      def __init__(self):
            super().__init__("Random Geometric", network= nx.random_geometric_graph(N, 120, 100))


class SmallWorld(NetworkTopology):
      def __init__(self):
            super().__init__("Small World", network= nx.watts_strogatz_graph(N, 4, 0.2))


class ScaleFree(NetworkTopology):
      def __init__(self):
            super().__init__("Scale Free", network= nx.barabasi_albert_graph(N, 2))


regular_network = Regular()
random_network = Random()
random_geometric_network = RandomGeometric()
small_world_network = SmallWorld()
scale_free_network = ScaleFree()

fig_degree = FigureDegree()
fig_cc = FigureCC()


networks = [
    [regular_network.calc_cc(), regular_network.calc_degree_distribution(), "Regular"],
    [random_network.calc_cc(), random_network.calc_degree_distribution(), "Random"],
    [random_geometric_network.calc_cc(), random_geometric_network.calc_degree_distribution(), "Random Geometric"],
    [small_world_network.calc_cc(), small_world_network.calc_degree_distribution(), "Small World"],
    [scale_free_network.calc_cc(), scale_free_network.calc_degree_distribution(), "Scale-Free"]
]


row = 1
column = 1
for network in networks:
      fig_cc.plot(network[0], row-1, column-1, network[len(network) - 1])
      fig_degree.plot(network[1], row-1, column-1, network[len(network) - 1])
      if column % 2 == 0:
            row += 1
            column -= 1
      else :
            column += 1


plt.show()
