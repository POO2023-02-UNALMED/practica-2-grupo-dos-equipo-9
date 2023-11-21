from tkinter import *
from gestorGrafico.ventPrincipal import VentPrincipal

class VentInicio(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)       
        self.pack()
        
        # Creacion de Frames

        p1Frame=Frame(self,height=450,width=425,bg="gray")
        p1Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=(5,0),pady=5)
        p1Frame.grid_propagate(False)

        p2Frame=Frame(self,height=450,width=425,bg="gray")
        p2Frame.grid(row=0,column=1,columnspan=1,rowspan=1,padx=(0,5),pady=5)
        p2Frame.grid_propagate(False)

        p3Frame=Frame(p1Frame,height=70,width=415,bg="black")
        p3Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=5,pady=(5,3))
        p3Frame.pack_propagate(False)

        p4Frame=Frame(p1Frame,height=365,width=415,bg="gray")
        p4Frame.grid(row=1,column=0,columnspan=2,rowspan=1,padx=5,pady=(3,5))
        p4Frame.pack_propagate(False)

        p5Frame=Frame(p2Frame,height=100,width=415,bg="yellow")
        p5Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=5,pady=(5,3))
        p5Frame.pack_propagate(False)

        p6Frame=Frame(p2Frame,height=335,width=335,bg="black")
        p6Frame.grid(row=1,column=0,columnspan=2,rowspan=1,padx=5,pady=(3,5))
        p6Frame.grid_propagate(False)

        # Frame 3 Saludo bienvenida
        mensaje="Bienvenido al Sistema De Información Academica"
        mensajeBienv = Label(p3Frame,text=mensaje,font=("Trebuchet MS", 18, "bold"),bg="black",wraplength=415,fg="white")
        mensajeBienv.pack(expand=True)

        # Frame 5 Bibliografia de cada desarrollador
        bibi1="Mi nombre es Ricardo Lopera, soy estudiante de ciencias de la computacion y matematicas, me gusta acampar y el senderismo, disfruto del rap y el punk, y en mi tiempo libre me gusta tomar cerveza"
        bibi2="Mi nombre es Yiduar Duvier Rangel Quintero. Soy estudiante de Ingeniería de Sistemas en la UNALMED. Me encantan los raspados y las salchipapas. En mi tiempo libre, disfruto explorar Colombia y pasar tiempo con mis amigos."
        
         
        self.biblios = [bibi1,bibi2]

        self.punteroIntergrante =1
        def cambiarTextoEImagenF6(evento):
            i=self.punteroIntergrante
            
            # Cambio de texto
            evento.widget["text"]=self.biblios[i]
            
            # Cambio de imagenes
            
            imag1=PhotoImage(file=f"src\gestorGrafico\Imagenes\imgIn{i+1}_1.png")     
            imag2=PhotoImage(file=f"src\gestorGrafico\Imagenes\imgIn{i+1}_2.png")     
            imag3=PhotoImage(file=f"src\gestorGrafico\Imagenes\imgIn{i+1}_3.png")     
            imag4=PhotoImage(file=f"src\gestorGrafico\Imagenes\imgIn{i+1}_4.png")     
            
            global lisImagenes # Es global para no perder el puntero de las imagenes cuando el metodo finalice
            lisImagenes=[imag1,imag2,imag3,imag4]
            
            setCuatroImagenes(lisImagenes)
            
            # Cambio de puntero  
            i+=1
            n =5 # numero de grupo de fotos en la carpeta imagenes, cuando se tengan todas debe ser 5
            if i ==n:
                self.punteroIntergrante= 0
            else:
                self.punteroIntergrante=i
            

        biblioTexto = Label(p5Frame,text=bibi1,font=("Comic Sans MS", 10),bg="black",wraplength=405,highlightbackground="black",highlightthickness=2, fg="white")
        biblioTexto.pack(expand=True,fill="both")
        biblioTexto.bind("<Button-1>",cambiarTextoEImagenF6)


        # Frame 6 Imagenes:
        def setCuatroImagenes(packImagenes):
            img1.config(image=packImagenes[0])
            img2.config(image=packImagenes[1])
            img3.config(image=packImagenes[2])
            img4.config(image=packImagenes[3])

        tam=157

        self.image1 =PhotoImage(file="src\gestorGrafico\Imagenes\imgIn1_1.png")
        self.image2 =PhotoImage(file="src\gestorGrafico\Imagenes\imgIn1_2.png")
        self.image3 =PhotoImage(file="src\gestorGrafico\Imagenes\imgIn1_3.png")
        self.image4 =PhotoImage(file="src\gestorGrafico\Imagenes\imgIn1_4.png")


        img1 = Label(p6Frame,image=self.image1,height=tam,width=tam)
        img1.grid(row=0,column=0,columnspan=1,rowspan=1,padx=3,pady=3)

        img2 = Label(p6Frame,image=self.image2,height=tam,width=tam)
        img2.grid(row=0,column=1,columnspan=1,rowspan=1,padx=3,pady=3)

        img3 = Label(p6Frame,image=self.image3,height=tam,width=tam)
        img3.grid(row=1,column=0,columnspan=1,rowspan=1,padx=3,pady=3)

        img4 = Label(p6Frame,image=self.image4,height=tam,width=tam)
        img4.grid(row=1,column=1,columnspan=1,rowspan=1,padx=3,pady=3)
        
        
        # Frame 4
        
        # Imagen:
        self.punteroImagen=2
        def cambiarTextoEImagenF4(evento):
            i=self.punteroImagen

            # Cambio de imagenes
            global imagF4
            imagF4=PhotoImage(file=f"src\gestorGrafico\Imagenes\imgInF4.{i}.png")     
   
            ImagenF4.config(image=imagF4)
            
            # Cambio de puntero  
            i+= 1
            n = 5 # numero de grupo de fotos en la carpeta imagenes, cuando se tengan todas debe ser 5
            if i ==(n+1):
                self.punteroImagen= 1
            else:
                self.punteroImagen=i
        
        self.imagenF41 =PhotoImage(file="src\gestorGrafico\Imagenes\imgInF4.1.png")
        
        ImagenF4 = Label(p4Frame,image=self.imagenF41,width=300,wraplength=160,highlightbackground="black",highlightthickness=4)
        ImagenF4.pack(side="top",pady=3)
        ImagenF4.bind("<Enter>",cambiarTextoEImagenF4)
        
        # Texto descripcion
        
        descripTexto = Label(p4Frame,text="",font=("arial", 10, "bold"),bg="gray",wraplength=400)
        descripTexto.pack(side="top",fill="x",pady=10)
        
        # Boton para pasar
        
        def cambioVentana():
            self.destroy()           
            ventana.abrirLog()
            
        
        botonIngreso=Button(p4Frame,text="Ingresar",command=cambioVentana,bg="black",font=("arial", 12, "bold"),fg="white")
        botonIngreso.pack(side="top",pady=(10,20))
           
        
        # Creacion del menu :U
        ventana.menuBar = Menu(ventana)
        ventana.option_add("*tearOff", False)
        ventana.config(menu=ventana.menuBar)
        menu1 = Menu(ventana.menuBar)
        ventana.menuBar.add_cascade(label="Archivo", menu=menu1)
        menu1.add_command(label="Salir", command=lambda: ventana.destroy())
        
        textDescrip="SDIAcademica Y&R consiste en un sistema de información académica diseñado para mejorar la administración de asignaturas en instituciones educativas. En esencia, está dirigido a los coordinadores de las diferentes instituciones."
        menu1.add_command(label="Descripcion",command=lambda: descripTexto.config(text=textDescrip))
        