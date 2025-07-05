self._view.txt_result.controls.clear()
self._view.txt_result.controls.append(ft.Text(f"scpre : {score} len : {len}"))
self._view.update_page()


def fillDD(self):
    local = self._model.local
    for l in local:
        self._view.dd_localization.options.append(ft.dropdown.Option(l))
    self._view.update_page()

#riempi tendina
