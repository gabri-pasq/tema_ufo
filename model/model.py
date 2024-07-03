import copy

import networkx as nx
from database.DAO import DAO
from geopy.distance import geodesic


class Model:

    def __init__(self):
        self.grafo = None
        self.idMap = {}

    def creaGrafo(self, anno, giorni):
        self.idMap = {}
        self.grafo = nx.Graph()
        stati = DAO.getStati()
        self.grafo.add_nodes_from(stati)
        for s in stati:
            self.idMap[s.id] = s
        archi = DAO.getArchi()
        for a in archi:
            s1 = self.idMap[a[0]]
            s2 = self.idMap[a[1]]
            self.grafo.add_edge(s1, s2, peso=0)

        for n1, n2 in list(self.grafo.edges):
            p = DAO.getPeso(n1.id, n2.id, anno, giorni)
            self.grafo[n1][n2]['peso'] = p

    def adiacenti(self):
        lista = []
        for n in self.grafo.nodes:
            p=0
            for vicino in self.grafo.neighbors(n):
                p += self.grafo[n][vicino]['peso']
            lista.append((n, p))
        lista.sort(key=lambda x: x[1], reverse=True)
        return lista



    def detailGraph(self):
        return f"{len(self.grafo.nodes())} nodi, {len(self.grafo.edges())} archi"
