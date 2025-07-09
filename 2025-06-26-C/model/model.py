import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.anni = DAO.getAllYears()
        self.grafo= nx.Graph()
        self.idMap = {}
        self.team = []
        self.sfortuna = 0
    def buildGraph(self,anno1,anno2):
        self.grafo.clear()
        nodi = DAO.getAllConstructors()

        for n in nodi:

            for i in range(anno1,anno2+1):
                punteggio = DAO.getAllPunteggi(n.constructorId,i)
                if len(punteggio)>0:
                    n.risultati[i] = punteggio
            self.grafo.add_nodes_from(nodi)

        for i in self.grafo.nodes:
            for j in self.grafo.nodes:
                if i.constructorId < j.constructorId and self.calcolaPeso(i,j)>0:
                    self.grafo.add_edge(i,j,peso=self.calcolaPeso(i,j))



        return self.grafo

    def calcolaPeso(self,n1,n2):
        peso = 0

        if len(n1.risultati.values()) == 0 or len(n2.risultati.values()) == 0:
            return peso

        for r in n1.risultati.values():  # per ogni anno
            for p in r:  # per ogni pilota e per ogni gara
                if p.position is not None:
                    peso += 1

        for r in n2.risultati.values():  # per ogni anno
            for p in r:  # per ogni pilota e per ogni gara
                if p.position is not None:
                    peso += 1

        return peso

    def getConnessa(self):
        conn = max(nx.connected_components(self.grafo), key=len)
        lista = []
        for nodo in conn:
            lista.append((nodo,self.trovaPesoMax(nodo)))
        lista.sort(key=lambda x: x[1], reverse=True)
        return lista

    def trovaPesoMax(self,nodo):
        pesoMax = 0

        for nodo1 in self.grafo.neighbors(nodo):
            if self.grafo[nodo][nodo1]["peso"]>pesoMax:
                pesoMax = self.grafo[nodo][nodo1]["peso"]

        return pesoMax

    def getSfortunati(self,M,K):
        self.team = []
        self.sfortuna = 0
        parziale = []

        connessa = list((max(nx.connected_components(self.grafo), key=len)))
        rimanenti = copy.deepcopy(connessa)
        for c in connessa:
            if len(list(c.risultati.keys()))>= M:
                parziale.append(c)
                rimanenti.remove(c)
                self.ricorsione(parziale,rimanenti,M,K)
                parziale.pop()
                rimanenti.append(c)
        return self.team,self.sfortuna

    def ricorsione(self,parziale,rimanenti,M,K):
        if len(parziale) == K:
            if self.calcolaSfortuna(parziale)> self.sfortuna:
                self.sfortuna = self.calcolaSfortuna(parziale)
                self.team = copy.deepcopy(parziale)
            return

        for c in rimanenti:
            if len(list(c.risultati.keys()))>= M:
                parziale.append(c)
                rimanenti.remove(c)
                self.ricorsione(parziale,rimanenti,M,K)
                parziale.pop()
                rimanenti.append(c)

    def calcolaSfortuna(self,parziale):
        npTot = 0
        np = 0
        for nodo in parziale:
            for risultato in nodo.risultati.values():
                npTot+= len(risultato)
                for pilota in risultato:
                    if pilota.position is not None:
                        np += 1


        return 1- np/npTot
