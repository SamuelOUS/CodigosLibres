import tkinter as tk


class MasterPanelDesign:

    def crear_presupuesto(self):
        pass

    def borrar_presupuesto(self):
        pass

    def cerrar_sesion(self):
        pass

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Gestion personal')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("990x680")
        self.ventana.config(bg='#3A536D')
        self.ventana.resizable(False, False)

        frame_menu = tk.Frame(self.ventana, bd=0, width=300, padx=10, pady=10, bg="#1E3247")
        frame_menu.pack(side="left", expand=tk.NO, fill=tk.BOTH)

        frame_app = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#28435F")
        frame_app.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        frame_form_line = tk.Frame(self.ventana, bg="black", bd=0,height=900)
        frame_form_line.pack(side="bottom", expand=tk.YES, fill=tk.X)

        label_bot = tk.Label(frame_app, fg="white", bg="white", pady=0, height=9)
        label_bot.pack(expand=tk.NO, fill=tk.X, side="bottom")

        label_menu = tk.Label(frame_menu, bg="black", pady=0, height=9)
        label_menu.pack(fill=tk.X, side="bottom")

        presupuesto_actual = "0"

        label_presupuesto = tk.Label(frame_app, bg="#28435F", text=presupuesto_actual, font=('Times', 70))
        label_presupuesto.place(x=385, y=200)

        money_button = tk.Button(label_bot, text="presupuestos", bg="white", height=2,font=('Times', 14), relief="solid", border=0)
        money_button.pack(expand=tk.YES, fill=tk.X, side="bottom")

        log_out_button = tk.Button(label_menu, text="cerrar sesion", bg="#233B4E", width=20, font=('Times', 9), relief="solid", border=0)
        log_out_button.pack( side="bottom")

        crear_ppresupuesto_button = tk.Button(frame_app, text="crear presupuesto", bg="#28435F", fg="white",width=20, font=('Times', 12),relief="solid", border=0)
        crear_ppresupuesto_button.place(x=320, y=420)

        self.ventana.mainloop()


MasterPanelDesign()