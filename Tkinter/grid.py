import tkinter as tk
from statistics import geometric_mean
from tkinter import ttk


ventana = tk.Tk()
ventana.title("Menu principal")
ventana.geometry("800x500")
ventana.configure(background="#333")

# Tamaño columnas
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=10)
ventana.columnconfigure(3, weight=1)


# Tamaño filas
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=1)
ventana.rowconfigure(2,weight=1)
ventana.rowconfigure(3,weight=1)


label1 = ttk.Label(ventana, text="Label 1")
label1.grid(row=3, column=0, pady=5, padx=10, sticky=tk.SE)

label2 = ttk.Label(ventana, text="Label 2")
label2.grid(row=0, column=1, pady=5, padx=10, sticky=tk.EW)

label3 = ttk.Label(ventana, text="Label 3")
label3.grid(row=0, column=2, pady=50, ipady=500, padx=10, sticky=tk.NSEW)

label4 = ttk.Label(ventana, text="Label 4")
label4.grid(row=0, column=4, pady=5, padx=10, sticky=tk.NE)


ventana.mainloop()