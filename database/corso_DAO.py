from database import DB_connect
from model.corso import Corso
from model.studente import Studente


class CorsoDAO:

    @staticmethod
    def getAllCorsi(corsi):

        cnx = DB_connect.get_connection()

        cursor = cnx.cursor(dictionary=True)

        query = """
        SELECT *
        FROM corso
        """

        cursor.execute(query)

        for row in cursor:

            corso = Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]
            )

            corsi[corso.codins] = corso

        cursor.close()
        cnx.close()

    @staticmethod
    def getIscrittiCorso(codins):

        cnx = DB_connect.get_connection()

        cursor = cnx.cursor(dictionary=True)

        query = """
        select *
from studente s , iscrizione i 
where s.matricola = i.matricola and i.codins = %s
        """

        cursor.execute(query , (codins,))
        res = []
        for row in cursor:
            res.append(Studente(
                matricola=row["matricola"],
                cognome= row["cognome"],
                nome=row["nome"],
                CDS=row["CDS"]
            ))



        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiStudente(matricola):

        cnx = DB_connect.get_connection()

        cursor = cnx.cursor(dictionary=True)

        query = """
        select c.codins , c.crediti , c.nome , c.pd 
from corso c , iscrizione i
where c.codins = i.codins and i.matricola = %s
        """

        cursor.execute(query , (matricola,))
        res = []
        for row in cursor:
            res.append(Corso(
                **row
            ))



        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def handleIscriviStudente(codins , matricola):

        cnx = DB_connect.get_connection()

        cursor = cnx.cursor(dictionary=True)

        query = """
        INSERT IGNORE INTO `iscritticorsi`.`iscrizione` 
    (`matricola`, `codins`) 
    VALUES(%s,%s)
        """

        cursor.execute(query , (matricola, codins , ))



        cursor.close()
        cnx.close()
        return True
