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

#PROVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

from database.DB_connect import DBConnect
from model.Circuito import Circuito

class DAO:

    @staticmethod
    def getCircuitiConRisultati():
        conn = DBConnect.get_connection()
        results = {}

        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT 
                c.circuitId, c.name, c.location, c.country,
                r.year,
                d.forename, d.surname,
                rs.position
            FROM results rs
            JOIN races r ON rs.raceId = r.raceId
            JOIN circuits c ON r.circuitId = c.circuitId
            JOIN drivers d ON rs.driverId = d.driverId
            WHERE rs.position IS NOT NULL
              AND r.year BETWEEN 2010 AND 2020
            ORDER BY c.circuitId, r.year, rs.position
        """

        cursor.execute(query)

        for row in cursor:
            circuitId = row["circuitId"]
            year = row["year"]
            posizione = int(row["position"])
            pilota = f"{row['forename']} {row['surname']}"

            if circuitId not in results:
                results[circuitId] = Circuito(
                    id=circuitId,
                    nome=row["name"],
                    location=row["location"],
                    country=row["country"]
                )

            results[circuitId].aggiungi_risultato(year, posizione, pilota)

        cursor.close()
        conn.close()
        return list(results.values())


from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass
class Circuito:
    id: int
    nome: str
    location: str
    country: str
    storico_posizioni: Dict[int, List[Tuple[int, str]]] = field(default_factory=dict)

    def aggiungi_risultato(self, anno: int, posizione: int, pilota: str):
        if anno not in self.storico_posizioni:
            self.storico_posizioni[anno] = []
        self.storico_posizioni[anno].append((posizione, pilota))

