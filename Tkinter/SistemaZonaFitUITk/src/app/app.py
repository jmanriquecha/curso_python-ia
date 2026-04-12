import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, showerror, askyesno

from service.cliente_service import ClienteService


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.cliente_service = ClienteService()
        self.id_seleccionado = None

        # Configurar ventana
        self.ventana()
        self.configurar_grid()
        self.mostrar_botones()
        self.mostrar_encabezado()
        self.mostrar_tabla()
        self.mostrar_formulario()
        self.configura_estilos()


    def ventana(self):
        self.title("Zona Fit (GYM)")
        self.geometry("1000x600")
        self.configure(background="#666666")


    def configurar_grid(self):
        # Configurar columnas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        # Configurar filas
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)


    def mostrar_encabezado(self):
        titulo = ttk.Label(self, text="Zona Fit (GYM)", background="#666", foreground="#fff", font=("Arial", 20, "bold"), anchor="center")
        titulo.grid(row=0, column=0, columnspan=2, sticky=tk.EW)


    def mostrar_formulario(self):
        formulario = ttk.Frame(self)
        # Columnas frame
        formulario.columnconfigure(0, weight=1)
        formulario.columnconfigure(1, weight=1)

        # Filas frame
        formulario.rowconfigure(0, weight=1)
        formulario.rowconfigure(1, weight=1)
        formulario.rowconfigure(2, weight=1)

        # Labels
        lb_nombre = ttk.Label(formulario, text="Nombre")
        lb_nombre.grid(row=0, column=0, sticky=tk.SE, pady=10)
        lb_apellido = ttk.Label(formulario, text="Apellido")
        lb_apellido.grid(row=1, column=0, sticky=tk.E, pady=10)
        lb_membresia = ttk.Label(formulario, text="Membresia")
        lb_membresia.grid(row=2, column=0, sticky=tk.NE, pady=10)

        # Cajas texto
        self.ent_nombre = ttk.Entry(formulario)
        self.ent_nombre.grid(row=0, column=1, sticky=tk.S, pady=10)
        self.ent_apellido = ttk.Entry(formulario)
        self.ent_apellido.grid(row=1, column=1, pady=10)
        self.ent_membresia = ttk.Entry(formulario)
        self.ent_membresia.grid(row=2, column=1, sticky=tk.N, pady=10)

        # Focus en nombre
        self.ent_nombre.focus()

        formulario.grid(row=1, column=0, sticky=tk.NSEW)


    def mostrar_tabla(self):
        frm_tabla = ttk.Frame(self)
        # Configurar grid
        frm_tabla.columnconfigure(0, weight=1)
        frm_tabla.columnconfigure(1,weight=0)
        frm_tabla.rowconfigure(0, weight=1)

        columnas = ("Id", "Nombre", "Apellido", "Membresia")
        self.tabla = ttk.Treeview(frm_tabla, columns=columnas, show="headings")

        self.tabla.heading("Id", text="Id")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("Membresia", text="Membresia")

        self.tabla.column(column="Id", width=50)
        self.tabla.column(column="Nombre", width=250)
        self.tabla.column(column="Apellido", width=250)
        self.tabla.column(column="Membresia", width=100)

        #Cargar datos de la base de datos
        self.cargar_datos_tabla()

        # mostrar elemento seleccionado
        self.tabla.bind("<<TreeviewSelect>>", self.mostrar_registro_seleccionado)

        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)

        # Agregamos Scrollbar Vertical
        scrollbar = ttk.Scrollbar(frm_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        frm_tabla.grid(row=1, column=1, padx=50, sticky=tk.NSEW)


    def mostrar_botones(self):
        btn_frame = ttk.Frame(self)
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)
        btn_frame.columnconfigure(2, weight=1)

        btn_guardar = ttk.Button(btn_frame, text="Guardar",
                                 command=self.validar_cliente)
        btn_guardar.grid(row=0, column=0, padx=20)
        btn_eliminar = ttk.Button(btn_frame, text="Eliminar",
                                  command=self.eliminar_cliente)
        btn_eliminar.grid(row=0, column=1, padx=20)
        btn_limpiar = ttk.Button(btn_frame, text="Limpiar",
                                 command=self.limpiar_entry)
        btn_limpiar.grid(row=0, column=2, padx=20)

        btn_frame.grid(row=2, column=0, columnspan=2, pady=20)


    def configura_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#666")
        style.configure("TButton")
        style.configure("TLabel", background="#666", foreground="#fff")
        style.configure("TEntry", foreground="yellow", fieldbackground="#555")
        style.configure("Treeview", rowheight=30)


    def limpiar_entry(self, limpiar_seleccion = True):
        self.ent_nombre.delete(0, tk.END)
        self.ent_apellido.delete(0, tk.END)
        self.ent_membresia.delete(0, tk.END)

        # deseleccionar registro
        if limpiar_seleccion:
            self.tabla.selection_remove(self.tabla.selection())
            self.id_seleccionado = None
        # Focus en nombre
        self.ent_nombre.focus()


    def eliminar_cliente(self):
        if self.id_seleccionado is None:
            showwarning(title="Atención!", message="Debes seleccionar un cliente a eliminar..!")
            return


        confirmar = askyesno("Confirmar", "¿Seguro que deseas eliminar este cliente?")
        if not confirmar:
            return

        eliminado = self.cliente_service.eliminar_cliente(self.id_seleccionado)

        if eliminado:
            showinfo(title="Se elimino el registro", message=f"Se elimino el cliente {self.id_seleccionado}")
            self.limpiar_entry()
            self.refrescar_tabla()

        else:
            showwarning(title="Atención!", message="No se encontro el registro o ya fue eliminado")

        self.tabla.selection_remove(self.tabla.selection())
        self.id_seleccionado = None


    def mostrar_registro_seleccionado(self, event):
        seleccion = self.tabla.selection()

        # Comprobamos si la tupla NO está vacía
        if not seleccion:
            print("No hay ningún registro seleccionado.")
            return  # Salimos de la función para que no continúe

        elemento_seleccionado = seleccion[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_id, nombre, apellido, membresia = elemento["values"]

        # limpiar entry antes de insertar
        self.limpiar_entry(limpiar_seleccion=False)

        # Insertar
        self.ent_nombre.insert(0, nombre)
        self.ent_apellido.insert(0, apellido)
        self.ent_membresia.insert(0, membresia)

        self.id_seleccionado = cliente_id



    def cargar_datos_tabla(self):
        lista_clientes = self.cliente_service.listar_clientes()
        for cliente in lista_clientes:
            self.tabla.insert(parent="",
                              index=tk.END,
                              values=(cliente.cliente_id, cliente.nombre, cliente.apellido, cliente.membresia))


    def refrescar_tabla(self):
        # 1. Limpiar todos los datos actuales de la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar datos en la tabla
        self.cargar_datos_tabla()


    def validar_cliente(self):
        nombre = self.ent_nombre.get()
        apellido = self.ent_apellido.get()
        membresia = self.ent_membresia.get()

        if not nombre.strip() or not apellido.strip() or not membresia.strip():
            showerror(title="Error", message="Todos los campos son obligatorios y no pueden estar vacios")
            return

        if not self.validar_membresia():
            showerror(title="Atención!", message="El valor de membresia no es Numerico")
            self.ent_membresia.delete(0, tk.END)
            self.ent_membresia.focus_set()
            return

        if self.id_seleccionado is None:
            # Agrega nuevo cliente
            self.guardar_datos(nombre, apellido, membresia)
        else:
            # Si el registro cliente ya existe lo actualiza
            self.actualizar_datos(self.id_seleccionado, nombre, apellido, membresia)

        self.limpiar_entry()
        self.refrescar_tabla()


    def validar_membresia(self):
        try:
            int(self.ent_membresia.get())
            return True
        except:
            return False


    def guardar_datos(self, nombre, apellido, membresia):
            # Crea un nuevo cliente
        guardar_cliente = self.cliente_service.crear_cliente(nombre, apellido, membresia)
        if guardar_cliente:
            showinfo(title="Exito", message=f"Se guardo el cliente {nombre} {apellido}")

        else:
            showerror(title="Error", message=guardar_cliente)


    def actualizar_datos(self, cliente_id, nombre, apellido, membresia):
        cliente_actualizado = self.cliente_service.actualizar_cliente(cliente_id, nombre, apellido, membresia)
        if cliente_actualizado:
            self.limpiar_entry()
            self.refrescar_tabla()
            showinfo(title="Exito!", message=f"Cliente {nombre}, se actualizo correctamente!")
        else:
            showerror(title="Error", message="Ocurrio un error")


if __name__ == "__main__":
    app = App()
    app.mainloop()