def getArchiViciniAmm(self, nodoLast, parziale):
    archiVicini = self._grafo.edges(nodoLast, data=True)
    result = []
    for a1 in archiVicini:
        if self.isAscendent(a1, parziale) and self.isNovel(a1, parziale):
            result.append(a1)
    return result


def isAscendent(self, e, parziale):
    if len(parziale) == 0:
        print("parziale is empty in isAscendent")
        return True
    return e[2]["weight"] >= parziale[-1][2]["weight"]


def isNovel(self, ARCO, parziale):
    if len(parziale) == 0:
        print("parziale is empty in isnovel")
        return True
    e_inv = (ARCO[1], ARCO[0], ARCO[2])
    return (e_inv not in parziale) and (ARCO not in parziale)
# QUESTE TRE FUNZIONI TROVANO GLI ARCHI VICINI E CHE ABBIANO PESO
# MAGGIORE RISPETTO A TUTTO IL PESO DI PARZIALE
#IN UN GRAFO NON ORIENTATO

for c in connesse:
    nodi_str = ", ".join(str(n) for n in c)
#per stampare senza andare a capo

list(risultati.keys())
#restituisce la lista delle chiavi del dizionario risultati

len(risultati.values())
#lunghezza valori del dizionario risultati

ordinati = sorted(adiacenti, key=lambda x: x[1].get("peso", 0), reverse=True)
#ordina la lista e dice che se esite peso lo ordina desc se no usa 0
#adiacenti è una lista di tuple ( nodo , dizionario peso)

ordinati = sorted(trovati,key = lambda x: x[1], reverse = True)
# ordina una lista di tuple(trovati)


