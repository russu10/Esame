ARCHI_VICINI = GRAFO.edges(NODO, data=True)
# OTTIENE TUTTI GLI ARCHI VICINI, ANCHE IL PESO IN UN GRAFO NON ORIENTATO



self._graph.out_edges(n, data=True):
#RESTITUISCE GLI ARCHI USCENTI

self._graph.in_edges(n, data=True):
#entranti


self._graph.neighbors(start)
#trova i nodi vicini  uscenti in un grafo orientato
#iìtrova tutti gli adiacenti in un grafo normale

conn = nx.node_connected_component(self.graph, source)
        print("modo 4", len(conn))
        return len(conn)

#trova la componente connessa in un grafo NON ORIENTATO

nx.weakly_connected_components(grafo)
nx.strongly_connected_components(grafo)

for componente in nx.strongly_connected_components(grafo):
    if nodoCercaro in componente:
        componenteTrovata = componente.copy.deepcopy()
#comp connessa per un grafo ORIENTATO


adiacenti = list(self.grafo[nodo].items())
#trova i nodi adiacenti in una lista di tuple
# tupla = (nodo, {"peso": 5}
# peso = tupla[1][["peso"]


edges = list(itertools.combinations(self.squadre, 2))
Questa riga genera tutte le coppie possibili di squadre (senza ripetizioni né inversioni), tratte dalla lista self.squadre.



#questo trova gli archi vicini e il rispettivo peso
 def getNeighborsSorted(self, source):
        vicini = nx.neighbors(self._grafo, source)  # [v0 v1 v2 ...]
        # vicini = self._grafo.neighbors(source)

        viciniTuple = []

        for v in vicini:
            viciniTuple.append((v, self._grafo[source][v]["weight"]))  # [(v0, p0) (v1, p1) ()]

        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple

