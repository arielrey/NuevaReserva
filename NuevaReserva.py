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

        # Crear un Canvas para el fondo general
        self.canvas = tk.Canvas(self, width=1343, height=900)
        self.canvas.pack(fill="both", expand=True)

        # Cargar la imagen de fondo
        fondo_img = tk.PhotoImage(file="fondo.png")
        self.canvas.create_image(0, 0, anchor="nw", image=fondo_img)
        # Evitar que la imagen sea eliminada por el recolector de basura
        self.canvas.fondo_img = fondo_img

        # Logo
        self.logo_frame = tk.Frame(self, width=60, height=35)  # Frame reducido
        self.logo_frame.place(relx=0.5, anchor="center", y=50)
        self.logo_frame.configure(background="black")

        # Cargar la imagen de logo con Pillow y eliminar los bordes
        original_img = Image.open("logo.png")
        # Reducir el tamaño de la imagen
        original_img = original_img.resize((40, 40))
        logo_img = ImageTk.PhotoImage(original_img)

        logo_label = tk.Label(self.logo_frame, image=logo_img)
        # Evitar que la imagen sea eliminada por el recolector de basura
        logo_label.image = logo_img
        logo_label.pack()

        # Crear un estilo para los Entry widgets
        estilo = ttk.Style()
        # Establecer el relleno (padding) para los Entry widgets
        estilo.configure("TEntry", padding=(5, 5, 5, 5))

        # Establecer el fondo del cuaderno de pestanas
        estilo.configure("TNotebook", background="black", fg="white")
        estilo.configure("TNotebook.Tab", background="black",
                         foreground="black")  # Establecer el fondo de los tabs

        # Cuaderno de pestañas
        self.pestanas = ttk.Notebook(self)
        self.pestanas.place(x=420, y=100, width=500)

        self.crear_tab()
        self.ver_tab()
        self.modificar_tab()
        self.borrar_tab()

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

    # --- Frames de Solapas ---

    # frame crear
    def crear_frame_content(self, parent):
        frame = tk.Frame(parent)
        frame.pack(padx=10, pady=10)
        nombre_label = tk.Label(
            frame, text="\nCrear reserva", font=("Arial", 14, "bold"))
        nombre_label.pack()
        id_mesa_crear_label = tk.Label(
            frame, text="\nId de mesa:")
        id_mesa_crear_label.pack()
        self.id_mesa_crear_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.id_mesa_crear_entry.pack(padx=10, pady=5)
        self.id_reserva_modificar_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        nombre_label = tk.Label(frame, text="\nNombre:")
        nombre_label.pack()
        self.nombre_crear_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.nombre_crear_entry.pack(padx=10, pady=5)
        apellido_label = tk.Label(frame, text="\nApellido:")
        apellido_label.pack()
        self.apellido_crear_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.apellido_crear_entry.pack(padx=10, pady=5)
        dni_crear_label = tk.Label(frame, text="\nDNI:")
        dni_crear_label.pack()
        self.dni_crear_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.dni_crear_entry.pack(padx=10, pady=5)
        telefono_label = tk.Label(frame, text="\nTeléfono:")
        telefono_label.pack()
        self.telefono_crear_entry = ttk.Entry(frame, style="TEntry", font=(
            "Arial", 12), background="#59F5D6")
        self.telefono_crear_entry.pack(padx=10, pady=5)
        fecha_crear_label = tk.Label(frame, text="\nFecha:")
        fecha_crear_label.pack()
        self.fecha_crear_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.fecha_crear_entry.pack(padx=10, pady=5)
        hora_crear_label = tk.Label(frame, text="\nHora:")
        hora_crear_label.pack()
        self.hora_crear_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.hora_crear_entry.pack(padx=10, pady=5)
        action_button = tk.Button(frame, text="Crear", bg="green", fg="white", font=(
            "Arial", 14, "bold"), command=self.crear_reserva)
        action_button.pack(padx=10, pady=10)

    # frame ver

    def ver_frame_content(self, parent):
        frame = tk.Frame(parent)
        frame.pack(padx=10, pady=10)
        # Widgets específicos para Ver Reserva
        ver_label = tk.Label(frame, text="\nVer reserva",
                             font=("Arial", 14, "bold"))
        ver_label.pack()
        nombre_ver_label = tk.Label(frame, text="\nNombre:")
        nombre_ver_label.pack()
        self.nombre_ver_entry = ttk.Entry(frame, font=("Arial", 12))
        self.nombre_ver_entry.pack(padx=10, pady=5)
        telefono_ver_label = tk.Label(frame, text="\nTeléfono:")
        telefono_ver_label.pack()
        self.telefono_ver_entry = ttk.Entry(frame, font=("Arial", 12))
        self.telefono_ver_entry.pack(padx=10, pady=5)
        ver_button = tk.Button(frame, text="Ver", bg="blue",
                               fg="white", font=("Arial", 14, "bold"))
        ver_button.pack(padx=10, pady=10)

    # frame modificar
    def modificar_frame_content(self, parent):
        frame = tk.Frame(parent)
        frame.pack(padx=10, pady=10)
        modificar_label = tk.Label(
            frame, text="\nModificar reserva", font=("Arial", 14, "bold"))
        modificar_label.pack()
        id_reserva_modificar_label = tk.Label(
            frame, text="\nId de reserva:")
        id_reserva_modificar_label.pack()
        self.id_reserva_modificar_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.id_reserva_modificar_entry.pack(padx=10, pady=5)
        nombre_modificar_label = tk.Label(frame, text="\nNombre:")
        nombre_modificar_label.pack()
        self.nombre_modificar_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.nombre_modificar_entry.pack(padx=10, pady=5)
        apellido_modificar_label = tk.Label(frame, text="\nApellido:")
        apellido_modificar_label.pack()
        self.apellido_modificar_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.apellido_modificar_entry.pack(padx=10, pady=5)
        telefono_modificar_label = tk.Label(frame, text="\nTeléfono:")
        telefono_modificar_label.pack()
        self.telefono_modificar_entry = ttk.Entry(frame, style="TEntry", font=(
            "Arial", 12), background="#59F5D6")
        self.telefono_modificar_entry.pack(padx=10, pady=5)
        fecha_modificar_label = tk.Label(frame, text="\nFecha:")
        fecha_modificar_label.pack()
        self.fecha_modificar_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.fecha_modificar_entry.pack(padx=10, pady=5)
        hora_modificar_label = tk.Label(frame, text="\nHora:")
        hora_modificar_label.pack()
        self.hora_modificar_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.hora_modificar_entry.pack(padx=10, pady=5)
        mesa_modificar_label = tk.Label(frame, text="\nMesa:")
        mesa_modificar_label.pack()
        self.mesa_modificar_entry = ttk.Entry(
            frame, style="TEntry", font=("Arial", 12))
        self.mesa_modificar_entry.pack(padx=10, pady=5)

        # Botón de acción
        action_button = tk.Button(
            frame, text="Modificar", bg="orange", fg="white", font=("Arial", 14, "bold"))
        action_button.pack(padx=10, pady=10)

    # frame borrar
    def borrar_frame_content(self, parent):
        frame = tk.Frame(parent)
        frame.pack(padx=10, pady=10)
        borrar_label = tk.Label(
            frame, text="\nBorrar reserva", font=("Arial", 14, "bold"))
        borrar_label.pack()

        # Widgets específicos para Borrar Reserva
        nombre_borrar_label = tk.Label(frame, text="\nNombre:")
        nombre_borrar_label.pack()
        self.nombre_borrar_entry = ttk.Entry(frame, font=("Arial", 12))
        self.nombre_borrar_entry.pack(padx=10, pady=5)
        telefono_borrar_label = tk.Label(frame, text="\nTeléfono:")
        telefono_borrar_label.pack()
        self.telefono_borrar_entry = ttk.Entry(frame, font=("Arial", 12))
        self.telefono_borrar_entry.pack(padx=10, pady=5)
        borrar_button = tk.Button(frame, text="Borrar", bg="red",
                                  fg="white", font=("Arial", 14, "bold"))
        borrar_button.pack(padx=10, pady=10)

    # Funciones para interactuar con la base de datos

        ######################################################################

    def crear_reserva(self):
        # Obtener datos del formulario
        mesa = self.id_mesa_crear_entry.get()
        nombre = self.nombre_crear_entry.get()
        apellido = self.apellido_crear_entry.get()
        dni = self.dni_crear_entry.get()
        telefono = self.telefono_crear_entry.get()
        fecha = self.fecha_crear_entry.get()
        hora = self.hora_crear_entry.get()

        # Establecer la conexión a la base de datos (reemplaza los valores con los de tu base de datos)
        conn = mysql.connector.connect(
            host="localhost", user="root", password="44602955", database="bar")
        cursor = conn.cursor()

        # Crear la consulta SQL para insertar un nuevo registro en la tabla cliente
        consulta_crear_cliente = "INSERT INTO cliente (nombre, apellido, dni, telefono) VALUES (%s, %s, %s, %s)"
        datos_cliente = (nombre, apellido, dni, telefono)

        # Ejecutar la consulta SQL para la tabla cliente
        cursor.execute(consulta_crear_cliente, datos_cliente)

        # Obtener el ID del cliente recién insertado
        id_cliente = cursor.lastrowid

        # Crear la consulta SQL para insertar un nuevo registro en la tabla reserva
        consulta_crear_reserva = "INSERT INTO reserva (id_mesa, id_cliente, fecha, hora) VALUES (%s, %s, %s, %s)"
        datos_crear_reserva = (mesa, id_cliente, fecha, hora)

        # Ejecutar la consulta SQL para la tabla reserva
        cursor.execute(consulta_crear_reserva, datos_crear_reserva)

        # Commit para aplicar los cambios en la base de datos
        conn.commit()

        # Cerrar la conexión
        conn.close()

        # Realizar la operación de creación en la base de datos usando los datos obtenidos

    def ver_reserva(self):
        # Obtener datos del formulario
        nombre = self.nombre_ver_entry.get()
        telefono = self.telefono_ver_entry.get()

        # Realizar la operación de consulta en la base de datos usando los datos obtenidos

    # def modificar_reserva(self):
        # Obtener datos del formulario
        # Realizar la operación de modificación en la base de datos usando los datos obtenidos

    # def borrar_reserva(self):
        # Obtener datos del formulario
        # Realizar la operación de borrado en la base de datos usando los datos obtenidos


app = VentanaPestanas()
app.mainloop()