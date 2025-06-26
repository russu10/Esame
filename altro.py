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



import sqlite3

class Circuito:
    def __init__(self, id, nome, location, country):
        self.id = id
        self.nome = nome
        self.location = location
        self.country = country
        self.storico_posizioni = {}  # {anno: [(posizione, pilota)]}

    def aggiungi_risultato(self, anno, posizione, pilota):
        if anno not in self.storico_posizioni:
            self.storico_posizioni[anno] = []
        self.storico_posizioni[anno].append((posizione, pilota))

    def __repr__(self):
        return f"Circuito({self.nome}, {self.country}) -> {self.storico_posizioni}"


# Connessione al database
conn = sqlite3.connect("tuo_database.db")
cur = conn.cursor()

# -- getCircuiti --
cur.execute("SELECT circuitId, name, location, country FROM circuits")
circuiti_data = cur.fetchall()

# Crea oggetti Circuito
circuiti = {}
for circuito_id, nome, location, country in circuiti_data:
    circuiti[circuito_id] = Circuito(circuito_id, nome, location, country)

# -- getRisultati tra 2010 e 2020 --
cur.execute("""
    SELECT c.circuitId, r.year, rs.position, d.forename || ' ' || d.surname
    FROM results rs
    JOIN races r ON rs.raceId = r.raceId
    JOIN circuits c ON r.circuitId = c.circuitId
    JOIN drivers d ON rs.driverId = d.driverId
    WHERE rs.position IS NOT NULL AND r.year BETWEEN 2010 AND 2020
    ORDER BY r.year, c.name, rs.position
""")

# Collega risultati ai circuiti
for circuito_id, anno, posizione, nome_pilota in cur.fetchall():
    circuito = circuiti.get(circuito_id)
    if circuito:
        circuito.aggiungi_risultato(anno, posizione, nome_pilota)

conn.close()

# ✅ Esempio stampa
for circuito in circuiti.values():
    if circuito.storico_posizioni:  # Mostra solo i circuiti con risultati nel range
        print(circuito)
