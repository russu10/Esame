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
