from tkinter import *

class App:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Tp prog")
        self.ventana.geometry("400x500")







ventana_principal = Tk()
objVentana = App(ventana_principal)
ventana_principal.mainloop()
