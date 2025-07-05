nx.number_connected_components(grafo)
#restituisce il numero di componenti connesse di quel grafo(sottografo)

conn = nx.node_connected_component(self.graph, source)
        print("modo 4", len(conn))
        return len(conn)
#restituisce un set di nodi ( fare list())
#trova la componente connessa in un grafo NON ORIENTATO

nx.weakly_connected_components(grafo)
nx.strongly_connected_components(grafo)

for componente in nx.strongly_connected_components(grafo):
    if nodoCercaro in componente:
        componenteTrovata = componente.copy.deepcopy()
#comp connessa per un grafo ORIENTATO

list(nx.connected_components(self.grafo))
#trova la lista delle componenti connesse del grafo