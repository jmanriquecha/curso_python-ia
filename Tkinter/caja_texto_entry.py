import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Menu principal")
ventana.geometry("700x450")

caja_texto1 = ttk.Entry(ventana)
caja_texto1.pack(pady=20)
nombre = caja_texto1.get

def saludar(nombre):
    print(nombre)

    etiqueta_1 = ttk.Label(ventana, text=f"Hola {nombre}")
    etiqueta_1.pack(pady=10)

boton1 = ttk.Button(ventana, text="Guardar", command=lambda: saludar(nombre()))
boton1.pack(pady=10)


ventana.mainloop()