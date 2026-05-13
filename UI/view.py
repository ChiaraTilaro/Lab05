import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self.ddCorso = None
        self.btnCercaIscrittiCorso = None

        self.txtInMatricola = None
        self.txtNome = None
        self.txtCognome = None

        self.btnCercaStudente = None
        self.btnCercaCorsi = None
        self.btnIscrivi = None

        self.lvOut = None



    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW 1
        self.ddCorso = ft.Dropdown(label="Selezionare un corso",
                                   width=200)
        self._controller.fillddCorso()
        self.btnCercaIscrittiCorso = ft.ElevatedButton(text="Cerca Iscritti" ,
                                                       on_click=self._controller.handleCercaIscrittiCorso,
                                                       width=300)
        row1 = ft.Row([self.ddCorso , self.btnCercaIscrittiCorso],
                      alignment= ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        # ROW 2
        self.txtInMatricola = ft.TextField(label="Matricola" ,
                                           width=300)
        self.txtNome = ft.TextField(value="Nome",
                                    width=300,
                                    read_only=True)
        self.txtCognome = ft.TextField(value="Cognome",
                                       width=300,
                                       read_only=True)
        row2 = ft.Row([self.txtInMatricola, self.txtNome, self.txtCognome],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        # ROW 3
        self.btnCercaStudente = ft.ElevatedButton(text="Cerca studente",
                                                  on_click=self._controller.handleCercaStudente,
                                                  width=300)
        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi",
                                               on_click=self._controller.handleCercaCorsi,
                                               width=300)
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi",
                                            on_click=self._controller.handleIscrivi,
                                            width=300)
        row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsi , self.btnIscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)


        self.lvOut = ft.ListView()
        self._page.controls.append(self.lvOut)
        self._page.update()




    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
