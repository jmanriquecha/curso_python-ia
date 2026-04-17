import tkinter as tk
from tkinter import ttk

from src.gui.formulario import Formulario
from src.gui.tabla_tareas_activas import TablaTareasActivas


class Ventana(tk.Tk):

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.configurar_estilos()
        self.mostrar_titulo()
        self.tabla_tareas_activas = TablaTareasActivas(self)
        self.formulario = Formulario(self)

        #
        self.tabla_tareas_activas.set_formulario(self.formulario)
        self.formulario.set_tabla_tareas_activas(self.tabla_tareas_activas)


    def configurar_ventana(self):
        self.title("Gestor de tareas")
        self.geometry("1000x500")


    def configurar_grid(self):
        # Columnas
        self.columnconfigure(0, weight=1, uniform="grupo1")
        self.columnconfigure(1, weight=2, uniform="grupo1")
        # Filas
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)


    def mostrar_titulo(self):
        titulo = ttk.Label(self, text="Gestor de tareas", style="encabezado.TLabel", font=("Verdana", 20), anchor="center")
        titulo.grid(row=0, column=0, columnspan=2, sticky=tk.N, pady=20)


    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("encabezado.TLabel", fieldbackground="red")
