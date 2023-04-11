from ProyectoRequisitos.Formulario.MasterClass.form_master_design import MasterPanelDesign
from tkinter import messagebox
import tkinter as tk


class MasterPanel(MasterPanelDesign):

    def __init__(self):
        super().__init__()
        self.presupuesto = None

    def aceptar(self):

        label_presupuesto = tk.Label(bg="#28435F", text=self.presupuesto.get(), font=('Times', 60), anchor="center")
        label_presupuesto.place(x=555, y=200)

        label_ocultar_1 = tk.Label(text="         ", font=('times', 30), fg="white", bg="#28435F", borderwidth=0,
                                   width=50)
        label_ocultar_1.place(x=450, y=450)

        label_ocultar_2 = tk.Label(text="         ", font=('times', 30), fg="white", bg="#28435F", borderwidth=0,
                                   width=50)
        label_ocultar_2.place(x=520, y=400)

        label_presupuesto_actual = tk.Label(text="presupuesto actual", font=('times', 30), fg="white", bg="#28435F")
        label_presupuesto_actual.place(x=440, y=100)

    def crear_presupuesto(self):

        title = tk.Label(text="introduzca su presupuesto", font=('times', 10), fg="white", bg="#28435F", pady=0,
                         borderwidth=0, relief="groove", )
        title.place(x=520, y=400)

        self.presupuesto = label_presupuesto_entry = tk.Entry(bg="#28435F", font=('Times', 20))
        label_presupuesto_entry.place(x=450, y=450)

        aceptar_button = tk.Button(text="aceptar", bg="#28435F", font=('Times', 9), relief="solid", border=0,
                                   command=self.aceptar)
        aceptar_button.place(x=755, y=455)

        label_presupuesto = tk.Label(bg="#28435F", font=('Times', 60))
        label_presupuesto.place(x=555, y=200)

    def borrar_presupuesto(self):
        Desicion_presupuesto = messagebox.askquestion(title="Cuidado", message="desea borrar su presupuesto actual?")
        if Desicion_presupuesto == "yes":
            label_presupuesto = tk.Label(bg="#28435F", text="                                                                          ", font=('Times', 60))
            label_presupuesto.place(x=555, y=200)

        else:
            messagebox.showinfo(title="info", message="No se borro nada")

    def cerrar_sesion(self):
        messagebox.showinfo(title="info", message="se va a cerrar sesion")
        messagebox.showinfo(title="info", message="La aplicacion va a cerrarse")
        self.ventana.destroy()






