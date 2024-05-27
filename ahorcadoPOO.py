"""
Nombre: largoLista
Entradas: lista
Salidas: El largo de la lista
Restricciones: Debe de ser tipo lista y distinta de vacio
"""


def largoLista(lista):
    resultado = 0
    if (isinstance(lista, list)):
        if (lista != []):
            for elemento in lista:
                resultado += 1
            return resultado
        else:
            return 0
    else:
        return "ERROR: La variable debe de ser tipo lista"


palabraJuego = ""
vidasJuego = 6
aciertos = 0
letrasUsadas = ""
palabraEnJuego = ""
palabraRes = ""
tiempo = '00:00:00'

contador = 0
correr = False

"""
Nombre: numeroRandom
Entrada: rango
Salida: un numero al azar
Restricciones: nula
"""
def numeroRandom(rango):
    numeroRandom = random.randint(0, rango)
    return numeroRandom



"""
Nombre: palabraPrinci
Entrada: inputs
Salida: palabra de modo de juego principiante
Restricciones: nula
"""
def palabraPrinci(lista):
    largo = largoLista(lista)
    rango = numeroRandom(largo-1)
    palabra = lista[rango]
    return palabra

"""
Nombre: contarDigitos
Entradas: num
Salidas: Digitos del num
Restricciones: num debe de ser entero
"""


def contarDigitos(num):
    if (isinstance(num, int)):
        digitos = 0
        if (num != 0):
            while (num > 0):
                num = num // 10
                digitos += 1
        else:
            digitos = 1
        return digitos


"""
Nombre: largoTexto
Entradas: texto
Salidas: Cantidad de Caracteres dentro del texto
Restricciones: Debe de ser un string
"""


def largoTexto(texto):
    if (isinstance(texto, str)):
        valor = 0
        for elemento in texto:
            valor += 1
        return valor
    else:
        return 0


"""
Nombre: buscarEnTexto
Entradas: nombreArchivo,  textoABuscar
Salidas: True y False
Restricciones: textoABuscar debe ser string
"""


def buscarEnTexto(textoBase, textoABuscar):
    if (textoBase == ""):
        return False
    else:
        return buscarEnTexto_Aux(textoBase, textoABuscar)


def buscarEnTexto_Aux(textoBase, textoABuscar):
    resultado = False
    largo = largoTexto(textoABuscar)

    while (textoBase != ""):
        texto = textoBase[0:largo]
        if (texto == textoABuscar):
            resultado = True
            break
        textoBase = textoBase[1:]
    return resultado


"""
Nombre: buscarEnLista
Entradas: lista, buscar
Salidas: True si se encuentra, Flase si no
Restricciones: lista debe ser tipo lista
"""


def buscarEnLista(lista, buscar):
    if (isinstance(lista, list)):
        for elemento in lista:
            if (elemento == buscar):
                return True
            else:
                continue
        return False


#################################################################################

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, Image
import random
from tkinter import ttk

"""
Nombre: Constructor de Ventana
Entradas: Interfaz
Salidas: Ventana de TKinter
Restricciones:
"""


class Ventana:
    contra = ""
    listaPalabras = ["PIZARRA", "TELEFONO", "TECLADO", "PANTALLA", "MESA", "CASA", "ANIMALES", "FUTBOL", "FOTO"]
    listaFrases = ["MIGUEL ANUEL", "COSCULLUELA RODILLA", "AGREGAR CASA"]
    listaPalabrasIngles = ["ANIMALS", "BLACKBOARD", "CAR", "KEYBOARD", "PHONE", "PHOTO", "SCREEN", "TABLE"]
    listaFrasesIngles = ["PINK BALL", "BIG HOUSE", "RED KEYBOARD", "BLUE CAP"]
    palabraJugar = ""
    juegos = []

    def  __init__(self, interfaz):
        self.interfaz = interfaz
        self.interfaz.geometry("500x300")
        self.interfaz.title("Juego Ahorcado")
        self.interfaz.resizable(0, 0)
        self.menuBar()
        self.img = Image.PhotoImage(Image.open(r'C:\Users\Gadyr\Downloads\fondo.jpg').resize((500, 300)))
        self.img1 = Image.PhotoImage(Image.open(r'C:\Users\Gadyr\Downloads\fondo1.jpg').resize((500, 300)))
        self.imgInicio = Image.PhotoImage(Image.open(r'C:\Users\Gadyr\Downloads\inicio.jpg').resize((500, 300)))

        self.interfaz.rowconfigure(0, weight=1)
        self.interfaz.columnconfigure(0, weight=1)

        self.pg1 = Frame(self.interfaz)
        self.pg2 = Frame(self.interfaz)
        self.pg3 = Frame(self.interfaz)
        self.pg4 = Frame(self.interfaz)
        self.pg5 = Frame(self.interfaz)
        self.pg6 = Frame(self.interfaz)
        self.pg7 = Frame(self.interfaz)
        self.pg8 = Frame(self.interfaz)
        self.pg9 = Frame(self.interfaz)
        self.image = imgLabel = Label(self.pg9, image=self.imgInicio).place(x=0, y=0)

        for pagina in (self.pg1, self.pg2, self.pg3, self.pg4, self.pg5, self.pg6, self.pg7, self.pg8, self.pg9):
            pagina.grid(row=0, column=0, sticky="nsew")

        Ventana.mostrarPagina(self, self.pg9)

    """
    Nombre: menuBar
    Entradas: self
    Salidas: Barra de menu en la ventana
    Restricciones:
    """

    def menuBar(self):
        menuBar = Menu(self.interfaz)
        menu1 = Menu(menuBar)
        menu2 = Menu(menuBar)

        menu1.add_command(label="Gestion de Palabras", command=lambda: Acceso.__init__(self, "palabras"))
        menu1.add_command(label="Gestion de Frases", command=lambda: Acceso.__init__(self, "frases"))

        menu2.add_command(label="Nuevo Juego", command=lambda: Ahorcado.__init__(self))
        menu2.add_command(label="Historia", command=lambda: Historia.__init__(self))
        menu2.add_command(label="Ayuda", command=lambda: Ayuda.__init__(self))
        menu2.add_command(label="Estadisticas", command=lambda: Estadisticas.__init__(self))

        menuBar.add_command(label="Inicio", command=lambda: Ventana.mostrarPagina(self, self.pg9))
        menuBar.add_cascade(label="Administracion", menu=menu1)
        menuBar.add_cascade(label="Jugar", menu=menu2)

        self.interfaz.config(menu=menuBar)

    """
    Nombre: mostrarPagina
    Entradas: self, pagina
    Salidas: Frame que se solicita
    Restricciones:
    """

    def mostrarPagina(self, pagina):
        pagina.tkraise()


"""
Nombre: Constructor de Acceso
Entradas: self, PoF
Salidas: Frame para introducir contraseña
Restricciones:
"""


class Acceso(Ventana):

    def __init__(self, PoF):
        if (Ventana.contra == "acceso"):
            if (PoF == "palabras"):
                Palabras.__init__(self)
            if (PoF == "frases"):
                Frases.__init__(self)
        else:
            self.image = imglabel = Label(self.pg1, image=self.img).place(x=0, y=0)
            Acceso.claveAcceso = StringVar()
            Acceso.PoF = PoF
            Acceso.crearWidgets(self)
            Ventana.mostrarPagina(self, self.pg1)

    """
    Nombre: crearWidgets
    Entradas: self
    Salidas: Widgets necesarios en la ventana
    Restricciones:
    """

    def crearWidgets(self):
        Acceso.marcoPg1 = Frame(self.pg1)
        Acceso.marcoPg1.config(width=265, height=125, bg="black")
        Acceso.marcoPg1.place(x=115, y=70)

        Acceso.fondoPg1 = Frame(Acceso.marcoPg1)
        Acceso.fondoPg1.config(width=263, height=123)
        Acceso.fondoPg1.place(x=1, y=1)

        Acceso.tituloPg1 = Label(self.pg1, text="Acceso", bg="blue", fg="white")
        Acceso.tituloPg1.place(x=125, y=60)

        Acceso.textoPg1 = Label(Acceso.fondoPg1, text="Contraseña: ")
        Acceso.textoPg1.place(x=25, y=15)

        Acceso.entryPg1 = Entry(Acceso.fondoPg1, textvariable=Acceso.claveAcceso, show='*',
                                font=("MS Sans Serif", 12, "bold"), fg="black", bg="white")
        Acceso.entryPg1.place(x=25, y=40)

        Acceso.botonPg1 = Button(Acceso.fondoPg1, text="  Ingresar  ", bg="blue", fg="white", bd=3,
                                 relief="groove", command=lambda: Acceso.evaluarClave(self, Acceso.claveAcceso))
        Acceso.botonPg1.place(x=100, y=85)

    """
    Nombre: evaluarClave
    Entradas: self, claveAcceso
    Salidas: mostrarVentana o messagebox
    Restricciones:
    """

    def evaluarClave(self, claveAcceso):
        archivo = open("Acceso.txt", "r")
        contenido = archivo.read()
        archivo.close()
        claveAcceso = Acceso.entryPg1.get()
        if (claveAcceso == contenido):
            if (Acceso.PoF == "palabras"):
                Acceso.entryPg1.delete(0, END)
                Ventana.contra = "acceso"
                Palabras.__init__(self)
            if (Acceso.PoF == "frases"):
                Acceso.entryPg1.delete(0, END)
                Ventana.contra = "acceso"
                Frases.__init__(self)
        else:
            Acceso.entryPg1.delete(0, END)
            messagebox.showerror("CLAVE INCORRECTA", "Porfavor intentelo de nuevo")


