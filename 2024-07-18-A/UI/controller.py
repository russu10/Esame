import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        cmin = self._view.dd_min_ch.value
        cmax = self._view.dd_max_ch.value
        grafo = self._model.buildGraph(cmin, cmax)
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f" Grafo creato con {len(grafo.nodes)} nodi e"
                                                       f" {len(grafo.edges)} archi "))
        self._view.update_page()

    def handle_dettagli(self, e):
        ordinati = self._model.getDettagli()
        for i in range(0,5):
            self._view.txt_result1.controls.append(ft.Text(f"{ordinati[i][0]} num uscenti {ordinati[i][2]} peso tot -> {ordinati[i][3]}"))
        self._view.update_page()


    def handle_path(self, e):
        percorso , lunghezza , peso = self._model.getCammino()
        self._view.txt_result2.controls.clear()
        for p in percorso:
            self._view.txt_result2.controls.append(ft.Text(f"{p}"))
        self._view.txt_result2.controls.append(ft.Text(f" lunghezza -> {lunghezza}"))
        self._view.txt_result2.controls.append(ft.Text(f"peso totale -> {peso}"))
        self._view.update_page()

    def fillDD(self):
        for i in range(1,10):
            self._view.dd_max_ch.options.append(ft.dropdown.Option(i))
            self._view.dd_min_ch.options.append(ft.dropdown.Option(i))
        self._view.update_page()