from tkinter import messagebox
from ProyectoRequisitos.Formulario.Login.form_login_design import FormLoginDesign
from ProyectoRequisitos.Formulario.MasterClass.form_master_design import MasterPanelDesign
from ProyectoRequisitos.Formulario.Registration.register_data import RegistrationWindowData


class FormLogin(FormLoginDesign):

    def verificar(self):
        user = self.usuario.get()
        password = self.password.get()
        if RegistrationWindowData.Users.get(user) == password:
            self.ventana.destroy()
            MasterPanelDesign()
        else:
            messagebox.showerror(message="Usuario no encontrado o datos incorrectos", title="Error")

    def user_register(self):
        RegistrationWindowData()
