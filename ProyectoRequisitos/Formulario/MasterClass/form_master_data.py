from ProyectoRequisitos.Formulario.MasterClass.form_master_design import MasterPanelDesign
from tkinter import messagebox


class MasterPanel(MasterPanelDesign):

    def crear_presupuesto(self):
        pass

    def borrar_presupuesto(self):
        pass

    def cerrar_sesion(self):
        messagebox.showinfo(title="info", message="se va a cerrar sesion")
        self.ventana.destroy()
