import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from src.gui.tabla_tareas_activas import TablaTareasActivas
from src.service.tarea_service import TareaService


class Formulario:

    def __init__(self, ventana):
        self.ventana = ventana
        self.crear_formulario()


    def crear_formulario(self):
        formulario = ttk.Frame(self.ventana)
        formulario.columnconfigure(0, weight=0)
        formulario.columnconfigure(1, weight=1)
        formulario.rowconfigure(0, weight=0)
        formulario.rowconfigure(1, weight=1)

        lbl_titulo = ttk.Label(formulario, text="Título", anchor="center")
        lbl_titulo.grid(row=0, column=0, padx=20)

        self.ent_titulo = ttk.Entry(formulario, foreground="red")
        self.ent_titulo.grid(row=0, column=1, sticky=tk.EW)

        lbl_descripcion = ttk.Label(formulario, text="Descripción")
        lbl_descripcion.grid(row=1, column=0, sticky=tk.N, pady=20, padx=20)

        self.ent_descripcion = tk.Text(formulario, height=10)
        self.ent_descripcion.grid(row=1, column=1, sticky=tk.N, pady=20)

        self.botones(formulario)

        formulario.grid(row=1, column=0, sticky=tk.NSEW, padx=20, pady=20)


    def botones(self, contenedor):
        self.btn_agregar = ttk.Button(contenedor, text="Guardar", command=self.validar_tarea)
        self.btn_agregar.grid(row=2, column=0, columnspan=2)


    def validar_tarea(self):
        try:
            tarea_id = self.tabla_tareas_activas.tarea_id
            titulo = self.ent_titulo.get()
            descripcion = self.ent_descripcion.get("1.0", "end-1c")

            if tarea_id is None:
                self.agregar_tarea(titulo, descripcion)
            else:
                self.actualizar_tarea(tarea_id, titulo, descripcion)

            self.tabla_tareas_activas.refrescar_tabla()
            self.limpiar_formulario()
        except ValueError as e:
            showerror(title="Error", message=e)

        except Exception as e:
            showerror(title="Error", message=e)



    def agregar_tarea(self, titulo, descripcion):
            TareaService.crear(titulo, descripcion)


    def actualizar_tarea(self, tarea_id, titulo, descripcion):
            TareaService.actualizar(tarea_id, titulo, descripcion)



    def limpiar_formulario(self):
        self.ent_titulo.delete(0, tk.END)
        self.ent_descripcion.delete("1.0", tk.END)
        self.tabla_tareas_activas.tarea_id = None
        self.btn_agregar.configure(text="Guardar")

    def set_tabla_tareas_activas(self, tabla_tareas_activas):
        self.tabla_tareas_activas = tabla_tareas_activas