"""
Nombre: Palabras
Entradas: self
Salidas: Frame de Gestion de Palabras
Restricciones:
"""


class Palabras(Ventana):

    def __init__(self):
        self.image = imglabel = Label(self.pg2, image=self.img1).place(x=0, y=0)
        Palabras.crearWidgets(self)
        Ventana.mostrarPagina(self, self.pg2)

    """
    Nombre: crearWidgets
    Entradas: self
    Salidas: Widgets necesarios en la ventana
    Restricciones:
    """

    def crearWidgets(self):
        Palabras.marcoPg2 = Frame(self.pg2)
        Palabras.marcoPg2.config(width=445, height=235, bg="black")
        Palabras.marcoPg2.place(x=25, y=25)

        Palabras.fondoPg2 = Frame(Palabras.marcoPg2)
        Palabras.fondoPg2.config(width=443, height=233)
        Palabras.fondoPg2.place(x=1, y=1)

        Palabras.tituloPg2 = Label(self.pg2, text="Gestion de Palabras", bg="blue", fg="white")
        Palabras.tituloPg2.place(x=35, y=15)

        Palabras.palabraPg2 = Label(Palabras.fondoPg2, text="Palabra: ", fg="black")
        Palabras.palabraPg2.place(x=215, y=15)

        Palabras.Palabra = StringVar()
        Palabras.entryPg2 = Entry(Palabras.fondoPg2, textvariable=Palabras.Palabra,
                                  font=("MS Sans Serif", 12, "bold"), bg="white", fg="black")
        Palabras.entryPg2.place(x=215, y=40)

        Palabras.listaPg2 = Listbox(Palabras.fondoPg2, width=30, selectbackground="blue")
        Palabras.listaPg2.place(x=10, y=15)

        Palabras.añadirPg2 = Button(Palabras.fondoPg2, text=" Agregar ", bg="blue", fg="white",
                                    relief="groove", command=lambda: Palabras.agregarPalabra(self))
        Palabras.añadirPg2.place(x=215, y=75)

        Palabras.eliminarPg2 = Button(Palabras.fondoPg2, text=" Eliminar ", bg="blue", fg="white",
                                      relief="groove", command=lambda: Palabras.eliminarPalabra(self))
        Palabras.eliminarPg2.place(x=282.5, y=75)

        Palabras.modificarPg2 = Button(Palabras.fondoPg2, text=" Modificar ", bg="blue", fg="white",
                                       relief="groove", command=lambda: Palabras.modificarPalabra(self))
        Palabras.modificarPg2.place(x=350, y=75)

        Palabras.contenidoListBox1(self)

    """
    Nombre: contenidoListBox1
    Entradas: self
    Salidas: contenido necesario para la listbox
    Restricciones:
    """

    def contenidoListBox1(self):
        for indice in range(largoLista(Ventana.listaPalabras)):
            Palabras.listaPg2.insert(indice, Ventana.listaPalabras[indice])

    """
    Nombre: agregarPalabra
    Entradas: self
    Salidas: La palabra dentro del listbox
    Restricciones: debe ser palabra y no estar en listbox
    """

    def agregarPalabra(self):
        nuevaPalabra = Palabras.Palabra.get()
        nuevaPalabra = nuevaPalabra.upper()

        if (buscarEnTexto(nuevaPalabra, " ") == False):
            if (largoLista(Ventana.listaPalabras) == 0):
                Ventana.listaPalabras += [nuevaPalabra]
                Palabras.entryPg2.delete(0, END)
                return Palabras.contenidoListBox1(self)
            else:
                if (buscarEnLista(Ventana.listaPalabras, nuevaPalabra) == False):
                    Ventana.listaPalabras += [nuevaPalabra]
                    Palabras.entryPg2.delete(0, END)
                    Palabras.listaPg2.delete(0, END)
                    return Palabras.contenidoListBox1(self)
                else:
                    Palabras.entryPg2.delete(0, END)
                    messagebox.showerror(" ERROR DE REPETICION",
                                         "La Palabra que intenta añadir ya se encuentra en la lista")
        else:
            Palabras.entryPg2.delete(0, END)
            messagebox.showerror("ERROR DE TIPO",
                                 "Introduzca una palabra no una frase")

    """
    Nombre: eliminarPalabra
    Entradas: self
    Salidas:El listbox sin la palabra
    Restricciones:
    """

    def eliminarPalabra(self):
        palabra = Palabras.listaPg2.get(ANCHOR)
        despuesDeLaPalabra = False
        contenido = Ventana.listaPalabras
        Ventana.listaPalabras = []

        for elemento in contenido:
            if (buscarEnTexto(elemento, palabra) == False):
                Ventana.listaPalabras += [elemento]
            else:
                continue

        Palabras.listaPg2.delete(0, END)
        return Palabras.contenidoListBox1(self)

    """
    Nombre: modificaPalabra
    Entradas: self
    Salidas: La palabra cambiada dentro del listbox
    Restricciones: debe ser palabra y no estar en listbox
    """

    def modificarPalabra(self):
        nuevaPalabra = Palabras.entryPg2.get()
        nuevaPalabra = nuevaPalabra.upper()
        palabra = Palabras.listaPg2.get(ANCHOR)

        if (buscarEnTexto(nuevaPalabra, " ") == True):
            Palabras.entryPg2.delete(0, END)
            messagebox.showerror("ERROR DE TIPO",
                                 "Introduzca una Palabra no una Frase")
        else:
            if (buscarEnLista(Ventana.listaPalabras, nuevaPalabra) == False):
                contenido = Ventana.listaPalabras
                Ventana.listaPalabras = []
                for elemento in contenido:
                    if (elemento == palabra):
                        Ventana.listaPalabras += [nuevaPalabra]
                    else:
                        Ventana.listaPalabras += [elemento]

                Palabras.entryPg2.delete(0, END)
                Palabras.listaPg2.delete(0, END)
                return Palabras.contenidoListBox1(self)

            else:
                Palabras.entryPg2.delete(0, END)
                messagebox.showerror("ERROR DE REPETICION",
                                     "La Palabra que desea añadir ya se encuentra en el archivo")


"""
Nombre: Constructor de Frases
Entradas: self
Salidas: Frame de gestion de frases
Restricciones:
"""


