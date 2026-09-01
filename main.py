import tkinter as tk
from model import PolinomioModel
from view import PolinomioView
from controller import PolinomioController

def main():
    root = tk.Tk()
    model = PolinomioModel()
    view = PolinomioView(root)
    controller = PolinomioController(model, view)
    root.mainloop()

if __name__ == "__main__":
    main()