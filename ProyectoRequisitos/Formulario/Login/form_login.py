from ProyectoRequisitos.Formulario.Login.form_login_design import FormLoginDesign
from ProyectoRequisitos.Formulario.Registration.register_data_design import RegistrationWindowDesign


class FormLogin(FormLoginDesign):

    def verificar(self):
        pass

    def user_register(self):
        self.ventana.destroy()
        RegistrationWindowDesign()