class Frases(Ventana):

    def  __init__(self):
        self.image = imglabel = Label(self.pg3, image=self.img1).place(x=0, y=0)
        Frases.crearWidgets(self)
        Ventana.mostrarPagina(self, self.pg3)

    """
    Nombre: crearWidgets
    Entradas: self
    Salidas: Widgets necesarios en la ventana
    Restricciones:
    """

    def crearWidgets(self):
        Frases.marcoPg3 = Frame(self.pg3)
        Frases.marcoPg3.config(width=445, height=235, bg="black")
        Frases.marcoPg3.place(x=25, y=25)

        Frases.fondoPg3 = Frame(Frases.marcoPg3)
        Frases.fondoPg3.config(width=443, height=233)
        Frases.fondoPg3.place(x=1, y=1)

        Frases.tituloPg3 = Label(self.pg3, text="Gestion de Frases", bg="blue", fg="white")
        Frases.tituloPg3.place(x=35, y=15)

        Frases.FrasePg3 = Label(Frases.fondoPg3, text="Frase: ", fg="black")
        Frases.FrasePg3.place(x=215, y=15)

        Frases.Frase = StringVar()
        Frases.entryPg3 = Entry(Frases.fondoPg3, textvariable=Frases.Frase,
                                font=("MS Sans Serif", 12, "bold"), bg="white", fg="black")
        Frases.entryPg3.place(x=215, y=40)

        Frases.listaPg3 = Listbox(Frases.fondoPg3, width=30, selectbackground="blue")
        Frases.listaPg3.place(x=10, y=15)

        Frases.añadirPg3 = Button(Frases.fondoPg3, text=" Agregar ", bg="blue", fg="white",
                                  relief="groove", command=lambda: Frases.agregarFrase(self))
        Frases.añadirPg3.place(x=215, y=75)

        Frases.eliminarPg3 = Button(Frases.fondoPg3, text=" Eliminar ", bg="blue", fg="white",
                                    relief="groove", command=lambda: Frases.eliminarFrase(self))
        Frases.eliminarPg3.place(x=282.5, y=75)

        Frases.modificarPg3 = Button(Frases.fondoPg3, text=" Modificar ", bg="blue", fg="white",
                                     relief="groove", command=lambda: Frases.modificarFrase(self))
        Frases.modificarPg3.place(x=350, y=75)

        Frases.contenidoListBox1(self)

    """
    Nombre: contenidoListBox1
    Entradas: self
    Salidas: contenido necesario para la listbox
    Restricciones:
    """

    def contenidoListBox1(self):
        for indice in range(largoLista(Ventana.listaFrases)):
            Frases.listaPg3.insert(indice, Ventana.listaFrases[indice])

    """
    Nombre: agregarFrase
    Entradas: self
    Salidas: La frase dentro del listbox
    Restricciones: debe ser frase y no estar en listbox
    """

    def agregarFrase(self):
        nuevaFrase = Frases.Frase.get()
        nuevaFrase = nuevaFrase.upper()

        if (buscarEnTexto(nuevaFrase, " ") == True):
            if (largoLista(Ventana.listaFrases) == 0):
                Ventana.listaFrases += [nuevaFrase]
                Frases.entryPg3.delete(0, END)
                return Frases.contenidoListBox1(self)
            else:
                if (buscarEnLista(Ventana.listaFrases, nuevaFrase) == False):
                    Ventana.listaFrases += [nuevaFrase]
                    Frases.entryPg3.delete(0, END)
                    Frases.listaPg3.delete(0, END)
                    return Frases.contenidoListBox1(self)
                else:
                    Frases.entryPg3.delete(0, END)
                    messagebox.showerror(" ERROR DE REPETICION",
                                         "La Frase que intenta añadir ya se encuentra en la lista")
        else:
            Frases.entryPg3.delete(0, END)
            messagebox.showerror("ERROR DE TIPO",
                                 "Introduzca una Frase no una Palabra")

    """
    Nombre: eliminarFrase
    Entradas: self
    Salidas: El listbox sin la frase
    Restricciones:
    """

    def eliminarFrase(self):
        Frase = Frases.listaPg3.get(ANCHOR)
        despuesDeLaFrase = False
        contenido = Ventana.listaFrases
        Ventana.listaFrases = []

        for elemento in contenido:
            if (buscarEnTexto(elemento, Frase) == False):
                Ventana.listaFrases += [elemento]
            else:
                continue

        Frases.listaPg3.delete(0, END)
        return Frases.contenidoListBox1(self)

    """
    Nombre: modificarFrase
    Entradas: self
    Salidas: La frase cambiada dentro del listbox
    Restricciones: debe ser frase y no estar en listbox
    """

    def modificarFrase(self):
        nuevaFrase = Frases.entryPg3.get()
        nuevaFrase = nuevaFrase.upper()
        Frase = Frases.listaPg3.get(ANCHOR)

        if (buscarEnTexto(nuevaFrase, " ") == False):
            Frases.entryPg3.delete(0, END)
            messagebox.showerror("ERROR DE TIPO",
                                 "Introduzca una Frase no una Palabra")
        else:
            if (buscarEnLista(Ventana.listaFrases, nuevaFrase) == False):
                contenido = Ventana.listaFrases
                Ventana.listaFrases = []
                for elemento in contenido:
                    if (elemento == Frase):
                        Ventana.listaFrases += [nuevaFrase]
                    else:
                        Ventana.listaFrases += [elemento]

                Frases.entryPg3.delete(0, END)
                Frases.listaPg3.delete(0, END)
                return Frases.contenidoListBox1(self)

            else:
                Frases.entryPg3.delete(0, END)
                messagebox.showerror("ERROR DE REPETICION",
                                     "La Frase que desea añadir ya se encuentra en el archivo")


class Historia(Ventana):

    def  __init__(self):
        self.image = imglabel = Label(self.pg4, image=self.img1).place(x=0, y=0)
        Historia.crearWidgets(self)
        Ventana.mostrarPagina(self, self.pg4)

    """
    Nombre: crearWidgets
    Entradas: self
    Salidas: Widgets necesarios en la ventana
    Restricciones:
    """

    def crearWidgets(self):
        Historia.fondoPg4 = Frame(self.pg4)
        Historia.fondoPg4.config(width=445, height=235, bg="black")
        Historia.fondoPg4.place(x=25, y=25)

        Historia.listaPg4 = Text(Historia.fondoPg4, width=54, height=14,
                                 bd=1, relief="solid", bg="#f0f0f0", selectbackground="blue")
        Historia.listaPg4.place(x=25, y=25)
        archivo = open("Historia.txt", "r")
        contenido = archivo.read()
        quote = contenido
        Historia.listaPg4.insert(tk.INSERT, quote)
        Historia.listaPg4.config(state="disable")

        barra = Scrollbar(Historia.fondoPg4, command=Historia.listaPg4.yview)
        Historia.listaPg4.config(yscrollcommand=barra.set)
        Historia.listaPg4.pack(side=LEFT)
        barra.pack(side=RIGHT, fill=Y)

        Historia.tituloPg4 = Label(self.pg4, text="Historia", bg="blue", fg="white")
        Historia.tituloPg4.place(x=35, y=15)


class Ayuda(Ventana):

    def __init__(self):
        self.image = imglabel = Label(self.pg5, image=self.img1).place(x=0, y=0)
        Ayuda.crearWidgets(self)
        Ventana.mostrarPagina(self, self.pg5)

    """
    Nombre: crearWidgets
    Entradas: self
    Salidas: Widgets necesarios en la ventana
    Restricciones:
    """

    def crearWidgets(self):
        Ayuda.fondoPg5 = Frame(self.pg5)
        Ayuda.fondoPg5.config(width=445, height=235)
        Ayuda.fondoPg5.place(x=45, y=25)

        Ayuda.listaPg5 = Text(Ayuda.fondoPg5, width=50, height=14,
                              bd=1, relief="solid", bg="#f0f0f0", selectbackground="blue")
        Ayuda.listaPg5.place(x=25, y=25)
        archivo = open("Ayuda.txt", "r")
        contenido = archivo.read()
        quote = contenido
        Ayuda.listaPg5.insert(tk.INSERT, quote)
        Ayuda.listaPg5.config(state="disable")

        barra = Scrollbar(Ayuda.fondoPg5, command=Ayuda.listaPg5.yview)
        Ayuda.listaPg5.config(yscrollcommand=barra.set)
        Ayuda.listaPg5.pack(side=LEFT)
        barra.pack(side=RIGHT, fill=Y)

        Ayuda.tituloPg5 = Label(self.pg5, text="Ayuda", bg="blue", fg="white")
        Ayuda.tituloPg5.place(x=55, y=15)

"""
Nombre: Ahorcado
Entrada: Inicializador
Salida: crea diferentes elementos dentro de la pagina
Restricciones: Debe llamarse desde el menu
"""
class Ahorcado:


    """
Nombre: __init__(self)
Entrada: self
Salida: crea diferentes elementos dentro de la pagina
Restricciones: Debe llamarse desde el ahorcado
    """

    def __init__(self):
        self.image = imglabel = Label(self.pg6, image=self.img).place(x=0, y=0)
        Ahorcado.crearWidgets(self)
        Ventana.mostrarPagina(self,self.pg6)

        """
    Nombre: crearWidgest
    Entrada: self
    Salida: crea diferentes elementos dentro de la pagina
    Restricciones: Debe llamarse desde el ahorcado
        """

    def crearWidgets(self):
        Ahorcado.marcoPg6 = Frame(self.pg6)
        Ahorcado.marcoPg6.config(width=445, height=125, bg="black")
        Ahorcado.marcoPg6.place(x=25, y=80)

        Ahorcado.fondoPg6 = Frame(Ahorcado.marcoPg6)
        Ahorcado.fondoPg6.config(width=443, height=123)
        Ahorcado.fondoPg6.place(x=1, y=1)

        Ahorcado.tituloPg6 = Label(self.pg6, text="Nueva Partida", bg="blue", fg="white")
        Ahorcado.tituloPg6.place(x=35, y=70)

        Ahorcado.modoPg6 = Label(Ahorcado.fondoPg6, text="Elige un modo de juego: ")
        Ahorcado.modoPg6.place(x=15, y=15)

        seleccionar = IntVar()
        seleccionarIdioma = IntVar()

        Ahorcado.opcion1 = Radiobutton(Ahorcado.fondoPg6, text="Principiante",
                              value=1, variable=seleccionar)
        Ahorcado.opcion1.place(x=20, y=35)
        Ahorcado.opcion2 = Radiobutton(Ahorcado.fondoPg6, text="Avanzado",
                              value=2, variable=seleccionar)
        Ahorcado.opcion2.place(x=20, y=55)

        opciones = ttk.Combobox(Ahorcado.fondoPg6)
        opciones.place(x=20, y=80)
        opciones["values"] = ("Español", "Ingles")
        opciones.current(0)
        opciones['state'] = 'readonly'

        Ahorcado.nombrePg6 = Label(Ahorcado.fondoPg6, text="Introduzca su usuario: ")
        Ahorcado.nombrePg6.place(x=200, y=15)

        jugador = StringVar()
        Ahorcado .entryPg6 = Entry(Ahorcado.fondoPg6, textvariable=jugador,
                         font=("MS Sans Serif", 12, "bold"), bg="white", fg="black")
        Ahorcado.entryPg6.place(x=200, y=35)


        Ahorcado.botonPg6 = Button(self.pg6, text="Jugar >>>", width=13, relief="groove",
                                       bg="blue", fg="white",
                                       command=lambda: Juego.__init__(self, seleccionar.get(), jugador.get(),opciones))
        Ahorcado.botonPg6.place(x=355, y=150)


