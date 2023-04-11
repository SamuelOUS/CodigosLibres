from ProyectoRequisitos.Formulario.Registration.register_data_design import RegistrationWindowDesign
from tkinter import messagebox


class RegistrationWindowData(RegistrationWindowDesign):
    Users = {}
    NumberUsers = 0

    def data(self):

        user = self.usuario.get()
        password = self.password.get()

        if user == "" and password == "":
            messagebox.showerror(message="Datos vacios", title="Error")

        elif RegistrationWindowData.Users.__contains__(user):
            messagebox.showerror(message="Usuario ya registrado", title="Error")
        else:
            RegistrationWindowData.Users[user] = password
            self.ventana.destroy()
