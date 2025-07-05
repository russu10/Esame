self.grafo.subgraph(parziale)
#restituisce un sottografo ( parziale è un set di nodi)

self._graph.in_edges(nodo, data=True):
#restituisce gli archi entranti

ARCHI_VICINI = GRAFO.edges(NODO, data=True)
# OTTIENE TUTTI GLI ARCHI VICINI, ANCHE IL PESO IN UN GRAFO NON ORIENTATO

self._graph.out_edges(nodo, data=True):
#RESTITUISCE GLI ARCHI USCENTI

self._graph.neighbors(start)
#trova i nodi vicini  uscenti in un grafo orientato
#trova tutti gli adiacenti in un grafo normale

adiacenti = list(self.grafo[nodo].items())
#trova i nodi adiacenti ad un nodo, restituisce  una lista di tuple
# tupla = (nodo, {"peso": 5}
# peso = tupla[1][["peso"]

for nodo in nodi:
    self.idMap[nodo.GeneID] = nodo
#idmpap

peso = grafo[nodo1][nodo2]["peso"]
#per trovare il peso dell arco tra nodo1 e nodo 2

list(grafo.edges(data=true))
#resitituisce una lista di tuple ( nodo1, nodo2 , dizionario del peso)

list(grafo.edges)
#resituisce unalista di  tuple ( nodo1, nodo2) se hanno un arco

nx.dfs_successors(self.graph, source).values()
# lista successori

nx.dfs_predecessors(self.graph, source).values()

#lista predecessori

nx.dfs_tree(self.graph,source)
#albero visita (non ancora listato)