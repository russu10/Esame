from database.DB_connect import DBConnect
from model.arco import Arco
from model.gene import Gene
from model.interaction import Interaction


class DAO():

    @staticmethod
    def get_all_genes(cmin,cmax):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select *
from genes g
where g.Chromosome between %s and %s
order by g.GeneID asc"""
            cursor.execute(query,(cmin,cmax,))

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


    def getArchi(cmin,cmax):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinctrow g1.GeneID as id1, g2.GeneID as id2, g1.`Function` as f1, g2.`Function` as  f2, g1.Chromosome , g2.Chromosome , i.Expression_Corr as peso 
from genes g1,genes g2, classification c1, classification c2 , interactions i 
where g1.Chromosome between %s and %s
and g2.Chromosome between %s and %s
and g1.GeneID =c1.GeneID
and g2.GeneID = c2.GeneID
and g1.GeneID <> g2.GeneID
and c1.Localization =c2.Localization
and ((i.GeneID1=g1.GeneID AND i.GeneID2=g2.GeneID) or (i.GeneID1=g2.GeneID AND i.GeneID2=g1.GeneID))
and g1.Chromosome <= g2.Chromosome"""
            cursor.execute(query,(cmin,cmax,cmin,cmax,))

            for row in cursor:
                result.append(Arco(row["id1"],row["f1"],row["id2"],row["f2"],row["peso"]))

            cursor.close()
            cnx.close()
        return result