"""
Nombre: Juego(Ventana)
Entrada: self
Salida: crea diferentes elementos dentro de la pagina
Restricciones: Debe llamarse desde el ahorcado
"""

class Juego(Ventana):
    """
    Nombre:  __init__
    Entrada: self, modoJuego, nombreJugador,opciones
    Salida: crea diferentes elementos dentro de la pagina
    Restricciones: Debe llamarse desde el ahorcado
    """
    def __init__(self, modoJuego, nombreJugador,opciones):
        opcion = opciones.get()
        if (opcion == "Español"):
            global correr
            correr = True
            self.image = imglabel = Label(self.pg7, image=self.img1).place(x=0, y=0)
            Juego.crearWidgets(self, modoJuego, nombreJugador)
            Ventana.mostrarPagina(self, self.pg7)
            Juego.iniciar(self)
            self.modo = modoJuego
            self.nombre = nombreJugador
        elif(opcion == "Ingles"):
            return JuegoIngles.__init__(self, modoJuego,nombreJugador)


        """
    Nombre: crearWidgest
    Entrada: self
    Salida: crea diferentes elementos dentro de la pagina
    Restricciones: Debe llamarse desde el ahorcado
        """


    def crearWidgets(self, modo, nombre):
        if (modo == 1):
            modo = "Principiante"
            palabra = palabraPrinci(Ventana.listaPalabras)
            palabraJuego = palabra
            print(palabraJuego)

        elif (modo == 2):
            modo = "Avanzado"
            palabra = palabraPrinci(Ventana.listaFrases)
            palabraJuego = palabra
            print(palabra)
        Juego.marcoPg7 = Frame(self.pg7)
        Juego.marcoPg7.config(width=500, height=300, bg="black")
        Juego.marcoPg7.place(x=0, y=0)

        Juego.fondoPg7 = Frame(Juego.marcoPg7)
        Juego.fondoPg7.config(width=498, height=298)
        Juego.fondoPg7.place(x=1, y=1)

        Juego.labelPg7 = Label(Juego.fondoPg7, text="Jugador:", bg="blue", fg="white")
        Juego.labelPg7.place(x=10, y=20)

        Juego.label_2Pg7 = Label(Juego.fondoPg7, text="Intentos:", bg="blue", fg="white")
        Juego.label_2Pg7.place(x=10, y=60)

        Juego.label_3Pg7 = Label(Juego.fondoPg7, text="Letras:", bg="blue", fg="white")
        Juego.label_3Pg7.place(x=10, y=110)

        Juego.label_4Pg7 = Label(Juego.fondoPg7, text="Modo de juego:", bg="blue", fg="white")
        Juego.label_4Pg7.place(x=10, y=160)
        #####################################################################################################
        # textos
        Juego.labelPg7 = Text(Juego.fondoPg7, width=10, height=1.4, font=("Times New Roman", 10), bg="#f0f0f0")
        Juego.labelPg7.place(x=61, y=21)
        Juego.labelPg7.insert(tk.INSERT, nombre)
        Juego.labelPg7.config(state="disable")

        Juego.label_2Pg7 = Text(Juego.fondoPg7, width=5, height=1.4, font=("Times New Roman", 10), bg="#f0f0f0")
        Juego.label_2Pg7.place(x=61, y=61)
        Juego.label_2Pg7.insert(tk.INSERT, "6")
        Juego.label_2Pg7.config(state="disable")

        Juego.label_3Pg7 = Text(Juego.fondoPg7, width=15, height=1.4, font=("Times New Roman", 10), bg="#f0f0f0")
        Juego.label_3Pg7.place(x=50, y=111)
        Juego.label_3Pg7.config(state="disable")

        # Juego.label_3Pg7.config(state="disable")

        Juego.label_4Pg7 = Text(Juego.fondoPg7, width=13, height=1.4, font=("Times New Roman", 10), bg="#f0f0f0")
        Juego.label_4Pg7.place(x=99, y=161)
        Juego.label_4Pg7.insert(tk.INSERT, modo)
        Juego.label_4Pg7.config(state="disable")

        # FrameJuego##############################################################
        Juego.ahorcado = Frame(Juego.fondoPg7, width=220, height=190, bg="white")
        Juego.ahorcado.place(x=250, y=10)

        Juego.imgInicio = Image.PhotoImage(Image.open(r'C:\Users\Gadyr\Downloads\fase0.jpg').resize((220, 190)))
        Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

        Juego.eti = Label(Juego.fondoPg7, text="Ingrese Una Palabra:", bg="#f0f0f0")
        Juego.eti.place(x=305, y=230)
        Juego.pal1 = Entry(Juego.fondoPg7, bg="#f0f0f0", width=15, textvariable=tk.StringVar())
        Juego.pal1.place(x=315, y=250)

        Juego.bot = Button(Juego.fondoPg7, text="Jugar", bg="blue", fg="white",
                           command=lambda: Jugar.__init__(self, Juego.pal1.get(), Juego.ahorcado, Juego.label_2Pg7,
                                                          Juego.label_3Pg7, palabraJuego, modo))
        Juego.bot.place(x=345, y=270)

        Juego.eti2 = Label(Juego.fondoPg7, text=palabraRes, bg="#f0f0f0", font=("Times New Roman", 15))
        Juego.eti2.place(x=305, y=210)

        Juego.tiempo = Label(Juego.fondoPg7, text="Cronometro", bg="blue", fg="white", font=("Times New Roman", 15))
        Juego.tiempo.place(x=45, y=210)

        Juego.tiempoJ = Label(Juego.fondoPg7, text="00:00:00", bg="#f0f0f0", font=("Times New Roman", 15))
        Juego.tiempoJ.place(x=45, y=245)

        """
    Nombre: iniciar
    Entrada: self
    Salida: crea diferentes elementos dentro de la pagina
    Restricciones: Debe llamarse desde el juego
        """


    def iniciar(self):
        def valor():
            if correr:
                global tiempo
                global contador
                # antes de comecar
                Juego.tiempoJ['font'] = "Times New Roman", 15
                d = str(tiempo)
                hora, minuto, segundo = map(int, d.split(":"))
                hora = int(hora)
                minuto = int(minuto)
                segundo = int(contador)

                if (segundo >= 59):
                    segundo = 0
                    contador = 0
                    minuto += 1

                segundo = str(0) + str(segundo)
                minuto = str(0) + str(minuto)
                hora = str(0) + str(hora)

                d = str(hora[-2:]) + ":" + str(minuto[-2:]) + ":" + str(segundo[-2:])
                Juego.tiempoJ['text'] = d
                tiempo = d

                segundo = int(contador)
                minuto = int(minuto)
                hora = int(hora)

                Juego.tiempoJ.after(1000, valor)
                contador += 1

        valor()




