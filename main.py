#Bienvenido al archivo main
#Este archivo es el que se ejecuta al iniciar el programa

from tkinter import N
import os
import pandas as pd
import PySimpleGUI as sg
import io

from peliculas import Peliculas
peliculas =[]
actorepeli=[]

iteracion = 0
it=0



print("------------Bienvenido al programa------------")
print('Curso Lenguajes Formales y de Programación, Seccion B+,Sebastian solares')
print('Carnet: 202004822')
print('----------------------------------------------')

def __init__(self):
    
    self.nombre = []
    self.actores = []
    self.año = []
    self.genero = []

def agregarNombre(self,nombre):
    self.nombre.append(nombre)

def agregarActores(self,actores):
    self.actores.append(actores)

def agregarAño(self,año):
    self.año.append(año)

def agregarGenero(self,genero):
    self.genero.append(genero)        

def agregarPelicula(self,nombre,actores,año,genero):
    self.peliculas.append(Peliculas(nombre,actores,año,genero))

def cargarArchivos():
    global df
    global ruta
    global leido
    
    sg.theme('LightTeal') 

    layout = [[sg.Text('Filename')],
              [sg.Input(), sg.FileBrowse(file_types=(( "*.lfp"),))],
              [sg.OK("ok")]]

    window = sg.Window('Cargar Archivo LFP', layout,)

    while True:

        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancesdal'):
            break
        elif event == "ok" :
            general =[]
            while True:
                try:
                     
                    print("RUTA DEL ARCHIVO:" + values[0])
                    
                    
                    sg.popup('Archivo cargado correctamente')
                    
                    ruta = values[0]
                
                    break
                    
                except:
                    sg.popup('El archivo no se cargo correctamente')
                    break
            
            window.close() 
def addPeliculas():
    exit =False
    pelirepetida =False
    

    try:
        objeto = open(ruta, "r+")
        
        info =objeto.read()

        infoxlinea= info.splitlines()

      

        for x in infoxlinea:
            
            line = x.split(";")

            name = line[0]
            actor= line[1]
            year= line[2]
            
            gender= line[3]
            
            
            peliagregada=Peliculas(name,actor,year,gender)
            actorAgg = actor
            
            for i in range(len(peliculas)):
                
                if peliculas[i].nombre == name:
                    print("Ya existe una pelicula con ese nombre")
                    pelirepetida=True

            if pelirepetida == False:

                peliculas.append(peliagregada)
                acc =actorAgg.split(",")
                for dent in acc:

                    actorepeli.append(dent)
                
                print("Pelicula agregada con exito")
            pelirepetida=False
        

        while exit== False:
            
            #menu De gestion de peliculas
            print('----------------------------------------------')
            print('------------GESTION DE PELICULAS--------------')
            print("--1. Mostrar peliculas--")
            print("--2. Mostrar Actores--")  
            print("--3. Regresar--")  
            print('----------------------------------------------')
            
            opcion2 = int(input("Ingrese una opcion: "))
            
            if opcion2 == 1:
                exit = False
                
                print('----------hola estas en el apartado de mostrar peliculas----------')
                for x in range(len(peliculas)):
                    Peliculas.imprimirPeliculas(peliculas[x])
            elif opcion2 == 2:
                exit = False
                
                print('-----------hola estas en el apartado de mostrar actores------------------')
                for i in range(len(peliculas)):
                    count= i+1
                    print(count,peliculas[i].nombre)

                opcion3 = int(input("Ingrese una opcion: "))
                print('Actores: ',peliculas[opcion3-1].actores)


                    
            elif opcion2 == 3:
                    exit= True
                    
        
            else:
                print('introduce un numero entre el 1 y el 3')     
    except:
        print("------------No se ha cargado ningun archivo------------")
        pass

