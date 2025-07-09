from database.DB_connect import DBConnect
from model.arco import Arco
from model.classification import Classification
from model.gene import Gene
from model.interaction import Interaction


class DAO():

    @staticmethod
    def get_all_genes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                        FROM genes"""
            cursor.execute(query)

            for row in cursor:
                result.append(Gene(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_interactions():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                           FROM interactions"""
            cursor.execute(query)

            for row in cursor:
                result.append(Interaction(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_classifications():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                        FROM classification"""
            cursor.execute(query)

            for row in cursor:
                result.append(Classification(**row))

            cursor.close()
            cnx.close()
        return result
    def getAllLocal():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct c.localization as local
from classification c 
order by c.Localization desc"""
            cursor.execute(query)

            for row in cursor:
                result.append(row["local"])

            cursor.close()
            cnx.close()
        return result

    def getNodi(local):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select c.GeneID , c.Localization , g.Essential
from classification c , genes g
where g.GeneID  = c.GeneID
and c.Localization =%s
group by c.GeneID 
order by c.GeneID asc"""
            cursor.execute(query,(local,))

            for row in cursor:
                result.append(Classification(**row))

            cursor.close()
            cnx.close()
        return result

    def getArchi(local):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT i.GeneID1 as id1, i.GeneID2 as id2, t.somma as peso
FROM genes g1, genes g2, classification c1, classification c2, interactions i,
     (SELECT g1.GeneID AS id1, g2.GeneID AS id2,
             CASE 
                 WHEN g1.Chromosome = g2.Chromosome THEN g1.Chromosome
                 ELSE g1.Chromosome + g2.Chromosome
             END AS somma
      FROM genes g1, genes g2
      WHERE g1.Chromosome <= g2.Chromosome
      GROUP BY g1.GeneID, g2.GeneID) AS t
WHERE g1.GeneID <> g2.GeneID
  AND c1.GeneID = g1.GeneID
  AND g2.GeneID = c2.GeneID
  AND c1.Localization = %s
  AND c2.Localization = c1.Localization
  AND i.GeneID1 = g1.GeneID
  AND i.GeneID2 = g2.GeneID
  AND t.id1 = g1.GeneID
  AND t.id2 = g2.GeneID"""
            cursor.execute(query, (local,))

            for row in cursor:
                result.append(Arco(**row))

            cursor.close()
            cnx.close()
        return result

