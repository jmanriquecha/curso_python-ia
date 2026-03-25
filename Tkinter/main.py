import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Mi primera app")
ventana.geometry("1300x700")

# Crear un texto
label = tk.Label(ventana, text="Hola, mundo")
label.pack()

# Crear un botón
def saludar():
    print("Hola desde el botón")

boton = tk.Button(ventana, text="Haz clic", command=saludar)
boton.pack()

# Ejecutar la app
ventana.mainloop()