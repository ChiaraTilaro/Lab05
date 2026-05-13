# Add whatever it is needed to interface with the DB Table studente

from mysql.connector import cursor

from database import DB_connect
from model.corso import Corso
from model.studente import Studente


class StudenteDAO():

    @staticmethod
    def getStudente(matricola):
            cnx = DB_connect.get_connection()
            cursor = cnx.cursor(dictionary = True)

            query = """
            select *
from studente s 
where s.matricola = %s
            """

            cursor.execute(query , (matricola , ))


            for row in cursor:
               studente = Studente(
                    matricola= row["matricola"],
                   cognome= row["cognome"],
                   nome= row["nome"],
                   CDS= row["CDS"]
               )

            cursor.close()
            cnx.close()
            return studente

