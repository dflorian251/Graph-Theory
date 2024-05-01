import networkx as nx


N = 140

class NetworkTopology:
      def __init__(self, name, network):
            self.name = name
            self.network = network


      def calc_degree_distribution(self):
            pass

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
            super().__init__("Regular")
            nx.random_regular_graph(4, N)

      def calc_degree_distribution(self):
            pass

      def calc_avg_shortest_path(self):
            pass

      def calc_cc(self):
            pass

      def calc_closeness_centrality(self):
            pass

      def calc_betweenness_centrality(self):
            pass

      def calc_eigenvector_centrality(self):
            pass



class Random(NetworkTopology):
      def __init__(self):
            super().__init__("Random")



class RandomGeometric(NetworkTopology):
      def __init__(self):
            super().__init__("Random Geometric")


class SmallWorld(NetworkTopology):
      def __init__(self):
            super().__init__("Small World")


class ScaleFree(NetworkTopology):
      def __init__(self):
            super().__init__("Scale Free", network= nx.barabasi_albert_graph(N, 2))


scale_free_network = ScaleFree()
print(scale_free_network.calc_cc())