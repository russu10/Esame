import copy
import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self.local = DAO.getAllLocal()
        self.grafo = nx.Graph()
        self.idMap = {}
        self.bestTeam = []
        self.bestScore = 0
        self.bestLen = 0

    def buildGraph(self, local):
        self.grafo.clear()
        nodi = DAO.getNodi(local)
        self.grafo.add_nodes_from(nodi)
        for nodo in nodi:
            self.idMap[nodo.GeneID] = nodo

        archi = DAO.getArchi(local)
        for arco in archi:
            nodo1 = self.idMap[arco.id1]
            nodo2 = self.idMap[arco.id2]
            peso = arco.peso
            self.grafo.add_edge(nodo1,nodo2,peso=peso)
        return self.grafo
    def getConnesse(self):
        connesse = list(nx.connected_components(self.grafo))
        trovate =[]
        for c in connesse:
            if len(c) > 1:
                trovate.append(c)
        return trovate

    def getMax(self):
        self.bestTeam = []
        self.bestScore = 0
        self.bestLen = 0
        allNodes = list(self.grafo.nodes())
        allNodes.sort(key = lambda x : x.GeneID)
        for nodo in allNodes:
            rimanenti = copy.deepcopy(allNodes)
            rimanenti.remove(nodo)
            rimanenti1 = []
            for x in rimanenti:
                if x.Essential == nodo.Essential:
                    rimanenti1.append(x)
            self.ricorsione([nodo],list(rimanenti1))
        return self.bestTeam , self.bestScore, self.bestLen

    def ricorsione(self,parziale,rimanenti):
        if len(rimanenti) == 0:

            if len(parziale) > self.bestLen:
                self.bestLen = len(parziale)
                self.bestScore = self.getScore(parziale)
                self.bestTeam = copy.deepcopy(parziale)
            if len(parziale) == self.bestLen:
                if self.getScore(parziale) < self.bestScore:
                    self.bestScore = self.getScore(parziale)
                    self.bestTeam = copy.deepcopy(parziale)
            return



        for n in rimanenti:
            if n.GeneID > parziale[-1].GeneID:
                parziale.append(n)
                rimanenti.remove(n)
                self.ricorsione(parziale, rimanenti)
                parziale.remove(n)
                rimanenti.append(n)

    def getScore(self, parziale):
        return nx.number_connected_components(self.grafo.subgraph(parziale))