"""
Nombre: iniciar
Entrada: self
Salida: crea diferentes elementos dentro de la pagina
Restricciones: Debe llamarse desde el juego
"""
class Jugar:

    def __init__(self,letraEntry,imagenAhorcado,vidas,letras,palabraJuego,modo):

        self.letraEntry = letraEntry
        self.imagen = imagenAhorcado
        self.vidas = vidas
        self.palabra = palabraJuego
        self.letras = letras
        self.modo = modo
        Jugar.juego(self)
        print(self.palabra)



        """
    Nombre: juego
    Entrada: self
    Salida: crea diferentes elementos dentro de la pagina
    Restricciones: Debe llamarse desde el jugar
        """
    def juego(self):
        global palabraJuego, letrasUsadas, vidasJuego, aciertos
        global palabraRes
        global tempo
        letra = self.letraEntry
        letra = letra.upper()
        if(self.modo == "Principiante"):
            if (Jugar.validarEntrada(self,letra)):
                if (Jugar.validarLargo(self,letra)== True):
                    if(Jugar.validarEs(self,letra)):
                        Juego.label_3Pg7.config(state=tk.NORMAL)
                        Juego.label_3Pg7.insert(tk.INSERT, letra)
                        Juego.label_3Pg7.config(state="disable")

                        if (Jugar.validarLetra(self, letra)):
                            aciertos += 1
                            palabraRes += letra
                            Juego.eti2 = Label(Juego.fondoPg7, text=palabraRes, bg="#f0f0f0", font=("Times New Roman", 15))
                            Juego.eti2.place(x=305, y=210)
                        else:
                            vidasJuego = vidasJuego - 1

                        Juego.pal1.delete(0, END)

                        if (vidasJuego == 5):
                            Juego.imgInicio = Image.PhotoImage(
                                Image.open(r'C:\Users\Gadyr\Downloads\fase1.jpg').resize((220, 190)))
                            Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                            Juego.label_2Pg7.config(state=tk.NORMAL)
                            Juego.label_2Pg7.delete("1.0", "end")
                            Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            Juego.label_2Pg7.config(state="disable")
                            # Juego.label_2pg7.config(state="disable")


                        elif (vidasJuego == 4):
                            Juego.imgInicio = Image.PhotoImage(
                                Image.open(r'C:\Users\Gadyr\Downloads\fase2.jpg').resize((220, 190)))
                            Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                            Juego.label_2Pg7.config(state=tk.NORMAL)
                            Juego.label_2Pg7.delete("1.0", "end")
                            Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            Juego.label_2Pg7.config(state="disable")

                        elif (vidasJuego == 3):
                            Juego.imgInicio = Image.PhotoImage(
                                Image.open(r'C:\Users\Gadyr\Downloads\fase3.jpg').resize((220, 190)))
                            Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                            Juego.label_2Pg7.config(state=tk.NORMAL)
                            Juego.label_2Pg7.delete("1.0", "end")
                            Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            Juego.label_2Pg7.config(state="disable")

                        elif (vidasJuego == 2):
                            Juego.imgInicio = Image.PhotoImage(
                                Image.open(r'C:\Users\Gadyr\Downloads\fase4.jpg').resize((220, 190)))
                            Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                            Juego.label_2Pg7.config(state=tk.NORMAL)
                            Juego.label_2Pg7.delete("1.0", "end")
                            Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            Juego.label_2Pg7.config(state="disable")


                        elif (vidasJuego == 1):
                            Juego.imgInicio = Image.PhotoImage(
                                Image.open(r'C:\Users\Gadyr\Downloads\fase5.jpg').resize((220, 190)))
                            Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                            Juego.label_2Pg7.config(state=tk.NORMAL)
                            Juego.label_2Pg7.delete("1.0", "end")
                            Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            Juego.label_2Pg7.config(state="disable")

                        elif (vidasJuego == 0):
                            Juego.imgInicio = Image.PhotoImage(
                                Image.open(r'C:\Users\Gadyr\Downloads\fase6.jpg').resize((220, 190)))
                            Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                            Juego.label_2Pg7.config(state=tk.NORMAL)
                            Juego.label_2Pg7.delete("1.0", "end")
                            Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            Juego.label_2Pg7.config(state="disable")

                        if (vidasJuego == 0):
                            global contador
                            global correr
                            global tiempo
                            contador = 0
                            correr = False

                            Ventana.juegos += [[self.palabra, self.modo, "perdio"]]
                            vidasJuego = 6
                            aciertos = 0
                            palabraRes = ""
                            messagebox.showinfo("Perdió", "Perdió la partida")
                            pregunta = messagebox.askquestion("Pregunta", "¿Desea jugar de nuevo?")
                            if (pregunta == "yes"):
                                tiempo = '00:00:00'
                                Juego.tiempoJ['text'] = tiempo
                                return Ahorcado.__init__(self)
                        if (aciertos >= largoTexto(self.palabra)):
                            correr = False
                            contador = 0
                            Ventana.juegos += [[self.palabra, self.modo, "gano"]]
                            # palabraJuego = ""
                            vidasJuego = 6
                            aciertos = 0
                            palabraRes = ""
                            messagebox.showinfo("Ganó", "Ganó la partida")
                            pregunta = messagebox.askquestion("Pregunta", "¿Desea jugar de nuevo?")
                            if (pregunta == "yes"):
                                tiempo = '00:00:00'
                                Juego.tiempoJ['text'] = tiempo
                                return Ahorcado.__init__(self)
                    else:
                        Juego.pal1.delete(0, END)
                        messagebox.showinfo("No se admiten espacios", "Ingrese solo letras")

                else:
                    Juego.pal1.delete(0, END)
                    messagebox.showinfo("Más de una letra", "Ingrese solo 1 letra")

            else:
                Juego.pal1.delete(0, END)
                messagebox.showinfo("Letra Incorrecta", "Ingrese solo letras")

        else:
            if (Jugar.validarEntrada(self, letra)):
                if (Jugar.validarLargo(self, letra) == True):
                    Juego.label_3Pg7.config(state=tk.NORMAL)
                    Juego.label_3Pg7.insert(tk.INSERT, letra)
                    Juego.label_3Pg7.config(state="disable")

                    if (Jugar.validarLetra(self, letra)):
                        aciertos += 1
                        palabraRes += letra
                        Juego.eti2 = Label(Juego.fondoPg7, text=palabraRes, bg="#f0f0f0",
                                           font=("Times New Roman", 15))
                        Juego.eti2.place(x=305, y=210)
                    else:
                        vidasJuego = vidasJuego - 1

                    Juego.pal1.delete(0, END)

                    if (vidasJuego == 5):
                        Juego.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase1.jpg').resize((220, 190)))
                        Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                        Juego.label_2Pg7.config(state=tk.NORMAL)
                        Juego.label_2Pg7.delete("1.0", "end")
                        Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        Juego.label_2Pg7.config(state="disable")
                        # Juego.label_2pg7.config(state="disable")


                    elif (vidasJuego == 4):
                        Juego.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase2.jpg').resize((220, 190)))
                        Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                        Juego.label_2Pg7.config(state=tk.NORMAL)
                        Juego.label_2Pg7.delete("1.0", "end")
                        Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        Juego.label_2Pg7.config(state="disable")

                    elif (vidasJuego == 3):
                        Juego.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase3.jpg').resize((220, 190)))
                        Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                        Juego.label_2Pg7.config(state=tk.NORMAL)
                        Juego.label_2Pg7.delete("1.0", "end")
                        Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        Juego.label_2Pg7.config(state="disable")

                    elif (vidasJuego == 2):
                        Juego.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase4.jpg').resize((220, 190)))
                        Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                        Juego.label_2Pg7.config(state=tk.NORMAL)
                        Juego.label_2Pg7.delete("1.0", "end")
                        Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        Juego.label_2Pg7.config(state="disable")


                    elif (vidasJuego == 1):
                        Juego.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase5.jpg').resize((220, 190)))
                        Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                        Juego.label_2Pg7.config(state=tk.NORMAL)
                        Juego.label_2Pg7.delete("1.0", "end")
                        Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        Juego.label_2Pg7.config(state="disable")

                    elif (vidasJuego == 0):
                        Juego.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase6.jpg').resize((220, 190)))
                        Juego.image = imgLabel = Label(Juego.ahorcado, image=Juego.imgInicio).place(x=0, y=0)

                        Juego.label_2Pg7.config(state=tk.NORMAL)
                        Juego.label_2Pg7.delete("1.0", "end")
                        Juego.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        Juego.label_2Pg7.config(state="disable")

                    if (vidasJuego == 0):
                        contador = 0
                        correr = False

                        Ventana.juegos += [[self.palabra, self.modo, "perdio"]]
                        vidasJuego = 6
                        aciertos = 0
                        palabraRes = ""
                        messagebox.showinfo("Perdio", "Perdio la partida")
                        pregunta = messagebox.askquestion("Pregunta", "¿Desea jugar de nuevo?")
                        if (pregunta == "yes"):
                            tiempo = '00:00:00'
                            Juego.tiempoJ['text'] = tiempo
                            return Ahorcado.__init__(self)
                    if (aciertos >= largoTexto(self.palabra)):
                        correr = False
                        contador = 0
                        Ventana.juegos += [[self.palabra, self.modo, "gano"]]
                        # palabraJuego = ""
                        vidasJuego = 6
                        aciertos = 0
                        palabraRes = ""
                        messagebox.showinfo("Gano", "Gano la partida")
                        pregunta = messagebox.askquestion("Pregunta", "¿Desea jugar de nuevo?")
                        if (pregunta == "yes"):
                            tiempo = '00:00:00'
                            Juego.tiempoJ['text'] = tiempo
                            return Ahorcado.__init__(self)
                else:
                    Juego.pal1.delete(0, END)
                    messagebox.showinfo("Más de una letra", "Ingrese solo 1 letra")

            else:
                Juego.pal1.delete(0, END)
                messagebox.showinfo("Letra Incorrecta", "Ingrese solo letras")



        """
    Nombre: validarLetra
    Entrada: self,letra
    Salida: True en caso de serlo, False si no
    Restricciones: Debe llamarse desde el jugar
        """

    def validarLetra(self, letra):
        for c in self.palabra:
            if (c == letra):

                return True

        return False


        """
    Nombre: validarEntrada
    Entrada: self,letra
    Salida: True en caso de serlo, False si no
    Restricciones: Debe llamarse desde el jugar
        """

    def validarEntrada(self,texto):
        for n in texto:
            if (n == "1"):
                return False
            elif (n == "2"):
                return False
            elif (n == "3"):
                return False
            elif (n == "4"):
                return False
            elif (n == "5"):
                return False
            elif (n == "6"):
                return False
            elif (n == "7"):
                return False
            elif (n == "8"):
                return False
            elif (n == "9"):
                return False
            elif (n == "10"):
                return False

            else:
                return True

        """
    Nombre: validarEs
    Entrada: self,letra
    Salida: True en caso de serlo, False si no
    Restricciones: Debe llamarse desde el jugar
        """

    def validarEs(self,texto):
        if(texto != " "):

            return True
        else:
            return False


        """
    Nombre: validarLargo
    Entrada: self,letra
    Salida: True en caso de serlo, False si no
    Restricciones: Debe llamarse desde el jugar
        """

    def validarLargo(self,texto):
        if(len(texto)== 1):
            return True
        else:
            return False


