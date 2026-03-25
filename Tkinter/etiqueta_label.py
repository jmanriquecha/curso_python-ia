import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Trabajando con etiquetas 'Label'")

# Redimencionar
ventana.geometry("600x300")


# Creamos una etiqueta (label)
label = ttk.Label(ventana, text="Nombre: ")
label.pack(pady=20)


# Cambiamo el texto usando el metodo configure
label.configure(text="Modificando nombre por Apellido")


# Otra forma de modificar el texto de una etiqueta es con la key
label["text"] = "Nuevo nombre en la etiqueta"


# Ejecutar ventana
ventana.mainloop()