import tkinter as tk
from tkinter.font import BOLD
import ProyectoRequisitos.Util.generic as utl


class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Gestion personal')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("990x680")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(False, False)
        label = tk.Label(self.ventana, bg="#F19A83")
        label.place(x=0, y=0, relheight=1,  relwidth=1)
        self.ventana.mainloop()

