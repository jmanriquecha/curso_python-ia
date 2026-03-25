import tkinter as tk

ventana = tk.Tk()


#Redimencionar ventana
ventana.geometry("800x500")

# Cambiar el titulo
ventana.title("Nueva ventana")


# Evitar redimencionar ventana
# ventana.resizable(0,0)

# Cambiar color a la ventana
ventana.configure(background="#111")

# Ejecutar
ventana.mainloop()