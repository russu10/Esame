import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.idMap = {}
        self.percorso = []
        self.lunghezzaMax = 0


    def buildGraph(self, cmin , cmax):
        self.grafo.clear()
        nodi = DAO.get_all_genes(cmin,cmax)
        for nodo in nodi:
            self.idMap[nodo.GeneID,nodo.Function] = nodo
        self.grafo.add_nodes_from(nodi)
        archi = DAO.getArchi(cmin,cmax)
        for arco in archi :
            nodo1 = self.idMap[arco.id1,arco.f1]
            nodo2 = self.idMap[arco.id2,arco.f2]
            peso = arco.peso
            self.grafo.add_edge(nodo1,nodo2,peso = peso)
        return self.grafo

    def getDettagli(self):
        nodi = self.grafo.nodes()
        trovati = []
        for nodo in nodi:
            uscenti = list(self.grafo.out_edges(nodo, data=True))
            lunghezza = len(uscenti)
            pesoTot = 0
            for nodo1,nodo2,data in uscenti:
                peso = self.grafo[nodo1][nodo2]["peso"]
                pesoTot += peso
            trovati.append((nodo,uscenti,lunghezza,pesoTot))

        ordinati = sorted(trovati, key = lambda x: x[2] , reverse = True)
        return ordinati
    def getCammino(self):
        self.percorso = []
        self.lunghezzaMax = 0
        nodi = list(self.grafo.nodes())
        for nodo in nodi:
            self.ricorsione([nodo])

        return self.percorso , self.lunghezzaMax , self.calcolaPeso(self.percorso)
    def ricorsione(self,parziale):
        rimanenti = self.calcolaRimanenti(parziale[-1])
        if len(rimanenti) == 0:
            if len(parziale) > self.lunghezzaMax:
                self.lunghezzaMax = len(parziale)
                self.percorso = copy.deepcopy(parziale)
            if len(parziale) == self.lunghezzaMax:
                if self.calcolaPeso(parziale) < self.calcolaPeso(self.percorso):
                    self.lunghezzaMax = len(parziale)
                    self.percorso = copy.deepcopy(parziale)
            return

        for nodo in rimanenti:
            if nodo not in parziale:
                if len(parziale) ==1:
                    parziale.append(nodo)
                    self.ricorsione(parziale)
                    parziale.pop()
                else:
                    if self.grafo[parziale[-1]][nodo]["peso"] >= self.grafo[parziale[-2]][parziale[-1]]["peso"]:
                        parziale.append(nodo)
                        self.ricorsione(parziale)
                        parziale.pop()

    def calcolaRimanenti(self,nodo):
        vicini = list(self.grafo.neighbors(nodo))
        viciniOk = []
        for v in vicini:
            if v.Essential != nodo.Essential:
                viciniOk.append(v)
        return viciniOk
    def calcolaPeso(self,parziale):
        pesoTot = 0
        for i in range(0,len(parziale)-1):
            pesoTot += self.grafo[parziale[i]][parziale[i+1]]["peso"]
        return pesoTot







