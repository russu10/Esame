import copy

from database.DAO import DAO
import networkx as nx

from model.state import State


class Model:
    def __init__(self):
        self.dati = DAO.getDati()
        self.m1 = int(self.dati[0][0])
        self.m2 = int(self.dati[0][1])
        self.m3 = int(self.dati[0][2])
        self.m4 = int(self.dati[0][3])
        self.grafo = nx.Graph()
        self.idMap = {}
        self.percorso = []
        self.PunteggioMax = 0.0
        self._cammino_ottimo = []
        self._punteggio_ottimo = 0.0


        self.forme = DAO.getShape()

    def buildGraph(self,lat,lng,forma):
        self.grafo.clear()
        nodi = DAO.get_all_states(lat,lng)
        print(len(nodi))
        for nodo in nodi:
            self.idMap[nodo.id] = nodo
        self.grafo.add_nodes_from(nodi)
        archi = DAO.getArchi(lat,lng,forma)
        for arco in archi:
            self.grafo.add_edge(self.idMap[arco.id1],self.idMap[arco.id2], peso = arco.peso)
        return self.grafo

    def getDettagli(self):
        archi = list(self.grafo.edges(data=True))
        ordinati = sorted(archi ,key = lambda x: x[2]["peso"], reverse = True)
        archiMax = []
        for i in range(0,5):
            archiMax.append((ordinati[i][0],ordinati[i][1],ordinati[i][2]["peso"]))

        nodi = list(self.grafo.nodes())
        trovati = []
        for nodo in nodi:
            trovati.append((nodo,len(list(self.grafo.neighbors(nodo)))))

        ord = sorted(trovati,key = lambda x: x[1], reverse = True)
        nodiMax = []
        for i in range(0,5):
            nodiMax.append(ord[i][0])
        return nodiMax , archiMax

    def getMax(self):
        self.percorso = []
        self.PunteggioMax = 0.0
        nodi = list(self.grafo.nodes())

        for nodo in nodi:

            self.ricorsione([nodo])

        return self.percorso , self.PunteggioMax

    def ricorsione(self,parziale):
        if len(self.calcolaRimanenti(parziale[-1])) == 0:
            if self.calcolaPunteggio(parziale) > self.PunteggioMax:
                self.PunteggioMax = self.calcolaPunteggio(parziale)
                self.percorso = copy.deepcopy(parziale)
            return

        for nodo in self.calcolaRimanenti(parziale[-1]):
            if nodo not in parziale:
                parziale.append(nodo)
                self.ricorsione(parziale)
                parziale.pop()
    def calcolaRimanenti(self,nodo):
        vicini = list(self.grafo.neighbors(nodo))
        successivi = []
        for v in vicini:
            if self.calcolaDensita(v) > self.calcolaDensita(nodo):
                successivi.append(v)
        return successivi

    def calcolaDensita(self,nodo):
        return nodo.Population/nodo.Area


    def calcolaPunteggio(self,parziale):
        distanzaTot = 0
        pesoTot = 0

        for i in range(0,len(parziale)-1):
            distanzaTot += parziale[i].distance_HV(parziale[i+1])
            pesoTot += self.grafo[parziale[i]][parziale[i+1]]["peso"]

        return pesoTot/distanzaTot  if distanzaTot != 0 else 0


    # SOLUZIONE DEL PROF :
    def cammino_ottimo(self):
        self._cammino_ottimo = []
        self._punteggio_ottimo = 0.0

        for nodo in self.grafo.nodes():
            self._calcola_cammino_ricorsivo([nodo], self._calcola_successivi(nodo))
        return self._cammino_ottimo, self._punteggio_ottimo

    def _calcola_cammino_ricorsivo(self, parziale: list[State], successivi: list[State]):
        if len(successivi) == 0:
            score = self._calcola_score(parziale)
            if score > self._punteggio_ottimo:
                self._punteggio_ottimo = score
                self._cammino_ottimo = copy.deepcopy(parziale)
        else:
            for nodo in successivi:
                # aggiungo il nodo in parziale ed aggiorno le occorrenze del mese corrispondente
                parziale.append(nodo)
                # nuovi successivi
                nuovi_successivi = self._calcola_successivi(nodo)
                # ricorsione
                self._calcola_cammino_ricorsivo(parziale, nuovi_successivi)
                parziale.pop()

    def _calcola_successivi(self, nodo: State) -> list[State]:
        """
        Calcola il sottoinsieme dei successivi ad un nodo
        """
        successivi = self.grafo.neighbors(nodo)
        successivi_ammissibili = []
        for s in successivi:
            if (s.Population / s.Area) > (nodo.Population / nodo.Area):
                successivi_ammissibili.append(s)
        return successivi_ammissibili

    def _calcola_score(self, cammino: list[State]) -> float:
        """
        Funzione che calcola il punteggio di un cammino.
        """
        score = 0
        for i in range(0, len(cammino) - 1):
            peso = self.grafo.get_edge_data(cammino[i], cammino[i + 1])["peso"]
            distanza = cammino[i].distance_HV(cammino[i + 1])
            score += peso / distanza
        return score








