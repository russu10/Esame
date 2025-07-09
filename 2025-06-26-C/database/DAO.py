from database.DB_connect import DBConnect
from model.costruttore import Costruttore
from model.punteggio import Punteggio


class DAO():
    @staticmethod
    def getAllConstructors():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    from constructors"""
        cursor.execute(query)

        res = []

        for row in cursor:
            res.append(Costruttore(row["constructorId"],
                                   row["constructorRef"],
                                   row["name"],
                                   row["nationality"],
                                    row["url"],
                                   {}))

        cursor.close()
        cnx.close()
        return res

    def getAllYears():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct year
from seasons
order by year desc"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["year"])

        cursor.close()
        cnx.close()
        return res

    def getAllPunteggi(ID,ANNO):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.constructorId , re.driverId , re.position , re.raceId , ra.year , ra.circuitId
from constructors c , results re , races ra
where re.raceId =ra.raceId 
and c.constructorId = re.constructorId
and c.constructorId =%s
and ra.year = %s"""
        cursor.execute(query,(ID,ANNO,))

        res = []
        for row in cursor:
            res.append(Punteggio(row["driverId"],row["position"],row["circuitId"]))

        cursor.close()
        cnx.close()
        return res







