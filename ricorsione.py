#Esame gene luglio 2024
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


#ESAME GENE
def getMax(self):
    self.bestTeam = []
    self.bestScore = 0
    self.bestLen = 0
    allNodes = list(self.grafo.nodes())
    allNodes.sort(key=lambda x: x.GeneID)
    for nodo in allNodes:
        rimanenti = copy.deepcopy(allNodes)
        rimanenti.remove(nodo)
        rimanenti1 = []
        for x in rimanenti:
            if x.Essential == nodo.Essential:
                rimanenti1.append(x)
        self.ricorsione([nodo], list(rimanenti1))
    return self.bestTeam, self.bestScore, self.bestLen


def ricorsione(self, parziale, rimanenti):
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

#ESAME FORMULA 1
def getDreamTeam(self, k):
    self._bestPath = []
    self._bestScore = 1000

    parziale = []
    self._ricorsione(parziale, k)
    return self._bestPath, self._bestScore


def _ricorsione(self, parziale, k):
    if len(parziale) == k:
        if self.getScore(parziale) < self._bestScore:
            self._bestScore = self.getScore(parziale)
            self._bestPath = copy.deepcopy(parziale)
        return

    for n in self._graph.nodes():
        if n not in parziale:
            parziale.append(n)
            self._ricorsione(parziale, k)
            parziale.pop()


def getScore(self, team):
    score = 0
    for e in self._graph.edges(data=True):
        if e[0] not in team and e[1] in team:
            score += e[2]["weight"]
    return score


#ALGORITMO RICORSIVO CAMMINO PESO MASSIMO IN GRAFO ORIENTATO
def getBestPath(self, startStr):
        self._bestPath = []
        self._bestScore = 0

        start = self._idMap[int(startStr)]

        parziale = [start]

        vicini = self._graph.neighbors(start)
        for v in vicini:
            parziale.append(v)
            self._ricorsione(parziale)
            parziale.pop()

        return self._bestPath, self._bestScore
    def _ricorsione(self, parziale):
        if self.getScore(parziale) > self._bestScore:
            self._bestScore = self.getScore(parziale)
            self._bestPath = copy.deepcopy(parziale)

        for v in self._graph.neighbors(parziale[-1]):
            if (v not in parziale and #check if not in parziale
                    self._graph[parziale[-2]][parziale[-1]]["weight"] >
                    self._graph[parziale[-1]][v]["weight"]):
                #check if peso nuovo arco è minore del precedente
                parziale.append(v)
                self._ricorsione(parziale)
                parziale.pop()

    def getScore(self, listOfNodes):
        tot = 0
        for i in range(len(listOfNodes) - 1):
            tot += self._graph[listOfNodes[i]][listOfNodes[i + 1]]["weight"]

        return tot
    def getStores(self):
        return DAO.getAllStores()
