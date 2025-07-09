import flet as ft
from UI.view import View
from model.model import Model


class Controller:

    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        local = self._view.dd_localization.value
        grafo = self._model.buildGraph(local)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f" Grafo con {len(grafo.nodes)} nodi e {len(grafo.edges)} archi"))
        for arco in grafo.edges(data=True):
            self._view.txt_result.controls.append(ft.Text(f"{arco[0]} -> {arco[1]} peso : {arco[2]["peso"]}"))
        self._view.update_page()

    def analyze_graph(self, e):
        connesse = self._model.getConnesse()
        for c in connesse:
            nodi_str = ", ".join(str(n) for n in c)
            self._view.txt_result.controls.append(ft.Text(f" {nodi_str} | dimensione = {len(c)}"))
        self._view.update_page()

    def handle_path(self, e):
        team , score, len = self._model.getMax()
        self._view.txt_result.controls.clear()
        for t in team:
            self._view.txt_result.controls.append(ft.Text(f"{t} "))
        self._view.txt_result.controls.append(ft.Text(f"scpre : {score} len : {len}"))
        self._view.update_page()

    def fillDD(self):
        local = self._model.local
        for l in local:
            self._view.dd_localization.options.append(ft.dropdown.Option(l))
        self._view.update_page()

