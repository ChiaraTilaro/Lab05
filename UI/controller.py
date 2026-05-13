import flet as ft

from model import corso


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillddCorso(self):
        for codins , c in self._model.getAllCorsi().items():
            self._view.ddCorso.options.append(
                ft.dropdown.Option(
                    key=c.codins,
                    text=c.nome
                )
            )
        self._view.update_page()

    def handleCercaIscrittiCorso(self , e):
        self._view.lvOut.controls.clear()
        if self._view.ddCorso.value is None:
            self._view.lvOut.controls.append(
                ft.Text("Selezionare un corso!")
            )
            self._view.update_page()
            return
        codins = self._view.ddCorso.value
        iscritti = self._model.getIscrittiCorso(codins)
        if len(iscritti) == 0:
            self._view.lvOut.controls.append(
                ft.Text("Non ci sono iscritti a questo corso")
            )
        else:
            self._view.lvOut.controls.append(
                ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:")
            )
            for studente in iscritti:
                self._view.lvOut.controls.append(
                    ft.Text(f"{studente}")
                )
        self._view.update_page()


    def handleCercaStudente(self , e):
        self._view.lvOut.controls.clear()
        if self._view.txtInMatricola.value == "":
            self._view.lvOut.controls.append(
                ft.Text("Inserire una matricola!")
            )
            self._view.update_page()
            return
        matricola = self._view.txtInMatricola.value
        studente = self._model.getStudente(matricola)
        if studente is None:
            self._view.lvOut.controls.append(
                ft.Text("Nessuno studente corrisponde alla matricola inserita")
            )
        else:
            self._view.txtNome.value = f"{studente.nome}"
            self._view.txtCognome.value = f"{studente.cognome}"
        self._view.update_page()

    def handleCercaCorsi(self , e):
        self._view.lvOut.controls.clear()
        if self._view.txtInMatricola.value == "":
            self._view.lvOut.controls.append(
                ft.Text("Inserire una matricola!")
            )
            self._view.update_page()
            return
        matricola = self._view.txtInMatricola.value
        iscrizioneCorsi = self._model.getCorsiStudente(matricola)
        if len(iscrizioneCorsi) == 0:
            self._view.lvOut.controls.append(
                ft.Text("Lo studente non è iscritto ad alcun corso")
            )
        else:
            self._view.lvOut.controls.append(
                ft.Text(f"Corsi a cui è iscritto lo studente:")
            )
            for corso in iscrizioneCorsi:
                self._view.lvOut.controls.append(
                    ft.Text(corso)
                )
        self._view.update_page()

    def handleIscrivi(self , e):
        self._view.lvOut.controls.clear()
        if self._view.ddCorso.value is None:
            self._view.lvOut.controls.append(
                ft.Text("Selezionare un corso!")
            )
            self._view.update_page()
            return
        if self._view.txtInMatricola.value == "":
            self._view.lvOut.controls.append(
                ft.Text("Inserire una matricola!")
            )
            self._view.update_page()
            return

        codins = self._view.ddCorso.value
        matricola = self._view.txtInMatricola.value
        aggiunta = self._model.iscriviStudente(codins , matricola)
        if aggiunta == True:
            self._view.lvOut.controls.append(
                ft.Text("Iscrizione avvenuta con successo")
            )
        else:
            self._view.lvOut.controls.append(
                ft.Text("Impossibile iscrivere lo studente al corso selezionato")
            )
        self._view.update_page()
