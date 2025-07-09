import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view: View = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_graph(self, e):
        m1 = self._model.m1
        m2 = self._model.m2
        m3 = self._model.m3
        m4 = self._model.m4
        lat = (self._view.txt_latitude.value)
        lng = (self._view.txt_longitude.value)
        forma = self._view.ddshape.value
        try : latitudine = int(lat)
        except ValueError :
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text("inserire lat valida"))
            self._view.update_page()
            return
        try : longitudine = int(lng)
        except ValueError :
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text("inserire lng valida"))
            self._view.update_page()
            return



        if latitudine >m1 or latitudine < m2 or longitudine >m3 or longitudine <m4:
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text(f"inserire valori di latitudine compresi tra {m2} e {m1}\n"
                                                           f"e valori di longitudine compresi tra {m4} e {m3}"))
            self._view.update_page()
            return
        if forma is None:
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text("inserire forma"))
            self._view.update_page()
            return


        grafo = self._model.buildGraph(latitudine, longitudine, forma)
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Grafo creato con {len(grafo.nodes)} nodi e {len(grafo.edges)} archi "))



        nodi , archi = self._model.getDettagli()
        self._view.txt_result1.controls.append(ft.Text("nodi con grado maggiore :"))
        for n in nodi :
            self._view.txt_result1.controls.append(ft.Text(n.Name))
        self._view.txt_result1.controls.append(ft.Text("archi con peso maggiore"))
        for n in archi :
            self._view.txt_result1.controls.append(ft.Text(f"{n[0]} -> {n[1]} peso: {n[2]}"))


        self._view.btn_path.disabled = False
        self._view.update_page()


    def handle_path(self, e):
        percorso , punteggio = self._model.getMax()
        self._view.txt_result2.controls.clear()
        for nodo in percorso:
            self._view.txt_result2.controls.append(ft.Text(nodo))
        self._view.txt_result2.controls.append(ft.Text(punteggio))
        self._view.update_page()


    def fill_ddshape(self):
        for forma in self._model.forme:
            self._view.ddshape.options.append(ft.dropdown.Option(forma))
        self._view.update_page()
