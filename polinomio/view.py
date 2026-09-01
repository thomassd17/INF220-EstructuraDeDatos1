import tkinter as tk

class PolinomioView:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingreso de Polinomio - MVC")
        self.root.geometry("420x220")

        # Etiqueta de instrucciones
        self.label_instruccion = tk.Label(
            root, text="Ingresa un polinomio (ej: Ax^2 + Bx - C):"
        )
        self.label_instruccion.pack(pady=10)

        # Campo de entrada
        self.entry_polinomio = tk.Entry(root, width=35)
        self.entry_polinomio.pack(pady=5)

        # Botón
        self.boton_mostrar = tk.Button(root, text="Mostrar Polinomio")
        self.boton_mostrar.pack(pady=10)

        # Label donde se muestra el resultado
        self.label_resultado = tk.Label(
            root, text="", font=("Arial", 14, "bold"), fg="blue"
        )
        self.label_resultado.pack(pady=15)

    def obtener_entrada(self):
        return self.entry_polinomio.get()

    def mostrar_resultado(self, texto):
        self.label_resultado.config(text=texto)

    def mostrar_error(self, mensaje):
        self.label_resultado.config(text=mensaje, fg="red")

    def set_comando_boton(self, funcion):
        self.boton_mostrar.config(command=funcion)