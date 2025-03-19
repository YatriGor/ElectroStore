__cnx=None
import mysql.connector

def getConn():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Yatri@2004',
                                host='127.0.0.1',
                                database='electro_store')
    return __cnx