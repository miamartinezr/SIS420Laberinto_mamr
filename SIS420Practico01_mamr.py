#!/usr/bin/env python
# coding: utf-8

# In[4]:


def mostrarMenu(opciones):
    print('Seleccione una opcion: ')
    for clave in sorted(opciones):
        print(f'{clave}){opciones[clave][0]}')

def leerOpcion(opciones):
    while(a:= input('Opcion: ')) not in opciones:
        print('Error, opcion incorrecta')
    return a
    
def ejecutarOpcion(opcion, opciones):
    opciones[opcion][1]()
    
def generarMenu(opciones, opcionSalida):
    opcion = None
    while opcion != opcionSalida:
        mostrarMenu(opciones)
        opcion = leerOpcion(opciones)
        ejecutarOpcion(opcion, opciones)
        print()

def menuPrincipal():
    opciones = {
        '1': ('Imprimir biografia', accion1),
        '2': ('Salir', salir)
    }
    generarMenu(opciones, '2')
    
def accion1():
    print('Biografia ')
    print('Nombre: Milton Angel Martinez Rodriguez')
    print('Carrera: Ingenieria en Ciencias de la Computacion')
    print('CI: 10320437 ')
    print('CU: 111-408')
    
def salir():
    print('Estas saliendo')
    
if __name__ == '__main__':
    menuPrincipal()

