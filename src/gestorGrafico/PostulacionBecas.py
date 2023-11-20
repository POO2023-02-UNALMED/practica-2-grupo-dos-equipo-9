from tkinter import *
from gestorGrafico.CrearBeca import CrearBeca
from gestorGrafico.EliminarBeca import EliminarBeca
from gestorGrafico.AplicarBeca import AplicarBeca
from gestorGrafico.MostrarBeca import MostrarBeca
from gestorGrafico.FieldFrame import FieldFrame

class PostulacionBecas(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#000000",highlightthickness=3)
        self.pack(expand=True)
        
        def mostrarBeca():
            self.pack_forget()
            mBeca = MostrarBeca(ventana)
            mBeca.pack()

        def aplicarBeca():
            self.pack_forget()
            aBeca = AplicarBeca(ventana)
            aBeca.pack()

        def becaNueva():
            self.pack_forget()
            cBeca = CrearBeca(ventana)
            cBeca.pack()

        def eliminarBeca():
            self.pack_forget()
            eBeca = EliminarBeca(ventana)
            eBeca.pack()
      
         
        tituloenventana = Label(self, text="Búsqueda y Postulación de Becas", bg="black", foreground="white", font=("Helvetica", 14, "bold"))  # Fondo gris, texto blanco
        tituloenventana.pack(side="top", anchor="c", padx=5, pady=5)
        textodescriptivo = ("Esta funcionalidad permite:\n1.Ver listado de becas existentes actualmente. \n2.Aplicar beca a estudiante." +
                           "\n3.Crear nueva beca. \n4.Eliminar beca.")
        descripcion = Label(self, text=textodescriptivo, font=("Arial", 11), bg="white", fg="black")  # Fondo gris, texto blanco
        descripcion.pack(anchor="n", pady=20, padx=5)

        seleccion = Frame(self, bg="#000000")  # Fondo negro
        seleccion.pack(padx=5, pady=5)

        mostrarB = Button(seleccion, text="Mostrar listado de becas", foreground="black", background="white", font=("Helvetica", 12), command=mostrarBeca)  # Texto blanco, fondo azul oscuro
        mostrarB.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        aplicarB = Button(seleccion, text="Aplicar beca a estudiante", foreground="black", background="white", font=("Helvetica", 12), command=aplicarBeca)  # Texto blanco, fondo azul oscuro
        aplicarB.grid(row=0,column=1,padx=10,pady=10,sticky="w")

        crearB = Button(seleccion, text="Crear nueva beca", foreground="black", background="white", font=("Helvetica", 12), command=becaNueva)  # Texto blanco, fondo azul oscuro
        crearB.grid(row=1,column=0,padx=45,pady=10,sticky="w")

        eliminarB = Button(seleccion, text="Eliminar beca", foreground="black",background="white",font=("Helvetica", 12), command= eliminarBeca)
        eliminarB.grid(row=1,column=1,padx=50,pady=10,sticky="w")

