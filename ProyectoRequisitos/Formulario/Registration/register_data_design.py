import tkinter as tk
from tkinter import ttk, messagebox
import ProyectoRequisitos.Util.generic as utl
from ProyectoRequisitos.Formulario.MasterClass.form_master import MasterPanel


class RegistrationWindowDesign:

    def data(self):
        pass

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('registro')
        self.ventana.geometry('800x600')
        self.ventana.config(bg="#F19A83")
        self.ventana.resizable(False, False)
        utl.centrar_ventana(self.ventana, 800, 500)

        logo = utl.leer_imagen("./Images/icono_gestion_personal.png", (100, 100))

        frame_logo = tk.Frame(self.ventana, bd=0, width=300, padx=10, pady=10, bg="white")
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)

        label = tk.Label(frame_logo, image=logo, bg="white")
        label.place(x=0, y=0, relheight=1, relwidth=1)

        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#3D5064")
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="white")
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Introduzca los datos de registro", font=('times', 20), fg="white", bg="#3D5064",
                         pady=50, borderwidth=2, relief="groove", )
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="white")
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="black", bg="white",
                                    anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=210, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="black", bg="white",
                                     anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=195, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)

        register = tk.Button(frame_form_fill, text="Registrar usuario", font=('Times', 15), bg="#556F8A", bd=0,
                             fg="white")
        register.pack(fill=tk.X, padx=20, pady=20)
        register.bind("<Return>", (lambda event: self.data))

        self.ventana.mainloop()
