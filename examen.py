"""Examen de programacion orientada a objetos, paint en comandos de consola
Alumno: Juan Antonio Roman Castro"""
#pylint: disable=C0103
#pylint: disable=E1101
import pygame
class Configuraciones:
    """objeto para las configuraciones de dibujo"""
    def __init__(self):
        self.grosor = 1
        self.color = (255,255,255)
        self.bgcolor =(0,0,0)
    def cambiar_color(self,asistente):
        """funcion para cambiar el color de linea"""
        self.color = asistente.codigo_colores[int(input("Ingrese el numero del color"))]
    def cambiar_bgcolor(self,asistente):
        """funcion para cambiar el color de fondo"""
        self.bgcolor = asistente.codigo_colores[int(input("Ingrese el numero del color"))]
    def cambiar_grosor(self):
        """funcion para cambiar el grosor de linea"""
        self.grosor = int(input("Ingrese el grosor"))

class Soporte:
    """objeto para dar ayuda al usuario"""
    def __init__(self):
        self.colores = ["Blanco","Negro","Rojo","Azul","Amarillo",
                        "Verde","Rosa","Cafe","Anaranjado","Morado"]
        self.codigo_colores=[(255,255,255),(0,0,0),(255,0,0),(0,0,255),(255,255,0)
                            ,(0,255,0),(240,54,135),(75,54,33),(255,102,0),(87,35,100)]
    def mostrar_colores(self):
        """funcion para mostrar lista de colores y su numero"""
        for i in range(len(self.colores)):
            print(i,"-",self.colores[i])
    def instrucciones(self):
        """funcion para imprimir informacion del programador y sobre los comandos"""
        print("Este programa es un paint, en el cual dibujas usando comandos")
        print("Datos del programador:")
        print("Nombre: Juan Antonio Roman Castro")
        print("Usuario en git: Juankid24")
        print("Lista de comandos:")
        print("'mostrar colores' muestra la lista de colores disponibles")
        print("'color de linea' cambia el color de la linea con el numero que se le asigno al color")
        print("'color de fondo' cambia el color del fondo con el numero que se le asigno al color")
        print("advertencia, tras cambiar el color del fondo se borran los dibujos")
        print(" se recomienda cambiarlo antes de iniciar el dibujo")
        print("'grosor' cambia el grosor de la linea")
        print("'linea' dibuja una linea de una coordenada a otra")
        print("'cuadrado' dibuja un cuadrado con los daros que se te piden")
        print("'rectangulo' dibuja un rectangulo con los daros que se te piden")
        print("'circulo' dibuja un circulo con los daros que se te piden")
        print("'triangulo equilatero' dibuja un triangulo equilatero con los daros que se te piden")
        print("'triangulo isoseles' dibuja un triangulo isoseles con los daros que se te piden")
        print("'triangulo escaleno' dibuja un triangulo escaleno con los daros que se te piden")
        print("'deshacer' deshace el ultimo comando de dibujo realizado")
        print("'exit' cierra el programa")

    def bienvenida(self):
        """funcion para recordarle al usuario al inicio del programa el comando de ayuda"""
        print("si necesitas revisar algun comando ingresa 'help'")

"""inicializacion de los objetos"""
config=Configuraciones()
ayuda=Soporte()        
# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles
width = 800
height = 600
surface = pygame.display.set_mode((width, height))
undovalores=[]
undofuncion=[]
nundo=-1

# Establecer el color de un píxel en la posición (100, 200) a rojo (255, 0, 0)
ayuda.bienvenida()

def linea(grosor,x1,y1,x2,y2,color):
    """funcion para dibujar lineas"""
    diferenciax = abs(x2 - x1)
    diferenciay = abs(y2 - y1)

    error = diferenciax - diferenciay

    if x1 > x2:
        incrementox = -1 
    else:
        incrementox = 1
    if y1 > y2:
        incrementoy = -1 
    else:
        incrementoy = 1

    x=x1
    y=y1
    while x != x2 or y != y2:
        for i in range(grosor):
            for j in range(grosor):
                surface.set_at((x+i, y+j), color)

        error2 = 2 * error
        if error2 > -diferenciay:
            error -= diferenciay
            x += incrementox
        if error2 < diferenciax:
            error += diferenciax
            y += incrementoy

    for i in range(grosor):
        for j in range(grosor):
            surface.set_at((x2+i,y2+j), color)

    pygame.display.flip()

def circulo(grosor,xi,yi,radio,color):
    """funcion para dibujar circulos"""
    radioC=radio-grosor
    for x in range(xi - radio, xi + radio + 1):
        for y in range(yi - radio, yi + radio + 1):
            dx = x - xi
            dy = y - yi
            if dx ** 2 + dy ** 2 <= radio ** 2:
                surface.set_at((x, y), color)
    for x in range(xi - radioC, xi + radioC + 1):
        for y in range(yi - radioC, yi + radioC + 1):
            dx = x - xi
            dy = y - yi
            if dx ** 2 + dy ** 2 <= radioC ** 2:
                surface.set_at((x, y), config.bgcolor)
    pygame.display.flip()

def cuadrado(grosor,x1,y1,lado,color):
    """funcion para dibujar cuadrados"""
    x2=x1+lado
    y2=y1+lado
    linea(grosor,x1,y1,x2,y1,color)
    linea(grosor,x1,y1,x1,y2,color)
    linea(grosor,x2,y2,x2,y1,color)
    linea(grosor,x2,y2,x1,y2,color)

