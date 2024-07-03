from database.DB_connect import DBConnect
from model.states import State


class DAO():

    @staticmethod
    def getStati():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select *
                       from state s
                        order by id"""
        cursor.execute(query)
        for row in cursor:
            result.append(State(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select state1, state2
                    from neighbor n 
                    where state1 > state2 """
        cursor.execute(query)
        for row in cursor:
            result.append((row['state1'], row['state2']))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(id1, id2, anno, giorni):
        conn = DBConnect.get_connection()
        result = 0
        cursor = conn.cursor(dictionary=True)
        query = """select  (count(distinct t1.id) + count(distinct t2.id)) as peso
                    from (select *
                            from sighting s 
                            where s.state =%s and year (s.`datetime`) = %s )	as t1,(select *
                                                                                        from sighting s 
                                                                                        where s.state =%s and year (s.`datetime`) = %s )as t2
                    where abs(datediff(t1.datetime,t2.datetime)) <= %s """
        cursor.execute(query,(id1, anno, id2, anno, giorni))
        for row in cursor:
            result= int(row['peso'])
        cursor.close()
        conn.close()
        return result

