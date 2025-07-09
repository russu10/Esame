from database.DB_connect import DBConnect
from model.arco import Arco
from model.state import State
from model.sighting import Sighting


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def get_all_states(lat,lng):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select  *
from state s 
where s.Lat > %s
and s.lng > %s"""
            cursor.execute(query,(lat,lng,))

            for row in cursor:
                result.append(
                    State(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_sightings():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                    from sighting s 
                    order by `datetime` asc """
            cursor.execute(query)

            for row in cursor:
                result.append(Sighting(**row))
            cursor.close()
            cnx.close()
        return result

    def getDati():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select max(s.lat) as m1, min(s.lat) as m2 ,
max(s.lng) as m3, min(s.lng) as m4
from state s  """
            cursor.execute(query)

            for row in cursor:
                result.append((row["m1"],row["m2"],row["m3"],row["m4"]))
            cursor.close()
            cnx.close()
        return result

    def getShape():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select  distinct s.shape as forma
from sighting s
where s.shape != ""

"""
            cursor.execute(query)

            for row in cursor:
                result.append(
                    row["forma"])

            cursor.close()
            cnx.close()
        return result

    def getArchi(lat,lng,forma):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select s1.id as id1, s2.id as id2 , t1.durata+t2.durata as peso
from state s1 , state s2 , neighbor n , (select  s.state as ids , sum(s.duration) as durata
from sighting s 
where s.shape = %s
group by s.state) t1 , (select  s.state as ids , sum(s.duration) as durata
from sighting s 
where s.shape = %s
group by s.state) t2
where n.state1 = s1.id
and n.state2 =s2.id
and s1.id < s2.id
and t1.ids = s1.id
and t2.ids = s2.id
and s1.lat > %s
and s1.lng > %s
and s2.lat >%s
and s2.lng > %s
order by s1.id asc """
            cursor.execute(query,(forma,forma,lat,lng,lat,lng))

            for row in cursor:
                result.append(Arco(**row))
            cursor.close()
            cnx.close()
        return result





