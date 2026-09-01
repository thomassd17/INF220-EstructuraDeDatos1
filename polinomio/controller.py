class PolinomioController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_comando_boton(self.manejar_click)

    def manejar_click(self):
        texto_ingresado = self.view.obtener_entrada()
        es_valido = self.model.parsear(texto_ingresado)

        if es_valido:
            resultado = self.model.obtener_polinomio_formateado()
            self.view.label_resultado.config(fg="blue")
            self.view.mostrar_resultado(f"P(x) = {resultado}")
        else:
            self.view.mostrar_error("Polinomio inválido. Ej: 3x^2+2x-5")
