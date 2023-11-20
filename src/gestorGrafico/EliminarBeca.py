from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gestorAplicacion.administracion.Beca import Beca
from gestorGrafico.FieldFrame import FieldFrame

class EliminarBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#000000", highlightthickness=3, bg="#000000")  # Fondo negro
        self.pack(expand=True)

        def confEliminar():
            quest = messagebox.askokcancel("Confirmar acción", f"¿Está seguro que desea eliminar la beca {comboBecas.get()} del sistema?\n Esta acción será permanente.")
            if quest:
                bec = Beca.buscandoBeca(str(comboBecas.get()))
                try:
                    Beca.eliminarBeca(bec)
                    messagebox.showinfo("Beca eliminada", f"La beca {comboBecas.get()} ha sido eliminada con éxito del sistema")
                except:
                    messagebox.showerror("Error", "Debe seleccionar una beca del listado para poder continuar.")

                

        titulo = Label(self, text="Eliminar Beca", bg="#000000", foreground="#FFFFFF", font=("Helvetica", 14, "bold"))  # Fondo negro, texto blanco
        titulo.pack(side="top", anchor="c")

        textoDesc = ("A continuación, deberá seleccionar de la lista de becas existentes\n cuál de estas desea eliminar.")
        descripcion = Label(self, text=textoDesc, bg="#000000", font=("Arial", 11), fg="#FFFFFF")  # Fondo negro, texto blanco
        descripcion.pack(anchor="n", pady=20)

        becaFrame = Frame(self, bg="#000000")  # Fondo negro
        becaFrame.pack()

        becaTit = Label(becaFrame, text="Becas existentes", bg="#000000", font=("Arial", 11, "bold"), fg="#FFFFFF")  # Fondo negro, texto blanco
        becaTit.grid(row=0, column=0, padx=10, pady=10)

        becasE = Beca.listaBecas()
        textoDefault = StringVar(becaFrame, value= "Seleccione una beca")
        comboBecas = ttk.Combobox(becaFrame, values=becasE, textvariable= textoDefault)
        comboBecas.grid(row=0, column=1, padx=10, pady=10)
        
        boton = Button(self, text="Eliminar Beca", command=confEliminar, font=("Arial", 11, "bold"), fg="#000000", bg="#696969")  # Texto negro, gris
        boton.pack()
