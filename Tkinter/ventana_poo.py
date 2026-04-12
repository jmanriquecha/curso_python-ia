import tkinter as tk
from tkinter import ttk
from tkinter.constants import NSEW
from tkinter.messagebox import showinfo


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        # Configurar ventana
        self.configurar_ventana()
        #Configurar Grid
        self.configurar_grid()
        # Mostrar tabla
        self.mostrar_tabla()


    def configurar_ventana(self):
        self.geometry("600x300")
        self.title("Manejo de ventanas con POO")
        self.configure(background="#0d2d21")


    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)


    def mostrar_tabla(self):
        # Definir estilos
        style = ttk.Style()
        style.theme_use("clam")  # Prepara para el manejo de tema oscuro
        style.configure("Treeview", background="black",
                        foreground="white",
                        fieldbaground="black",
                        rowheight=30)
        style.map("Treeview", background=[("selected", "#3a86ff")])

        # Tabla
        self.tabla = ttk.Treeview(self, columns=("Nombre", "Apellido"), show="headings")
        # Definir encabezados
        self.tabla.heading("Nombre", text="Nombre", anchor=tk.W)
        self.tabla.heading("Apellido", text="Apellido")

        # Formato a las columnas
        self.tabla.column("Nombre", width=200)
        self.tabla.column("Apellido", width=200)

        # Insertar datos
        datos = (("Juan Carlos", "Garcia"), ("Valentina Julieth", "Velazco Cortez"),
                 ("Gabriel Javier", "Rozo Millan"), ("Carmelina Aurora", "Pinzon Rodriguez"))
        for persona in datos:
            self.tabla.insert(parent="", index=tk.END, values=persona)

        # Agregamos Scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Asociar el evento select de la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.mostrar_registro_seleccionado)

        self.tabla.grid(row=0, column=0, sticky=NSEW)

    # Mostrar registro seleccionado
    def mostrar_registro_seleccionado(self, event):
        print("Ejecutando mostrar registro seleccinado")
        elemento_seleccionado = self.tabla.selection()[0]  # Solo se procesa el primer registro seleccionado
        elemento = self.tabla.item(elemento_seleccionado)  # item
        persona = elemento["values"]  # Tupla registro persona
        print(persona)
        nombre, apellido = persona
        showinfo(title="Registro Seleccionado...", message=f"Persona {nombre} {apellido}")


if __name__ == "__main__":
    app = App()
    app.mainloop()