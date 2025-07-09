import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleBuildGraph(self, e):
        anno1 = self._view._ddYear1.value
        anno2 = self._view._ddYear2.value
        if anno1 is None or anno2 is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserisci anni"))
            self._view._update_page()
            return

        grafo = self._model.buildGraph(int(anno1), int(anno2))
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo creato correttamente"))
        self._view._txt_result.controls.append(ft.Text(f"con {len(grafo.nodes)} nodi e {len(grafo.edges)} archi"))
        self._view.update_page()


    def handlePrintDetails(self, e):
        connessa = self._model.getConnessa()
        self._view._txt_result.controls.clear()
        for ci in connessa:
            self._view._txt_result.controls.append(ft.Text(f"nodo {ci[0]} - {ci[1]} peso"))
        self._view.update_page()

    def handleCercaTeamSfortunati(self, e):
        M = self._view._txtInNumDiEdizioni.value
        K = self._view._txtInSoglia.value
        team , sfortuna = self._model.getSfortunati(int(M),int(K))
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Team sfortunato:"))
        for t in team:
            self._view._txt_result.controls.append(ft.Text(t))
        self._view._txt_result.controls.append(ft.Text(f"{sfortuna}"))

        self._view.update_page()
    def fillDD(self):
        anni = self._model.anni
        for anno in anni:
            self._view._ddYear1.options.append(ft.dropdown.Option(anno))
            self._view._ddYear2.options.append(ft.dropdown.Option(anno))

        self._view.update_page()