def grafico():
    global peli
    data = '''
    digraph main {
        graph [pad="0.5", nodesep="0.5", ranksep="2"];
        node [shape=plain]
        rankdir=LR;\n
    '''

    global iteracion_2
    iteracion_2 = 1


    
    peli={
        
    }
    
    
    
    for xy in range(len(peliculas)):
        
        actlist =peliculas[xy].actores
        actlist2 = actlist.split(",")
        
        
        jaja = {
            peliculas[xy].nombre:{
                
                'Actores': actlist2,
                'Anio': peliculas[xy].año,
                'Genero': peliculas[xy].genero
                },
        }
        peli.update(jaja)
        
    
    

    
    
    def crear_nodo(pelicula, anio, genero):
        global iteracion
        iteracion += 1
        return f'''\nnodo{iteracion} [label=<
        <table border="0" cellborder="1" cellspacing="0">
        <tr><td bgcolor="#0091ea" port="p1" colspan="2">{pelicula}</td></tr>
        <tr><td> {anio} </td><td> {genero} </td></tr>
        </table>>];\n\n'''

    def crear_actor(actor):
        return f'\t"{actor}"\n' # Eso lo pueden omitir xd
        

    def crear_relacion(nodo,actor):
        return f'''\tnodo{nodo}:p1 -> "{actor}";\n'''

    def agregar_estilo():

        data += 'node [shape=box, style=filled, fillcolor="#00c853"]\n'

    # Aqui creamos los nodos de peliculas
    for pelicula in peli.keys():
        anio = peli[pelicula]['Anio']
        genero = peli[pelicula]['Genero']
        nodo =crear_nodo(pelicula, anio, genero)
        data += nodo

    # Aqui agregamos el estilo a los nodos de actores
    data += 'node [shape=box, style=filled, fillcolor="#00c853"]'
    # Aqui creamos los nodos de actores
    for actor in actorepeli:
        nodo = crear_actor(actor)
        data += nodo

    # Aqui creamos las relaciones
    for pelicula in peli.keys():
        for actor in peli[pelicula]['Actores']:
            relacion = crear_relacion(iteracion_2,actor)
            data += relacion
        iteracion_2 += 1
        
    data += '}'

    # Aqui creamos el archivo
    with open('grafico.dot', 'w') as f:
        f.write(data)

    # Aqui creamos la imagen
    os.system('dot -Tpdf grafico.dot -o grafico.pdf')
           
             
def filtradoPeliculas():
    exit =False
    while exit== False:
            
            #menu De FILTRACION DE PELICULAS
            print('----------------------------------------------')
            print('----------FILTRACION DE PELICULAS-------------')
            print("--1. Filtrado Por Actor--")
            print("--2. Filtrado Por año--")  
            print("--3. Filtrado Por Genero--")  
            print("--4. Regresar--")
            print('----------------------------------------------')
            
            opcion2 = int(input("Ingrese una opcion: "))
            
            if opcion2 == 1:
                encontrado = False
                encontrado2 = False
                count=0
                print('----------hola estas en el apartado de filtrado por actor----------')
                opc = str(input("Ingrese el nombre del actor: "))
                
                for i in range(len(peliculas)):
                    
                    count= i+1
                    
                    if peliculas[i].actores== opc:
                    
                        encontrado = True
                        print('actor encontrado')
                    else:
                        encontrado = False
                        print('actor no encontrado')    

                if encontrado == True:
                    print('Pelicula: ',peliculas[count-1].nombre)
                        
            elif opcion2 == 2:
                try:
                    print('----------hola estas en el apartado de filtrado por año----------')
                    count2 = 0
                    opc2 = int(input("Ingrese el año: "))
                    for i in range(len(peliculas)):
                        
                        
                        
                        if int(peliculas[i].año)== int(opc2):
                            
                            print('Año: ',peliculas[i].año,'Pelicula: ',peliculas[i].nombre, 'Genero: ',peliculas[i].genero) 
                            encontrado = True
                            
                            
                        else:
                            count2= i+1
                            
                except:
                    print('Solo se pueden ingresar numeros')
                

            elif opcion2 == 3:
                try:
                    print('----------hola estas en el apartado de filtrado por Genero----------')
                    count3 = 0
                    opc3 = str(input("Ingrese el genero: "))
                    for i in range(len(peliculas)):
                        
                        cadenaGenero = peliculas[i].genero
                        cadenaGenero2 = cadenaGenero.replace("  ","")
                        
                        if str(peliculas[i].genero.replace(' ','')) == str(opc3):
                            
                            print('Pelicula: ',peliculas[i].nombre, 'Genero: ',peliculas[i].genero) 
                            encontrado2 = True
                            
                            
                        else:
                            count3= i+1
                            
                except:
                    print('Solo se pueden ingresar letras')


                    
            elif opcion2 == 4:
                    exit= True
                    
        
            else:
                print('introduce un numero entre el 1 y el 4')     
    
         
            
def MenuPrincipal():
    

    #menu en consola
    print('-------------BIENVENIDO-----------')
    print("--1. Cargar Archivo de Entrada--")
    print("--2. Gestionar Peliculas--")
    print("--3. Filtrado de Peliculas--")
    print("--4. Graficar Peliculas--")
    print("--5. Salir--")
    
while  True:
        MenuPrincipal()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:

            cargarArchivos()
        elif opcion == 2:
            
            addPeliculas()
                
        elif opcion == 3:
                filtradoPeliculas()

        elif opcion == 4:
                grafico()

        elif opcion == 5:
                print("Gracias por usar el programa")
                exit = True
                break
        else:
            print('introduce un numero entre el 1 y el 5')    
                
    