"""
Nombre: Estadisticas
Entrada: inicializador
Salida: Muestra los widgest
Restricciones: Debe llamarse desde el menu
"""
class Estadisticas(Ventana):

    def __init__(self):
        Estadisticas.crearWidgets(self)
        Ventana.mostrarPagina(self, self.pg8)

    def crearWidgets(self):

        Estadisticas.juegos = Ventana.juegos

        Estadisticas.fondo1 = Frame(self.pg8)
        Estadisticas.fondo1.config(width=15, height=35)
        Estadisticas.fondo1.place(x=10, y=30)

        Estadisticas.titulo1 = Label(self.pg8, text=" Derrotas - Palabras ",
                                     width=15, bg="blue", fg="white")
        Estadisticas.titulo1.place(x=10, y=10)

        Estadisticas.palabras = Listbox(Estadisticas.fondo1, width=15, height=15,
                                        selectbackground="blue", bg="#f0f0f0", relief="solid")
        barra1 = Scrollbar(Estadisticas.fondo1, command=Estadisticas.palabras.yview)
        Estadisticas.palabras.config(yscrollcommand=barra1.set)
        Estadisticas.palabras.pack(side=LEFT)
        barra1.pack(side=RIGHT, fill=Y)

        Estadisticas.fondo2 = Frame(self.pg8)
        Estadisticas.fondo2.config(width=20, height=35)
        Estadisticas.fondo2.place(x=140, y=30)

        Estadisticas.titulo2 = Label(self.pg8, text=" Derrotas - Frases ",
                                     width=20, bg="blue", fg="white")
        Estadisticas.titulo2.place(x=140, y=10)

        Estadisticas.frases = Listbox(Estadisticas.fondo2, width=20, height=15,
                                      selectbackground="blue", bg="#f0f0f0", relief="solid")
        barra2 = Scrollbar(Estadisticas.fondo2, command=Estadisticas.frases.yview)
        Estadisticas.frases.config(yscrollcommand=barra2.set)
        Estadisticas.frases.pack(side=LEFT)
        barra2.pack(side=RIGHT, fill=Y)

        Estadisticas.contenidoListBox2(self)
        Estadisticas.azul = Frame(self.pg8, width=190, height=300, bg="blue").pack(side=RIGHT)

        Estadisticas.titulo3 = Label(self.pg8, text="Total de juegos: ", bg="blue", fg="white")
        Estadisticas.titulo3.place(x=325, y=10)

        Estadisticas.totalJuegos = 0
        for juego in Ventana.juegos:
            Estadisticas.totalJuegos += 1
        Estadisticas.juegos = Text(self.pg8, width=5, height=1, selectbackground="blue")
        quote = str(Estadisticas.totalJuegos)
        Estadisticas.juegos.insert(tk.INSERT, quote)
        Estadisticas.juegos.config(state="disabled")
        Estadisticas.juegos.place(x=435, y=10)

        Estadisticas.marco1 = Frame(self.pg8, width=160, height=100, bg="black")
        Estadisticas.marco1.place(x=325, y=55)

        Estadisticas.fondo3 = Frame(Estadisticas.marco1, width=158, height=98, bg="blue")
        Estadisticas.fondo3.place(x=1, y=1)

        Estadisticas.titulo4 = Label(self.pg8, text="Juegos por Modo", fg="black")
        Estadisticas.titulo4.place(x=335, y=45)

        Estadisticas.titulo6 = Label(Estadisticas.fondo3, text="Principiante: ", bg="blue", fg="white")
        Estadisticas.titulo6.place(x=5, y=15)

        Estadisticas.modoFacil = 0
        for juego in Ventana.juegos:
            if (juego[1] == "Principiante"):
                Estadisticas.modoFacil += 1
            else:
                continue
        Estadisticas.principiante = Text(Estadisticas.fondo3, width=5, height=1, selectbackground="blue")
        quote = str(Estadisticas.modoFacil)
        Estadisticas.principiante.insert(tk.INSERT, quote)
        Estadisticas.principiante.config(state="disabled")
        Estadisticas.principiante.place(x=100, y=22)

        Estadisticas.titulo7 = Label(Estadisticas.fondo3, text="Avanzado: ", bg="blue", fg="white")
        Estadisticas.titulo7.place(x=15, y=55)

        Estadisticas.modoDificil = 0
        for juego in Ventana.juegos:
            if (juego[1] == "Avanzado"):
                Estadisticas.modoDificil += 1
            else:
                continue
        Estadisticas.principiante = Text(Estadisticas.fondo3, width=5, height=1, selectbackground="blue")
        quote = str(Estadisticas.modoDificil)
        Estadisticas.principiante.insert(tk.INSERT, quote)
        Estadisticas.principiante.config(state="disabled")
        Estadisticas.principiante.place(x=100, y=62)

        Estadisticas.marco2 = Frame(self.pg8, width=160, height=100, bg="black")
        Estadisticas.marco2.place(x=325, y=175)

        Estadisticas.fondo4 = Frame(Estadisticas.marco2, width=158, height=98, bg="blue")
        Estadisticas.fondo4.place(x=1, y=1)

        Estadisticas.titulo5 = Label(self.pg8, text="Resultado Juegos", fg="black")
        Estadisticas.titulo5.place(x=375, y=165)

        Estadisticas.titulo5 = Label(self.pg8, text="Resultado Juegos", fg="black")
        Estadisticas.titulo5.place(x=375, y=165)

        Estadisticas.titulo8 = Label(Estadisticas.fondo4, text="Victorias: ", bg="blue", fg="white")
        Estadisticas.titulo8.place(x=15, y=15)

        Estadisticas.juegosGanados = 0
        for juego in Ventana.juegos:
            if (juego[2] == "gano"):
                Estadisticas.juegosGanados += 1
            else:
                continue
        Estadisticas.victorias = Text(Estadisticas.fondo4, width=5, height=1, selectbackground="blue")
        quote = str(Estadisticas.juegosGanados)
        Estadisticas.victorias.insert(tk.INSERT, quote)
        Estadisticas.victorias.config(state="disabled")
        Estadisticas.victorias.place(x=100, y=22)

        Estadisticas.titulo8 = Label(Estadisticas.fondo4, text="Derrotas: ", bg="blue", fg="white")
        Estadisticas.titulo8.place(x=15, y=55)

        Estadisticas.juegosPerdidos = 0
        for juego in Ventana.juegos:
            if (juego[2] == "perdio"):
                Estadisticas.juegosPerdidos += 1
            else:
                continue
        Estadisticas.derrotas = Text(Estadisticas.fondo4, width=5, height=1, selectbackground="blue")
        quote = str(Estadisticas.juegosPerdidos)
        Estadisticas.derrotas.insert(tk.INSERT, quote)
        Estadisticas.derrotas.config(state="disabled")
        Estadisticas.derrotas.place(x=100, y=62)

    """
    Nombre: contenidoListbox2
    Entrada:self
    Salida: Muestra los widgest
    Restricciones: Debe llamarse desde Estadisticas
    """

    def contenidoListBox2(self):
        indiceP = 0
        indiceF = 0
        while (largoLista(Estadisticas.juegos) > 0):
            PoF = Estadisticas.juegos[0][0]
            repeticiones = Estadisticas.repeticiones(self, PoF)
            if (repeticiones > 0):
                linea = PoF + ": " + str(repeticiones)
                if (buscarEnTexto(PoF, " ") == False):
                    Estadisticas.palabras.insert(indiceP, linea)
                    indiceP += 1
                if (buscarEnTexto(PoF, " ") == True):
                    Estadisticas.frases.insert(indiceF, linea)
                    indiceF += 1

    """
    Nombre:repeticiones
    Entrada:self
    Salida: Muestra los widgest
    Restricciones: Debe llamarse desde Estadisticas
    """


    def repeticiones(self, PoF):
        contenido = Estadisticas.juegos
        Estadisticas.juegos = []
        repeticiones = 0
        for partida in contenido:
            if (partida[0] == PoF):
                if (partida[2] == "perdio"):
                    repeticiones += 1
            else:
                Estadisticas.juegos += [partida]

        return repeticiones

#############################################################################
#####################MANEJO DE IDIOMAS#########################################################
#############################################################################
"""
Nombre: JuegoIngles
Entrada:Inicializador
Salida: Muestra los widgest
Restricciones: Debe llamarse desde el ahoracado
"""