def rectangulo(grosor,x1,y1,base,altura,color):
    """funcion para dibujar rectangulos"""
    x2=x1+base
    y2=y1+altura
    linea(grosor,x1,y1,x2,y1,color)
    linea(grosor,x1,y1,x1,y2,color)
    linea(grosor,x2,y2,x2,y1,color)
    linea(grosor,x2,y2,x1,y2,color)

def equilatero(grosor,x1,y1,lado,color):
    """funcion para dibujar triangulos equilateros"""
    x2=x1+lado
    x3=int(x1+(lado/2))
    y2=int(y1-(lado*1.732/2))
    linea(grosor,x1,y1,x2,y1,color)
    linea(grosor,x1,y1,x3,y2,color)
    linea(grosor,x3,y2,x2,y1,color)

def isoseles(grosor,x1,y1,base,altura,color):
    """funcion para dibujar triangulos isoseles"""
    x2=x1+base
    x3=int(x1+(base/2))
    y2=y1-altura
    linea(grosor,x1,y1,x2,y1,color)
    linea(grosor,x1,y1,x3,y2,color)
    linea(grosor,x3,y2,x2,y1,color)

def escaleno(grosor,x1,y1,base,altura,color):
    """funcion para dibujar triangulos escalenos"""
    x2=x1+base
    y2=y1-altura
    linea(grosor,x1,y1,x2,y1,color)
    linea(grosor,x1,y1,x1,y2,color)
    linea(grosor,x2,y1,x1,y2,color)

# Esperar a que el usuario cierre la ventana
while True:
    """comandos para que funcione el programa"""
    cmd = input("cmd> ")
    if cmd == "exit":
        pygame.quit()

    if cmd == "help":
        ayuda.instrucciones()
    if cmd == "mostrar colores":
        ayuda.mostrar_colores()

    if cmd == "color de linea":
        config.cambiar_color(ayuda)
    if cmd == "color de fondo":
        config.cambiar_bgcolor(ayuda)
        surface.fill(config.bgcolor)
        pygame.display.flip()
        undovalores=[]
        undofuncion=[]
        nundo=-1
    if cmd == "grosor":
        config.cambiar_grosor()

    if cmd == "linea":
        xi=int(input("Coordenada inicial \n X> "))
        yi=int(input(" Y> "))
        xf=int(input("Coordenada final \n X> "))
        yf=int(input(" Y> "))
        undovalores.append([config.grosor,xi,yi,xf,yf])
        undofuncion.append(linea)
        nundo=nundo+1
        linea(config.grosor,xi,yi,xf,yf,config.color)

    if cmd == "cuadrado":
        xi=int(input("Coordenada de la esquina superior izquierda \n X> "))
        yi=int(input(" Y> "))
        lado=int(input("valor del lado> "))
        undovalores.append([config.grosor,xi,yi,lado])
        undofuncion.append(cuadrado)
        nundo=nundo+1
        cuadrado(config.grosor,xi,yi,lado,config.color)

    if cmd == "rectangulo":
        xi=int(input("Coordenada de la esquina superior izquierda \n X> "))
        yi=int(input(" Y> "))
        base=int(input("valor de la base> "))
        altura=int(input("valor de la altura> "))
        undovalores.append([config.grosor,xi,yi,base,altura])
        undofuncion.append(rectangulo)
        nundo=nundo+1
        rectangulo(config.grosor,xi,yi,base,altura,config.color)

    if cmd == "circulo":
        x=int(input("Coordenada centro del circulo \n X> "))
        y=int(input(" Y> "))
        radio=int(input("radio del circulo> "))
        undovalores.append([config.grosor,x,y,radio])
        undofuncion.append(circulo)
        nundo=nundo+1
        circulo(config.grosor,x,y,radio,config.color)

    if cmd == "triangulo equilatero":
        xi=int(input("Coordenada de la esquina inferior izquierda \n X> "))
        yi=int(input(" Y> "))
        lado=int(input("valor del lado> "))
        undovalores.append([config.grosor,xi,yi,lado])
        undofuncion.append(equilatero)
        nundo=nundo+1
        equilatero(config.grosor,xi,yi,lado,config.color)

    if cmd == "triangulo isoseles":
        xi=int(input("Coordenada de la esquina inferior izquierda \n X> "))
        yi=int(input(" Y> "))
        base=int(input("valor de la base> "))
        altura=int(input("valor de la altura> "))
        undovalores.append([config.grosor,xi,yi,base,altura])
        undofuncion.append(isoseles)
        nundo=nundo+1
        isoseles(config.grosor,xi,yi,base,altura,config.color)

    if cmd == "triangulo escaleno":
        xi=int(input("Coordenada de la esquina inferior izquierda \n X> "))
        yi=int(input(" Y> "))
        base=int(input("valor de la base> "))
        altura=int(input("valor de la altura> "))
        undovalores.append([config.grosor,xi,yi,base,altura])
        undofuncion.append(escaleno)
        nundo=nundo+1
        escaleno(config.grosor,xi,yi,base,altura,config.color)

    if cmd == "deshacer":
        if nundo >= 0:
            funcion = undofuncion[nundo]
            funcion(*undovalores[nundo],config.bgcolor)
            undofuncion.pop(nundo)
            undovalores.pop(nundo)
            nundo=nundo-1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()