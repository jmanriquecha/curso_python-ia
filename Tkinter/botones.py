import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Pricipal")
ventana.geometry("500x250")

def saludar(nombre):
    etiqueta1 = ttk.Label(ventana, text= f"Hola {nombre}, te saludo desde el boton")
    etiqueta1.pack()

nombre = "Juan Castro"
boton1 = ttk.Button(ventana, text="Saludar", command=lambda: saludar(nombre))
# boton1.configure(text="Guardar")
# boton1["text"] = "Autoguardado"
boton1.pack(pady=20)



# Ejecuta
ventana.mainloop()