class JuegoIngles:
    def __init__(self, modoJuego, nombreJugador):
        global correr
        correr = True
        self.image = imglabel = Label(self.pg7, image=self.img1).place(x=0, y=0)
        JuegoIngles.crearWidgets(self, modoJuego, nombreJugador)
        Ventana.mostrarPagina(self, self.pg7)
        JuegoIngles.iniciar(self)
        self.modo = modoJuego
        self.nombre = nombreJugador

        """
    Nombre: crearWidgest
    Entrada: self
    Salida: crea diferentes elementos dentro de la pagina
    Restricciones: Debe llamarse desde el ahorcado
        """

    def crearWidgets(self, modo, nombre):
        if (modo == 1):
            modo = "beginner"
            palabra = palabraPrinci(Ventana.listaPalabrasIngles)
            palabraJuego = palabra
            print(palabraJuego)

        elif (modo == 2):
            modo = "advanced"
            palabra = palabraPrinci(Ventana.listaFrasesIngles)
            palabraJuego = palabra
            print(palabra)
        JuegoIngles.marcoPg7 = Frame(self.pg7)
        JuegoIngles.marcoPg7.config(width=500, height=300, bg="black")
        JuegoIngles.marcoPg7.place(x=0, y=0)

        JuegoIngles.fondoPg7 = Frame(JuegoIngles.marcoPg7)
        JuegoIngles.fondoPg7.config(width=498, height=298)
        JuegoIngles.fondoPg7.place(x=1, y=1)

        JuegoIngles.labelPg7 = Label(JuegoIngles.fondoPg7, text="Player:", bg="blue", fg="white")
        JuegoIngles.labelPg7.place(x=10, y=20)

        JuegoIngles.label_2Pg7 = Label(JuegoIngles.fondoPg7, text="Remaining lives:", bg="blue", fg="white")
        JuegoIngles.label_2Pg7.place(x=10, y=60)

        JuegoIngles.label_3Pg7 = Label(JuegoIngles.fondoPg7, text="Words:", bg="blue", fg="white")
        JuegoIngles.label_3Pg7.place(x=10, y=110)

        JuegoIngles.label_4Pg7 = Label(JuegoIngles.fondoPg7, text="game mode:", bg="blue", fg="white")
        JuegoIngles.label_4Pg7.place(x=10, y=160)
        #####################################################################################################
        # textos
        JuegoIngles.labelPg7 = Text(JuegoIngles.fondoPg7, width=10, height=1.4, font=("Times New Roman", 10),
                                    bg="#f0f0f0")
        JuegoIngles.labelPg7.place(x=51, y=21)
        JuegoIngles.labelPg7.insert(tk.INSERT, nombre)
        JuegoIngles.labelPg7.config(state="disable")

        JuegoIngles.label_2Pg7 = Text(JuegoIngles.fondoPg7, width=5, height=1.4, font=("Times New Roman", 10),
                                      bg="#f0f0f0")
        JuegoIngles.label_2Pg7.place(x=102, y=61)
        JuegoIngles.label_2Pg7.insert(tk.INSERT, "6")
        JuegoIngles.label_2Pg7.config(state="disable")

        JuegoIngles.label_3Pg7 = Text(JuegoIngles.fondoPg7, width=15, height=1.4, font=("Times New Roman", 10),
                                      bg="#f0f0f0")
        JuegoIngles.label_3Pg7.place(x=52, y=111)
        JuegoIngles.label_3Pg7.config(state="disable")

        # Juego.label_3Pg7.config(state="disable")

        JuegoIngles.label_4Pg7 = Text(JuegoIngles.fondoPg7, width=13, height=1.4, font=("Times New Roman", 10),
                                      bg="#f0f0f0")
        JuegoIngles.label_4Pg7.place(x=83, y=161)
        JuegoIngles.label_4Pg7.insert(tk.INSERT, modo)
        JuegoIngles.label_4Pg7.config(state="disable")

        # FrameJuego##############################################################
        JuegoIngles.ahorcado = Frame(JuegoIngles.fondoPg7, width=220, height=190, bg="white")
        JuegoIngles.ahorcado.place(x=250, y=10)

        JuegoIngles.imgInicio = Image.PhotoImage(
            Image.open(r'C:\Users\Gadyr\Downloads\fase0.jpg').resize((220, 190)))
        JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(x=0, y=0)

        JuegoIngles.eti = Label(JuegoIngles.fondoPg7, text="Enter a word:", bg="#f0f0f0")
        JuegoIngles.eti.place(x=322, y=232)
        JuegoIngles.pal1 = Entry(JuegoIngles.fondoPg7, bg="#f0f0f0", width=15, textvariable=tk.StringVar())
        JuegoIngles.pal1.place(x=315, y=252)

        JuegoIngles.bot = Button(JuegoIngles.fondoPg7, text="Play", bg="blue", fg="white",
                                 command=lambda: JugarIngles.__init__(self, JuegoIngles.pal1.get(),
                                                                      JuegoIngles.ahorcado,
                                                                      JuegoIngles.label_2Pg7, JuegoIngles.label_3Pg7,
                                                                      palabraJuego, modo))
        JuegoIngles.bot.place(x=345, y=272)

        JuegoIngles.eti2 = Label(JuegoIngles.fondoPg7, text=palabraRes, bg="#f0f0f0", font=("Times New Roman", 15))
        JuegoIngles.eti2.place(x=305, y=210)

        JuegoIngles.tiempo = Label(JuegoIngles.fondoPg7, text="Chronometer", bg="blue", fg="white",
                                   font=("Times New Roman", 15))
        JuegoIngles.tiempo.place(x=45, y=210)

        JuegoIngles.tiempoJ = Label(JuegoIngles.fondoPg7, text="00:00:00", bg="#f0f0f0",
                                    font=("Times New Roman", 15))
        JuegoIngles.tiempoJ.place(x=45, y=245)

        """
    Nombre: iniciar
    Entrada: self
    Salida: crea diferentes elementos dentro de la pagina
    Restricciones: Debe llamarse desde el juegoIngles
        """

    def iniciar(self):
        def valor():
            if correr:
                global tiempo
                global contador
                # antes de comecar
                JuegoIngles.tiempoJ['font'] = "Times New Roman", 15
                d = str(tiempo)
                hora, minuto, segundo = map(int, d.split(":"))
                hora = int(hora)
                minuto = int(minuto)
                segundo = int(contador)

                if (segundo >= 59):
                    segundo = 0
                    contador = 0
                    minuto += 1

                segundo = str(0) + str(segundo)
                minuto = str(0) + str(minuto)
                hora = str(0) + str(hora)

                d = str(hora[-2:]) + ":" + str(minuto[-2:]) + ":" + str(segundo[-2:])
                JuegoIngles.tiempoJ['text'] = d
                tiempo = d

                segundo = int(contador)
                minuto = int(minuto)
                hora = int(hora)

                JuegoIngles.tiempoJ.after(1000, valor)
                contador += 1

        valor()

"""
Nombre:Jugar
Entrada: Inicializador
Salida: crea diferentes elementos dentro de la pagina
Restricciones: Debe llamarse desde el juegoIngles
 """

