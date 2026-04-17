import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from src.service.tarea_service import TareaService


class TablaTareasActivas:
    def __init__(self, ventana):
        self.tarea_id =  None
        self.ventana = ventana
        self.generar_crear_tabla()
        # self.iniciar_refresco_tabla()


    def generar_crear_tabla(self):
        frm_tabla = ttk.Frame(self.ventana)
        frm_tabla.columnconfigure(0, weight=1)
        frm_tabla.columnconfigure(1, weight=0)
        frm_tabla.rowconfigure(0, weight=1)

        columnas = ("Tarea_id", "Titulo", "Descripcion", "Estado")

        self.tabla = ttk.Treeview(frm_tabla, columns=columnas, show="headings")

        for columna in columnas:
            # headings
            self.tabla.heading(columna, text=columna)
            # columns
            if columna == "Estado":
                self.tabla.column(column=columna, anchor=tk.CENTER, width=20, minwidth=20)
                continue
            self.tabla.column(column=columna)

        # Muestra solo las columnas indicadas, ocultal el ID
        self.tabla.configure(displaycolumns=["Titulo", "Descripcion", "Estado"])

        # Cargar datos de la db
        self.cargar_datos_tabla()

        # Selecciona tarea de la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.tarea_seleccinada)
        self.tabla.bind("<Button-1>", self.finalizar_tarea)
        self.tabla.bind("<Button-1>", self.deselecionar_tabla, add="+")


        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)


        # Agregamos Scrollbar
        scrollbar = ttk.Scrollbar(frm_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        frm_tabla.grid(row=1, column=1, sticky=tk.NSEW, pady=20, padx=20)


    def tarea_seleccinada(self, e):
        seleccion = self.tabla.selection()

        if not seleccion:
            print("No hay registros seleccionados")
            return

        tarea_seleccionada = seleccion[0]
        tarea = self.tabla.item(tarea_seleccionada)
        tarea_id, titulo, descripcion, estado = tarea["values"]

        # Agregar datos al entry y text
        if self.tarea_id != tarea_id:
            self.formulario.limpiar_formulario()
            self.tarea_id = tarea_id
            self.formulario.ent_titulo.insert(0, titulo)
            self.formulario.ent_descripcion.insert(1.0, descripcion)

        # Cambia texto del boton
        self.formulario.btn_agregar.configure(text="Actualizar")


    def refrescar_tabla(self):
        # 1. Limpiar todos los datos actuales de la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        self.cargar_datos_tabla()


    def cargar_datos_tabla(self):
        tareas = TareaService.tareas_activas()
        for tarea in tareas:
            self.tabla.insert(parent="", index=tk.END, values=(tarea.tarea_id, tarea.titulo, tarea.descripcion, "☐"))


    # def iniciar_refresco_tabla(self):
    #     self.refrescar_tabla()
    #     self.tabla.after(15000, self.iniciar_refresco_tabla)


    def finalizar_tarea(self, event):
        item = self.tabla.identify_row(event.y)
        column = self.tabla.identify_column(event.x)

        if column == "#3":  # columna Estado
            valores = list(self.tabla.item(item, "values"))

            if valores[3] == "☐":
                # valores[3] = "☑"
                # Finaliza tarea

                TareaService.finalizar_tarea(valores[0])
                showinfo(title="Atención", message="La tarea fue finalizada!")

                # Cargar nuevamente la tabla
                self.refrescar_tabla()
                self.formulario.limpiar_formulario()


    def deselecionar_tabla(self, event):
        # Identificar la región donde se hizo click
        region = self.tabla.identify_region(event.x, event.y)
        print(region)

        # Si la region no es 'cell' (o 'tree'), significa que es un área vacía
        if region not in ("tree", "cell"):
            # Deseleccionar todos los elementos seleccionados
            self.tabla.selection_remove(self.tabla.selection())
            # Limpiar formulario
            self.formulario.limpiar_formulario()


    def set_formulario(self, formulario):
        self.formulario = formulario


