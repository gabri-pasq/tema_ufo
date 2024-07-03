import networkx as nx
from geopy.distance import geodesic

# distanzaT = geodesic((Lat1, Lng1), (Lat2, Lng2)).kilometers

# self.grafo = nx.Graph()
# self.grafoDirezionato = nx.DiGraph()
# nx.dijkstra_path(Grafo, nodoStart, nodoTarget) questo utilizza il cammino peso minimo
# nx.shortest_path(Grafo, nodoStart, nodoTarget) questo utilizza il cammino piu corto
# nx.number_connected_components(self.grafo)
# self.grafo.clear()


def getConnessa(self, v0int):
    v0 = self._idMap[v0int]

    # Modo1: successori di v0 in DFS
    successors = nx.dfs_successors(self._grafo, v0)
    allSucc = []
    for v in successors.values():
        allSucc.extend(v)

    print(f"Metodo 1 (pred): {len(allSucc)}")

    # Modo2: predecessori di v0 in DFS
    predecessors = nx.dfs_predecessors(self._grafo, v0)
    print(f"Metodo 2 (succ): {len(predecessors.values())}")

    # Modo3: conto i nodi dell'albero di visita
    tree = nx.dfs_tree(self._grafo, v0)
    print(f"Metodo 3 (tree): {len(tree.nodes)}")

    # Modo4: node_connected_component
    connComp = nx.node_connected_component(self._grafo, v0)
    print(f"Metodo 4 (connected comp): {len(connComp)}")

    return len(connComp)