class JugarIngles:

    def __init__(self,letraEntry,imagenAhorcado,vidas,letras,palabraJuego,modo):

        self.letraEntry = letraEntry
        self.imagen = imagenAhorcado
        self.vidas = vidas
        self.palabra = palabraJuego
        self.letras = letras
        self.modo = modo

        JugarIngles.juego(self)
        print(self.palabra)

        """
    Nombre: juego
    Entrada: self
   Salida: funcion de jugar
    Restricciones: Debe llamarse desde JugarIngles
        """

    def juego(self):
        global palabraJuego, letrasUsadas, vidasJuego, aciertos
        global palabraRes
        global tempo
        letra = self.letraEntry
        letra = letra.upper()
        if (self.modo == "beginner"):
            if (JugarIngles.validarEntrada(self, letra)):
                if (JugarIngles.validarLargo(self, letra) == True):
                    if (JugarIngles.validarEs(self, letra)):
                        JuegoIngles.label_3Pg7.config(state=tk.NORMAL)
                        JuegoIngles.label_3Pg7.insert(tk.INSERT,letra)
                        JuegoIngles.label_3Pg7.config(state="disable")
                        if (JugarIngles.validarLetra(self,letra)):
                            aciertos += 1
                            palabraRes += letra
                            JuegoIngles.eti2 = Label(JuegoIngles.fondoPg7, text=palabraRes, bg="#f0f0f0", font=("Times New Roman", 15))
                            JuegoIngles.eti2.place(x=305, y=210)
                        else:
                            vidasJuego = vidasJuego - 1



                        JuegoIngles.pal1.delete(0, END)



                        if(vidasJuego == 5):
                            JuegoIngles.imgInicio = Image.PhotoImage(Image.open(r'C:\Users\Gadyr\Downloads\fase1.jpg').resize((220, 190)))
                            JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(x=0, y=0)


                            JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                            JuegoIngles.label_2Pg7.delete("1.0", "end")
                            JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            JuegoIngles.label_2Pg7.config(state="disable")
                            #Juego.label_2pg7.config(state="disable")


                        elif (vidasJuego == 4):
                            JuegoIngles.imgInicio = Image.PhotoImage(Image.open(r'C:\Users\Gadyr\Downloads\fase2.jpg').resize((220, 190)))
                            Juego.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(x=0, y=0)

                            JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                            JuegoIngles.label_2Pg7.delete("1.0", "end")
                            JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            JuegoIngles.label_2Pg7.config(state="disable")

                        elif (vidasJuego == 3):
                            JuegoIngles.imgInicio = Image.PhotoImage(Image.open(r'C:\Users\Gadyr\Downloads\fase3.jpg').resize((220, 190)))
                            JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(x=0, y=0)

                            JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                            JuegoIngles.label_2Pg7.delete("1.0", "end")
                            JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            JuegoIngles.label_2Pg7.config(state="disable")

                        elif (vidasJuego == 2):
                            JuegoIngles.imgInicio = Image.PhotoImage(Image.open(r'C:\Users\Gadyr\Downloads\fase4.jpg').resize((220, 190)))
                            JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(x=0, y=0)

                            JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                            JuegoIngles.label_2Pg7.delete("1.0", "end")
                            JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            JuegoIngles.label_2Pg7.config(state="disable")


                        elif (vidasJuego == 1):
                            JuegoIngles.imgInicio = Image.PhotoImage(Image.open(r'C:\Users\Gadyr\Downloads\fase5.jpg').resize((220, 190)))
                            JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(x=0, y=0)

                            JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                            JuegoIngles.label_2Pg7.delete("1.0", "end")
                            JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            JuegoIngles.label_2Pg7.config(state="disable")

                        elif (vidasJuego == 0):
                            JuegoIngles.imgInicio = Image.PhotoImage(Image.open(r'C:\Users\Gadyr\Downloads\fase6.jpg').resize((220, 190)))
                            JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(x=0, y=0)

                            JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                            JuegoIngles.label_2Pg7.delete("1.0", "end")
                            JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                            JuegoIngles.label_2Pg7.config(state="disable")

                        if(vidasJuego == 0):
                            global contador
                            global correr
                            global tiempo
                            contador = 0
                            correr = False

                            Ventana.juegos += [[self.palabra,self.modo,"perdio"]]
                            vidasJuego = 6
                            aciertos = 0
                            palabraRes = ""
                            messagebox.showinfo("Game Over", "You lost the game")
                            pregunta = messagebox.askquestion("Ask", "Do you want to play again?")
                            if (pregunta == "yes"):
                                tiempo = '00:00:00'
                                JuegoIngles.tiempoJ['text'] = tiempo
                                return Ahorcado.__init__(self)
                        if(aciertos >= largoTexto(self.palabra)):
                            correr = False
                            contador = 0
                            Ventana.juegos += [[self.palabra, self.modo, "gano"]]
                            #palabraJuego = ""
                            vidasJuego = 6
                            aciertos = 0
                            palabraRes = ""
                            messagebox.showinfo("You Win", "Won the game")
                            pregunta = messagebox.askquestion("Ask", "Do you want to play again?")
                            if (pregunta == "yes"):
                                tiempo = '00:00:00'
                                JuegoIngles.tiempoJ['text'] = tiempo
                                return Ahorcado.__init__(self)
                    else:
                        JuegoIngles.pal1.delete(0, END)
                        messagebox.showinfo("spaces are not allowed", "Enter only letters")

                else:
                    JuegoIngles.pal1.delete(0, END)
                    messagebox.showinfo("More than one letter", "Enter only 1 letter")

            else:
                JuegoIngles.pal1.delete(0, END)
                messagebox.showinfo("wrong letter", "Enter only letters")
        else:
            if (JugarIngles.validarEntrada(self, letra)):
                if (JugarIngles.validarLargo(self, letra) == True):
                    JuegoIngles.label_3Pg7.config(state=tk.NORMAL)
                    JuegoIngles.label_3Pg7.insert(tk.INSERT, letra)
                    JuegoIngles.label_3Pg7.config(state="disable")

                    if (JugarIngles.validarLetra(self, letra)):
                        aciertos += 1
                        palabraRes += letra
                        JuegoIngles.eti2 = Label(JuegoIngles.fondoPg7, text=palabraRes, bg="#f0f0f0",
                                                 font=("Times New Roman", 15))
                        JuegoIngles.eti2.place(x=305, y=210)
                    else:
                        vidasJuego = vidasJuego - 1

                    JuegoIngles.pal1.delete(0, END)

                    if (vidasJuego == 5):
                        JuegoIngles.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase1.jpg').resize((220, 190)))
                        JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(
                            x=0, y=0)

                        JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                        JuegoIngles.label_2Pg7.delete("1.0", "end")
                        JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        JuegoIngles.label_2Pg7.config(state="disable")
                        # Juego.label_2pg7.config(state="disable")


                    elif (vidasJuego == 4):
                        JuegoIngles.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase2.jpg').resize((220, 190)))
                        Juego.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(x=0,
                                                                                                                y=0)

                        JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                        JuegoIngles.label_2Pg7.delete("1.0", "end")
                        JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        JuegoIngles.label_2Pg7.config(state="disable")

                    elif (vidasJuego == 3):
                        JuegoIngles.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase3.jpg').resize((220, 190)))
                        JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(
                            x=0, y=0)

                        JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                        JuegoIngles.label_2Pg7.delete("1.0", "end")
                        JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        JuegoIngles.label_2Pg7.config(state="disable")

                    elif (vidasJuego == 2):
                        JuegoIngles.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase4.jpg').resize((220, 190)))
                        JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(
                            x=0, y=0)

                        JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                        JuegoIngles.label_2Pg7.delete("1.0", "end")
                        JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        JuegoIngles.label_2Pg7.config(state="disable")


                    elif (vidasJuego == 1):
                        JuegoIngles.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase5.jpg').resize((220, 190)))
                        JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(
                            x=0, y=0)

                        JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                        JuegoIngles.label_2Pg7.delete("1.0", "end")
                        JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        JuegoIngles.label_2Pg7.config(state="disable")

                    elif (vidasJuego == 0):
                        JuegoIngles.imgInicio = Image.PhotoImage(
                            Image.open(r'C:\Users\Gadyr\Downloads\fase6.jpg').resize((220, 190)))
                        JuegoIngles.image = imgLabel = Label(JuegoIngles.ahorcado, image=JuegoIngles.imgInicio).place(
                            x=0, y=0)

                        JuegoIngles.label_2Pg7.config(state=tk.NORMAL)
                        JuegoIngles.label_2Pg7.delete("1.0", "end")
                        JuegoIngles.label_2Pg7.insert(tk.INSERT, vidasJuego)
                        JuegoIngles.label_2Pg7.config(state="disable")

                    if (vidasJuego == 0):

                        contador = 0
                        correr = False

                        Ventana.juegos += [[self.palabra, self.modo, "perdio"]]
                        vidasJuego = 6
                        aciertos = 0
                        palabraRes = ""
                        messagebox.showinfo("Game Over", "You lost the game")
                        pregunta = messagebox.askquestion("Ask", "Do you want to play again?")
                        if (pregunta == "yes"):
                            tiempo = '00:00:00'
                            JuegoIngles.tiempoJ['text'] = tiempo
                            return Ahorcado.__init__(self)
                    if (aciertos >= largoTexto(self.palabra)):
                        correr = False
                        contador = 0
                        Ventana.juegos += [[self.palabra, self.modo, "gano"]]
                        # palabraJuego = ""
                        vidasJuego = 6
                        aciertos = 0
                        palabraRes = ""
                        messagebox.showinfo("You Win", "Won the game")
                        pregunta = messagebox.askquestion("Ask", "Do you want to play again?")
                        if (pregunta == "yes"):
                            tiempo = '00:00:00'
                            JuegoIngles.tiempoJ['text'] = tiempo
                            return Ahorcado.__init__(self)

                else:
                    JuegoIngles.pal1.delete(0, END)
                    messagebox.showinfo("More than one letter", "Enter only 1 letter")

            else:
                JuegoIngles.pal1.delete(0, END)
                messagebox.showinfo("wrong letter", "Enter only letters")

        """
    Nombre: validarLetra
    Entrada: self,letra
   Salida: True en caso de serlo, False si no
    Restricciones: Debe llamarse desde JugarIngles
        """


    def validarLetra(self, letra):
        for c in self.palabra:
            if (c == letra):

                return True

        return False


        """
    Nombre: validarEntrada
    Entrada: self,letra
    Salida: True en caso de serlo, False si no
    Restricciones: Debe llamarse desde JugarIngles
        """


    def validarEntrada(self,texto):
        for n in texto:
            if (n == "1"):
                return False
            elif (n == "2"):
                return False
            elif (n == "3"):
                return False
            elif (n == "4"):
                return False
            elif (n == "5"):
                return False
            elif (n == "6"):
                return False
            elif (n == "7"):
                return False
            elif (n == "8"):
                return False
            elif (n == "9"):
                return False
            elif (n == "10"):
                return False

            else:
                return True


        """
    Nombre: validarEs
    Entrada: self,letra
    Salida: True en caso de serlo, False si no
    Restricciones: Debe llamarse desde JugarIngles
        """


    def validarEs(self,texto):
        if(texto != " "):
            print("1")
            return True
        else:
            return False


        """
    Nombre: validarLargo
    Entrada: self,letra
    Salida: True en caso de serlo, False si no
    Restricciones: Debe llamarse desde JugarIngles
        """

    def validarLargo(self,texto):
        if(len(texto)== 1):
            return True
        else:
            return False






ahorcado = Ventana(Tk())
ahorcado.interfaz.mainloop()