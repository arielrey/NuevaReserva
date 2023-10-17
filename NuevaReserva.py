###
### Lineas a modificar para la conexion a la base de datos: 282, 313, 349 y 384
###
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector

class VentanaPestanas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nueva Reserva")
        self.geometry("1343x900")
        self.iconbitmap("logo.ico")

        # -- Crear un Canvas para el fondo general
        self.canvas = tk.Canvas(self, width=1343, height=900)
        self.canvas.pack(fill="both", expand=True)
        fondo_img = tk.PhotoImage(file="fondo.png")
        self.canvas.create_image(0, 0, anchor="nw", image=fondo_img)
        self.canvas.fondo_img = fondo_img

        # -- Logo
        self.logo_frame = tk.Frame(self, width=60, height=35)
        self.logo_frame.place(relx=0.5, anchor="center", y=50)
        self.logo_frame.configure(background="black")
        # -- Cargar la imagen de logo con pillow
        original_img = Image.open("logo.png")
        original_img = original_img.resize((40, 40))
        logo_img = ImageTk.PhotoImage(original_img)
        logo_label = tk.Label(self.logo_frame, image=logo_img)
        logo_label.image = logo_img
        logo_label.pack()

        # -- Estilo de Entry widgets
        estilo = ttk.Style()
        estilo.configure("TEntry", padding=(5, 5, 5, 5))
        # -- Fondo del cuaderno de pestanas
        estilo.configure("TNotebook", background="black", fg="white")
        estilo.configure("TNotebook.Tab", background="black",foreground="black")

        # -- Cuaderno de solapas
        self.pestanas = ttk.Notebook(self)
        self.pestanas.place(x=420, y=100, width=500)
        self.crear_tab()
        self.ver_tab()
        self.modificar_tab()
        self.borrar_tab()

        # -- Funcion de combobox
    def on_combobox_select(self, event):
        selected_option = self.combo.get()


    #
    ##
    ###
    #### Funciones para dividir solapas 
    ###
    ##
    #

    def crear_tab(self):
        crear_tab = ttk.Frame(self.pestanas)
        self.pestanas.add(crear_tab, text=" Crear Reserva ")
        self.crear_frame_content(crear_tab)

    def ver_tab(self):
        ver_tab = ttk.Frame(self.pestanas)
        self.pestanas.add(ver_tab, text=" Ver Reserva ")
        self.ver_frame_content(ver_tab)

    def modificar_tab(self):
        modificar_tab = ttk.Frame(self.pestanas)
        self.pestanas.add(modificar_tab, text=" Modificar Reserva ")
        self.modificar_frame_content(modificar_tab)

    def borrar_tab(self):
        borrar_tab = ttk.Frame(self.pestanas)
        self.pestanas.add(borrar_tab, text=" Borrar Reserva ")
        self.borrar_frame_content(borrar_tab)

    #
    ##
    ###
    #### Funciones del contenido de solapas (contenido de cada frame)
    ###
    ##
    #

        # -- frame crear
    def crear_frame_content(self, parent):
        frame = tk.Frame(parent)
        frame.pack(padx=10, pady=10)
        
        nombre_label = tk.Label(frame, text="\nCrear reserva\n", font=("Arial", 14, "bold"))
        nombre_label.pack()

        self.combo = ttk.Combobox(frame, state="readonly", values=["Familiar", "Una persona", "Dos personas"], style="TEntry")
        self.combo.set("Tipo de mesa             🔽")  # Establece el texto por defecto
        self.combo.bind("<<ComboboxSelected>>", self.on_combobox_select)  # Configura el evento de selección
        self.combo.pack(padx=10, pady=10)

        nombre_label = tk.Label(frame, text="\nNombre:")
        nombre_label.pack()
        self.nombre_crear_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.nombre_crear_entry.pack(padx=10, pady=5)
        
        apellido_label = tk.Label(frame, text="\nApellido:")
        apellido_label.pack()
        self.apellido_crear_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.apellido_crear_entry.pack(padx=10, pady=5)
        
        dni_crear_label = tk.Label(frame, text="\nDNI:")
        dni_crear_label.pack()
        self.dni_crear_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.dni_crear_entry.pack(padx=10, pady=5)
        
        telefono_label = tk.Label(frame, text="\nTeléfono:")
        telefono_label.pack()
        self.telefono_crear_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12), background="#59F5D6")
        self.telefono_crear_entry.pack(padx=10, pady=5)
        
        fecha_crear_label = tk.Label(frame, text="\nFecha:")
        fecha_crear_label.pack()
        self.fecha_crear_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.fecha_crear_entry.pack(padx=10, pady=5)
        
        hora_crear_label = tk.Label(frame, text="\nHora:")
        hora_crear_label.pack()
        self.hora_crear_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.hora_crear_entry.pack(padx=10, pady=5)
        
        action_button = tk.Button(frame, text="Crear", bg="green", fg="white", font=("Arial", 14, "bold"), command=self.crear_reserva)
        action_button.pack(padx=10, pady=10)

        self.resultado_crear_label = tk.Label(frame, text="", font=("Arial", 12, "bold"), fg="green")
        self.resultado_crear_label.pack(padx=10, pady=10)
        
        # -- frame ver
    def ver_frame_content(self, parent):
        frame = tk.Frame(parent)
        frame.pack(padx=10, pady=10)
            #Widgets
        ver_label = tk.Label(frame, text="\nVer reserva", font=("Arial", 14, "bold"))
        ver_label.pack()
        
        nombre_ver_label = tk.Label(frame, text="\nNombre:")
        nombre_ver_label.pack()
        self.nombre_ver_entry = ttk.Entry(frame, font=("Arial", 12))
        self.nombre_ver_entry.pack(padx=10, pady=5)
        
        telefono_ver_label = tk.Label(frame, text="\nTeléfono:")
        telefono_ver_label.pack()
        self.telefono_ver_entry = ttk.Entry(frame, font=("Arial", 12))
        self.telefono_ver_entry.pack(padx=10, pady=5)
        
        ver_button = tk.Button(frame, text="Ver", bg="blue", fg="white", font=("Arial", 14, "bold"), command=self.mostrar_reserva)
        ver_button.pack(padx=10, pady=10)
        
        # Crear un Treeview para mostrar los resultados
        self.resultados_treeview = ttk.Treeview(frame, columns=("id_reserva", "id_mesa", "id_cliente", "fecha", "hora"))
        self.resultados_treeview.heading("#1", text="ID Reserva")
        self.resultados_treeview.heading("#2", text="ID Mesa")
        self.resultados_treeview.heading("#3", text="ID Cliente")
        self.resultados_treeview.heading("#4", text="Fecha")
        self.resultados_treeview.heading("#5", text="Hora")
        self.resultados_treeview["show"] = "headings"
        self.resultados_treeview.pack(padx=10, pady=10)

        recargar_button = tk.Button(frame, text="❌", bg="#CE2828", font=("Arial", 14), command=self.resetear_consulta, fg="white")
        recargar_button.pack(padx=0, pady=0)

        # -- frame modificar
    def modificar_frame_content(self, parent):
        frame = tk.Frame(parent)
        frame.pack(padx=10, pady=10)
        frame.config(width=400)
            #Widgets
        modificar_label = tk.Label(frame, text="\nModificar reserva", font=("Arial", 14, "bold"))
        modificar_label.pack()
        
        id_reserva_modificar_label = tk.Label(frame, text="\nId de reserva:")
        id_reserva_modificar_label.pack()
        self.id_reserva_modificar_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.id_reserva_modificar_entry.pack(padx=10, pady=5)
        
        nombre_modificar_label = tk.Label(frame, text="\nNombre:")
        nombre_modificar_label.pack()
        self.nombre_modificar_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.nombre_modificar_entry.pack(padx=10, pady=5)
        
        apellido_modificar_label = tk.Label(frame, text="\nApellido:")
        apellido_modificar_label.pack()
        self.apellido_modificar_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.apellido_modificar_entry.pack(padx=10, pady=5)
        
        telefono_modificar_label = tk.Label(frame, text="\nTeléfono:")
        telefono_modificar_label.pack()
        self.telefono_modificar_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12), background="#59F5D6")
        self.telefono_modificar_entry.pack(padx=10, pady=5)
        
        fecha_modificar_label = tk.Label(frame, text="\nFecha:")
        fecha_modificar_label.pack()
        self.fecha_modificar_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.fecha_modificar_entry.pack(padx=10, pady=5)
        
        hora_modificar_label = tk.Label(frame, text="\nHora:")
        hora_modificar_label.pack()
        self.hora_modificar_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.hora_modificar_entry.pack(padx=10, pady=5)
        
        mesa_modificar_label = tk.Label(frame, text="\nMesa:")
        mesa_modificar_label.pack()
        self.mesa_modificar_entry = ttk.Entry(frame, style="TEntry", font=("Arial", 12))
        self.mesa_modificar_entry.pack(padx=10, pady=5)
        
        action_button = tk.Button(frame, text="Modificar", bg="orange", fg="white", font=("Arial", 14, "bold"), command=self.modificar_reserva)
        action_button.place(y=606, x=10)
        action_button.pack(padx=5, pady=10)

        recargar_button = tk.Button(frame,text="❌", bg="#CE2828", font=("Arial", 14), command=self.resetear_consulta, fg="white")
        recargar_button.pack(padx=2, pady=5)
        recargar_button.place(y=606, x=200)

        self.resultado_modificar_label = tk.Label(frame, text="", font=("Arial", 12, "bold"), fg="green")
        self.resultado_modificar_label.pack(padx=10, pady=10)
      
    # frame borrar
    def borrar_frame_content(self, parent):
        frame = tk.Frame(parent)
        frame.pack(padx=10, pady=10)
            #Widgets
        borrar_label = tk.Label(frame, text="\nBorrar reserva", font=("Arial", 14, "bold"))
        borrar_label.pack()
        
        nombre_borrar_label = tk.Label(frame, text="\nNombre:")
        nombre_borrar_label.pack()
        self.nombre_borrar_entry = ttk.Entry(frame, font=("Arial", 12))
        self.nombre_borrar_entry.pack(padx=10, pady=5)
        
        telefono_borrar_label = tk.Label(frame, text="\nTeléfono:")
        telefono_borrar_label.pack()
        self.telefono_borrar_entry = ttk.Entry(frame, font=("Arial", 12))
        self.telefono_borrar_entry.pack(padx=10, pady=5)
        
        borrar_button = tk.Button(frame, text="Borrar", bg="red", fg="white", font=("Arial", 14, "bold"), command=self.borrar_reserva)
        borrar_button.pack(padx=10, pady=10)

        self.resultado_borrar_label = tk.Label(frame, text="", font=("Arial", 12, "bold"), fg="green")
        self.resultado_borrar_label.pack(padx=10,pady=10)

    #
    ##
    ###
    #### Funciones para interactuar con la base de datos
    ###
    ## 
    #

    def crear_reserva(self):
        mesa = self.combo.current()
        nombre = self.nombre_crear_entry.get()
        apellido = self.apellido_crear_entry.get()
        dni = self.dni_crear_entry.get()
        telefono = self.telefono_crear_entry.get()
        fecha = self.fecha_crear_entry.get()
        hora = self.hora_crear_entry.get()

        if mesa == "Familiar":
            mesa == 1
        elif mesa == "Una persona":
            mesa == 2
        elif mesa == "Dos personas":
            mesa == 3
        elif not mesa or not nombre or not apellido or not dni or not telefono or not fecha or not hora:
            mensaje = "Debe completar todos los campos."
            self.resultado_crear_label.config(text=mensaje, fg="red")
            return
        try:
            # Modificar los datos si es necesario
            conn = mysql.connector.connect(host="localhost", user="root", password="???", database="bar")
            cursor = conn.cursor()
            # Consulta para crear el cliente
            consulta_crear_cliente = "INSERT INTO cliente (nombre, apellido, dni, telefono) VALUES (%s, %s, %s, %s)"
            datos_cliente = (nombre, apellido, dni, telefono)
            cursor.execute(consulta_crear_cliente, datos_cliente)
            id_cliente = cursor.lastrowid
            # Consulta para crear la reserva
            consulta_crear_reserva = "INSERT INTO reserva (id_mesa, id_cliente, fecha, hora) VALUES (%s, %s, %s, %s)"
            datos_crear_reserva = (mesa, id_cliente, fecha, hora)
            cursor.execute(consulta_crear_reserva, datos_crear_reserva)
            conn.commit()
            conn.close()
            mensaje = "La reserva fue creada con éxito."
            self.resultado_crear_label.config(text=mensaje, fg="green")
        except mysql.connector.Error as err:
            mensaje = "No se pudo crear la reserva."
            self.resultado_crear_label.config(text=mensaje, fg="red")

        self.combo.set("Tipo de mesa             🔽")
        self.nombre_crear_entry.delete(0, tk.END)
        self.apellido_crear_entry.delete(0, tk.END)
        self.telefono_crear_entry.delete(0, tk.END)
        self.dni_crear_entry.delete(0, tk.END)
        self.fecha_crear_entry.delete(0, tk.END)
        self.hora_crear_entry.delete(0, tk.END)

    def mostrar_reserva(self):
        nombre = self.nombre_ver_entry.get()
        telefono = self.telefono_ver_entry.get()            
        # Modificar los datos si es necesario
        conn = mysql.connector.connect(host="localhost", user="root", password="???", database="bar")
        cursor = conn.cursor()
        consulta_ver_reserva = "SELECT * FROM reserva R INNER JOIN cliente C ON R.id_cliente = C.id_cliente WHERE C.nombre = %s AND C.telefono = %s"
        datos_ver_reserva = (nombre, telefono)
        cursor.execute(consulta_ver_reserva, datos_ver_reserva)
        reservas = cursor.fetchall()
            
            # Limpiar la tabla antes de mostrar nuevos resultados
        for row in self.resultados_treeview.get_children():
            self.resultados_treeview.delete(row)
        if reservas:
            for reserva in reservas:
                self.resultados_treeview.insert("", "end", values=reserva)
        else:
            self.resultados_treeview.insert("", "end", values=("No se encontraron reservas", "", "", "", ""))
            
        conn.close()


    def modificar_reserva(self):
        id_reserva = self.id_reserva_modificar_entry.get()
        nombre = self.nombre_modificar_entry.get()
        apellido = self.apellido_modificar_entry.get()
        telefono = self.telefono_modificar_entry.get()
        fecha = self.fecha_modificar_entry.get()
        hora = self.hora_modificar_entry.get()
        mesa = self.mesa_modificar_entry.get()

        if not id_reserva or not nombre or not apellido or not telefono or not fecha or not hora or not mesa:
            mensaje = "Debe completar todos los campos."
            self.resultado_modificar_label.config(text=mensaje, fg="red")
            self.resultados_text.delete(1.0, tk.END)
            self.resultados_text.insert(tk.END, mensaje)
            return
        try:
            # Modificar los datos si es necesario
            conn = mysql.connector.connect(host="localhost", user="root", password="???", database="bar")
            cursor = conn.cursor()
            # Consulta para modificar la reserva
            consulta_modificar_reserva = "UPDATE reserva SET id_mesa=%s, fecha=%s, hora=%s WHERE id_reserva=%s"
            datos_modificar_reserva = (mesa, fecha, hora, id_reserva)
            cursor.execute(consulta_modificar_reserva, datos_modificar_reserva)
            # Consulta para modificar cliente
            consulta_modificar_cliente = "UPDATE cliente SET nombre=%s, apellido=%s, telefono=%s WHERE id_cliente=(SELECT id_cliente FROM reserva WHERE id_reserva=%s)"
            datos_modificar_cliente = (nombre, apellido, telefono, id_reserva)
            cursor.execute(consulta_modificar_cliente, datos_modificar_cliente)
            conn.commit()
            conn.close()
            self.nombre_modificar_entry.delete(0, tk.END)
            self.apellido_modificar_entry.delete(0, tk.END)
            self.id_reserva_modificar_entry.delete(0, tk.END)
            self.telefono_modificar_entry.delete(0, tk.END)
            self.fecha_modificar_entry.delete(0, tk.END)
            self.hora_modificar_entry.delete(0, tk.END)
            self.mesa_modificar_entry.delete(0, tk.END)

            mensaje = "La reserva fue modificada con éxito."
            self.resultado_modificar_label.config(text=mensaje, fg="green")
        except mysql.connector.Error as err:
            mensaje = "No se pudo modificar la reserva."
            self.resultado_modificar_label.config(text=mensaje, fg="red")

    def borrar_reserva(self):
        nombre = self.nombre_borrar_entry.get()
        telefono = self.telefono_borrar_entry.get()
        if not nombre or not telefono:
            mensaje = "Debe completar los campos"
            self.resultado_borrar_label.config(text=mensaje, fg="red")
            return
        try:
            # Cambiar datos si es necesario
            conn = mysql.connector.connect(host="localhost", user="root", password="???", database="bar")
            cursor = conn.cursor()
            # Borrar reserva
            consulta_borrar_reserva = "DELETE FROM reserva WHERE id_cliente IN (SELECT id_cliente FROM cliente WHERE nombre = %s AND telefono = %s)"
            datos_borrar_reserva = (nombre, telefono)
            cursor.execute(consulta_borrar_reserva, datos_borrar_reserva)
            # Borrar el cliente
            consulta_borrar_cliente = "DELETE FROM cliente WHERE nombre = %s AND telefono = %s"
            datos_borrar_cliente = (nombre, telefono)
            cursor.execute(consulta_borrar_cliente, datos_borrar_cliente)
            conn.commit()
            conn.close()
            mensaje = "La reserva fue eliminada con éxito."
            self.resultado_borrar_label.config(text=mensaje, fg="green")
        except mysql.connector.Error as err:
            # Mostrar mensaje de error de conexión a la base de datos
            mensaje = "No se pudo eliminar la reserva."
            self.resultado_borrar_label.config(text=mensaje, fg="red")

        self.nombre_borrar_entry.delete(0, tk.END)
        self.telefono_borrar_entry.delete(0, tk.END)

    # Funcion de boton para resetear los campos de las consultas
    def resetear_consulta(self):
        self.nombre_ver_entry.delete(0, tk.END)
        self.telefono_ver_entry.delete(0, tk.END)
        self.resultados_text.delete(1.0, tk.END)
        self.id_reserva_modificar_entry.delete(0, tk.END)
        self.nombre_modificar_entry.delete(0, tk.END)
        self.apellido_modificar_entry.delete(0, tk.END)
        self.telefono_modificar_entry.delete(0, tk.END)
        self.fecha_modificar_entry.delete(0, tk.END)
        self.hora_modificar_entry.delete(0, tk.END)
        self.mesa_modificar_entry.delete(0, tk.END)

app = VentanaPestanas()
app.mainloop()