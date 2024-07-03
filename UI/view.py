import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.textT = None
        self.textAlfa = None
        self.textGiorni = None
        self.textAnno = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self.btn_Grafo = None
        self.btn_Simula = None
        self.txt_result = None
        self.txt_container = None

        self.txtN = None
        self.txtOut2 = None
        self.btn_path = None

    def load_interface(self):
        # title
        self._title = ft.Text("Lab13 - Ufo sighting", color="blue", size=24)
        self._page.controls.append(self._title)

        self.textAnno = ft.TextField(label="Anno")
        self.textGiorni = ft.TextField(label="xG")

        self.btn_Grafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)
        row1 = ft.Row([self.textAnno, self.textGiorni, self.btn_Grafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.textT = ft.TextField(label="T1")
        self.textAlfa = ft.TextField(label="Alfa")

        self.btn_Simula = ft.ElevatedButton(text="Simula", on_click=self._controller.handle_simula, disabled=True)
        row2 = ft.Row([self.textT, self.textAlfa, self.btn_Simula],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
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
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
