from database import corso_DAO
from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO


class Model:
    def __init__(self):
        self.corsi = None
        self.studenti = dict()

    def getAllCorsi(self):
        if self.corsi is None:
            self.corsi = dict()
            CorsoDAO.getAllCorsi(self.corsi)
            return self.corsi

    def getIscrittiCorso(self , codins):
        return CorsoDAO.getIscrittiCorso(codins)

    def getStudente(self , matricola):
        return StudenteDAO.getStudente(matricola)

    def getCorsiStudente(self , matricola):
        return CorsoDAO.getCorsiStudente(matricola)

    def iscriviStudente(self , codins , matricola):
        return CorsoDAO.handleIscriviStudente(codins , matricola)



