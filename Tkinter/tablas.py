import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Ventana principal
ventana = tk.Tk()
ventana.title("Manejo de tablas")
ventana.configure(background="#0d2d21")
ventana.geometry("600x400")

# Configurarl el grid

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=0)
ventana.rowconfigure(0, weight=1)

# Definir estilos
style = ttk.Style()
style.theme_use("clam") # Prepara para el manejo de tema oscuro
style.configure("Treeview", background="black",
                foreground="white",
                fieldbaground="black",
                rowheight=30)
style.map("Treeview", background=[("selected", "#3a86ff")])

# Tabla
tabla = ttk.Treeview(ventana, columns=("Nombre", "Apellido"), show="headings")

# Definir encabezados
tabla.heading("Nombre", text="Nombre", anchor=tk.W)
tabla.heading("Apellido", text="Apellido")

# Formato a las columnas
tabla.column("Nombre", width=200)
tabla.column("Apellido", width=200)

# Insertar datos
datos = (("Juan Carlos", "Garcia"), ("Valentina Julieth", "Velazco Cortez"),
         ("Gabriel Javier", "Rozo Millan"), ("Carmelina Aurora", "Pinzon Rodriguez"))
for persona in datos:
    tabla.insert(parent="", index=tk.END, values=persona)


# Agregamos Scrollbar
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)


# Mostrar registro seleccionado
def mostrar_registro_seleccionado(event):
    print("Ejecutando mostrar registro seleccinado")
    elemento_seleccionado = tabla.selection()[0] # Solo se procesa el primer registro seleccionado
    elemento = tabla.item(elemento_seleccionado) # item
    persona = elemento["values"] # Tupla registro persona
    print(persona)
    nombre, apellido = persona
    showinfo(title="Registro Seleccionado...", message=nombre + " " +apellido)

# Asociar el evento select de la tabla
tabla.bind("<<TreeviewSelect>>", mostrar_registro_seleccionado)


tabla.grid(row=0, column=0, sticky=tk.NSEW)

ventana.mainloop()
