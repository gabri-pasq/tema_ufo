import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        if self._view.textAnno.value == "":
            self._view.create_alert("Inserire un anno")
            return
        if self._view.textGiorni.value == "":
            self._view.create_alert("Inserire un giorno")
            return
        try:
            anno = int(self._view.textAnno.value)
            xG = int(self._view.textGiorni.value)
            if anno > 2014 or anno < 1906:
                self._view.create_alert("Inserire un anno tra 1906 e 2014")
                return
            elif xG < 1 or xG > 180:
                self._view.create_alert("Inserire un valore in xG tra 1 e 180")
                return
            else:
                self._model.creaGrafo(anno, xG)
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text(self._model.detailGraph()))
                for n, p in self._model.adiacenti():
                    self._view.txt_result.controls.append(ft.Text(f"{n}, peso adiacenti: {p}"))
                self._view.update_page()

        except ValueError:
            self._view.create_alert("Inserire valori interi")
            return

    def handle_simula(self, e):
        pass
