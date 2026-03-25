import tkinter as tk
from tkinter import ttk

from app_login.login import Login

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("600x400")
ventana.configure(background="#1d2d44")
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

style = ttk.Style()
style.theme_use('clam')
style.configure(ventana, background='#1d2d44', foreground="#ffffff", fieldbackground="#000")
style.configure("TButton", background="#005f73")
style.map("TButton", background=[("active", "#0a9396")])

style.configure("contenedor.TFrame")

# Estilos Label
style.configure("s_label.TLabel")

# Frame
frame = ttk.Frame(ventana, style="contenedor.TFrame")
frame.configure( width=300, height=300, padding=20)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)


# Agregar Etrys, label y button
l_login = ttk.Label(frame, text="Login", font=("Arial", 14, "bold"), anchor="center", style="s_label.TLabel")
l_login.grid(row=0, column=0, columnspan=2,  pady=20)

l_usuario = ttk.Label(frame, text="Usuario: ", style="s_label.TLabel")
l_usuario.grid(row=1, column=0, sticky=tk.W)

e_usuario = ttk.Entry(frame)
e_usuario.grid(row=1, column=1, pady=10)

l_pass = ttk.Label(frame, text="Password: ", style="s_label.TLabel")
l_pass.grid(row=2, column=0)

e_pass = ttk.Entry(frame, show="*")
e_pass.grid(row=2, column=1, padx=10)

l_result = ttk.Label(frame, style="s_label.TLabel")
l_result.grid(row=4, column=0, columnspan=2)


# Se crea función de login
login = Login()

def ejecuta_login(event=None):
    if login.validacion(e_usuario.get(), e_pass.get()):
        l_result.configure(text=f"Hola {e_usuario.get()}, Bienvenido...")
        l_result.configure(foreground="green")
    else:
        l_result.configure(text="¡Los datos ingresados no son validos!")
        l_result.configure(foreground="red")
        e_usuario.delete(0, tk.END)
        e_pass.delete(0, tk.END)

b_enviar = ttk.Button(frame, text="Enviar", command=ejecuta_login)
b_enviar.grid(row=3, column=0, columnspan=2, pady=20)


# asociar eventos al boton de login
ventana.bind("<Return>", ejecuta_login)



# Publicar frame
frame.grid(row=0, column=0, pady=50, padx=50)

ventana.mainloop()




