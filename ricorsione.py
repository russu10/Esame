"""def getDreamTeam(self, k):
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
    return score"""


#ALGORITMO RICORSIVO CAMMINO PESO MASSIMO IN GRAFO ORIENTATO
"""def getBestPath(self, startStr):
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
                    self._graph[parziale[-1]][v]["weight"]): #check if peso nuovo arco è minore del precedente
                parziale.append(v)
                self._ricorsione(parziale)
                parziale.pop()

    def getScore(self, listOfNodes):
        tot = 0
        for i in range(len(listOfNodes) - 1):
            tot += self._graph[listOfNodes[i]][listOfNodes[i + 1]]["weight"]

        return tot
    def getStores(self):
        return DAO.getAllStores()"""