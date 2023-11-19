from tkinter import messagebox
from tkinter import *
from gestorGrafico.DesmatricularAlumno import DesmatricularAlumno
from gestorGrafico.MatricularMateria import MatricularMateria
from gestorGrafico.PostulacionBecas import PostulacionBecas
from gestorGrafico.GenerarHorario import GenerarHorario
from gestorGrafico.eliminarAgregarMateria import EliminarAgregarMateria

class VentPrincipal(Tk):
    def __init__(self):
        super().__init__()
        self.configure_window()
        self.create_menu()
        self.create_main_frame()
        self.mainloop()

    def configure_window(self):
        self.title("SDIAcademica")
        self.resizable(0, 0)
        self.geometry("865x480")
        self.configure(bg="black")
        self.pack_propagate(False)
        self.iconphoto(True, PhotoImage(file="/home/Rick/GitHub/practica-2-grupo-dos-equipo-9/src/gestorGrafico/Imagenes/iconoRY.png"))

    def create_menu(self):
        menuBar = Menu(self)
        self.option_add("*tearOff", False)
        self.config(menu=menuBar)

        menu1 = Menu(menuBar)
        menuBar.add_cascade(label="Archivo", menu=menu1)
        menu1.add_cascade(label="Aplicacion", command=self.info_basica)
        menu1.add_cascade(label="Salir", command=self.salir)

        menu2 = Menu(menuBar)
        menuBar.add_cascade(label="Procesos y Consultas", menu=menu2)
        menu2.add_cascade(label="Matricular materia", command=self.matricular_materia)
        menu2.add_cascade(label="Generar Horario", command=self.generar_horario)
        menu2.add_cascade(label="Eliminar o agregar Materia / Grupo", command=self.eliminar_agregar_materia)
        menu2.add_cascade(label="Desmatricular Alumno", command=self.desmatricular_alumno)
        menu2.add_cascade(label="Busqueda y Postulacion de Becas", command=self.becas)

        menu3 = Menu(menuBar)
        menuBar.add_cascade(label="Ayuda", menu=menu3)
        menu3.add_cascade(label="Acerca de", command=self.mostrar_autores)

    def create_main_frame(self):
        frame = Frame(self)
        frame.pack(anchor="center", expand=True)

        bienvenida_label = Label(frame, text="¡Bienvenidos a la ventana principal, saludan Y&R!", font=("Trebuchet MS", 14), fg="black", bg="gray")
        bienvenida_label.pack(padx=10, pady=10)

        self.imagen = PhotoImage(file="/home/Rick/GitHub/practica-2-grupo-dos-equipo-9/src/gestorGrafico/Imagenes/imgVentPrincipal.png")
        figura = Label(frame, height=108, width=192, image=self.imagen)
        figura.pack(anchor="center")

        informacion = """
        Esta aplicación te permite gestionar la matrícula de los estudiantes de forma eficiente. Aquí puedes realizar las siguientes acciones:

        1. Matricular Materia: Selecciona y matricula las materias para los estudiantes en el período académico actual.
        2. Generar Horario: Crea automáticamente horarios para los estudiantes, evitando conflictos de horarios entre las materias matriculadas.
        3. Agregar o Eliminar Materia/Grupo: Crea nuevas materias y grupos en la base de datos, para ofrecer más opciones a los estudiantes.
        4. Desmatricular Alumno: Cancela la matrícula de un estudiante y retira todas las materias inscritas o una sola materia de tu eleccion.
        5. Búsqueda y Postulación de Becas: Explora las becas disponibles y ayuda a los estudiantes en el proceso de postulación.

        Para comenzar, selecciona la opción deseada en el menú principal en Procesos y Consultas y sigue las instrucciones que se te presenten.

        ¡Disfruta de la experiencia de matricularte de forma rápida y eficaz!
        """

        info_text = Label(frame, text=informacion, font=("Arial", 10), fg="white", bg="black")
        info_text.pack(padx=10, pady=10)

    def info_basica(self):
        texto = """Texto de información básica"""
        messagebox.showinfo("Informacion de la aplicacion", texto)

    def salir(self):
        self.destroy()

    def mostrar_autores(self):
        autores = "Autores de la aplicacion:\n\nYiduar Duvier Rangel Quintero\n\nRicardo Esteban Lopera Vasco\n\n"
        messagebox.showinfo("Autores", autores)

    def matricular_materia(self):
        self.mata_hijos()
        MatricularMateria(self).pack()

    def generar_horario(self):
        self.mata_hijos()
        GenerarHorario(self).pack()

    def eliminar_agregar_materia(self):
        self.mata_hijos()
        EliminarAgregarMateria(self).pack()

    def desmatricular_alumno(self):
        self.mata_hijos()
        DesmatricularAlumno(self).pack()

    def becas(self):
        self.mata_hijos()
        PostulacionBecas(self).pack()

    def mata_hijos(self):
        for widget in self.winfo_children():
            if isinstance(widget, Frame):
                widget.destroy()